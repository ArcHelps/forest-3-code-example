"""Local trace explorer for the FOREST-3 code-link example.

Serves a browser UI over this repository. The item markers are rescanned on
every page load, so edits show up after a refresh. Example files are parsed,
never imported or executed. Standard library only; run from the repo root:

    python web/server.py
"""

import argparse
import ast
import json
import re
import subprocess
import sys
import time
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATIC = Path(__file__).resolve().parent / "static"
SCAN_DIRS = ("examples", "src", "tests")
MARKER = re.compile(r"\bARC-FOREST3-([A-Z]+)-(\d+)\b")
TEST_LINE = re.compile(r"^(\w+) \(([\w.]+)\) \.\.\. (.+)$")

KINDS = {
    "SYS": "System",
    "REQ": "Requirement",
    "PROP": "Property",
    "RSK": "Risk",
    "TST": "Test case",
    "TPL": "Test plan",
}


def _anchors(tree):
    """Map each statement's first line to what a marker above it annotates."""
    anchors = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            anchors[node.lineno] = {"symbol": node.name, "node": node}
        elif isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name):
                if target.id == "RECORDS" and isinstance(node.value, ast.List):
                    for element in node.value.elts:
                        if isinstance(element, ast.Dict):
                            anchors[element.lineno] = {"record": element}
                else:
                    anchors.setdefault(
                        node.lineno, {"symbol": target.id, "node": node}
                    )
    return anchors


def _next_code_line(lines, index):
    for number in range(index + 1, len(lines)):
        stripped = lines[number].strip()
        if stripped and not stripped.startswith("#"):
            return number + 1
    return None


def scan():
    files, items, anchored = {}, {}, {}
    for directory in SCAN_DIRS:
        for path in sorted((ROOT / directory).rglob("*.py")):
            rel = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8")
            files[rel] = text
            lines = text.splitlines()
            anchors = _anchors(ast.parse(text, filename=rel))
            for index, line in enumerate(lines):
                for match in MARKER.finditer(line):
                    item_id = match.group(0)
                    kind = match.group(1)
                    item = items.setdefault(
                        item_id,
                        {
                            "id": item_id,
                            "kind": kind,
                            "kindLabel": KINDS.get(kind, kind),
                            "ref": None,
                            "name": None,
                            "fields": {},
                            "locations": [],
                        },
                    )
                    start = _next_code_line(lines, index)
                    anchor = anchors.get(start, {})
                    location = {"path": rel, "line": index + 1}
                    if "record" in anchor:
                        record = ast.literal_eval(anchor["record"])
                        item["ref"] = record.get("reference")
                        item["name"] = record.get("name")
                        item["fields"] = {
                            key: value
                            for key, value in record.items()
                            if key not in ("reference", "name")
                        }
                        location["role"] = "definition"
                    else:
                        location["role"] = "test" if directory == "tests" else "source"
                        if anchor:
                            location["symbol"] = anchor["symbol"]
                            location["endLine"] = anchor["node"].end_lineno
                            key = (rel, start)
                            anchored.setdefault(key, []).append(item_id)
                    item["locations"].append(location)

    return {
        "kinds": KINDS,
        "items": items,
        "links": _links(items, anchored),
        "propertyValues": _property_values(items),
        "files": files,
        "scannedAt": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


def _links(items, anchored):
    by_ref = {item["ref"]: item for item in items.values() if item["ref"]}
    systems = {item["ref"] for item in items.values() if item["kind"] == "SYS"}
    links = []

    # Test case "V-STR-001" verifies requirement "STR-001" by naming convention.
    for item in items.values():
        ref = item["ref"] or ""
        target = by_ref.get(ref[2:]) if ref.startswith("V-") else None
        if item["kind"] == "TST" and target and target["kind"] == "REQ":
            links.append({"source": item["id"], "target": target["id"], "kind": "verifies"})

    # "STR-001", "V-STR-001" and "STR_mass" all belong to system "STR".
    for item in items.values():
        ref = (item["ref"] or "").removeprefix("V-")
        prefix = re.split(r"[-_]", ref, maxsplit=1)[0]
        if item["kind"] != "SYS" and prefix in systems:
            links.append(
                {"source": item["id"], "target": by_ref[prefix]["id"], "kind": "subsystem"}
            )

    # A record's text naming another record's reference.
    names = sorted(by_ref, key=len, reverse=True)
    pattern = re.compile(r"\b(" + "|".join(map(re.escape, names)) + r")\b")
    for item in items.values():
        found = set()
        for value in item["fields"].values():
            found.update(pattern.findall(str(value)))
        for ref in sorted(found - {item["ref"]}):
            links.append({"source": item["id"], "target": by_ref[ref]["id"], "kind": "mentions"})

    # Markers sharing one function or test in src/ or tests/.
    for ids in anchored.values():
        for index, source in enumerate(ids):
            for target in ids[index + 1 :]:
                links.append({"source": source, "target": target, "kind": "co-tagged"})

    return links


def _arithmetic(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_arithmetic(node.operand)
    if isinstance(node, ast.BinOp):
        left, right = _arithmetic(node.left), _arithmetic(node.right)
        operations = {
            ast.Add: lambda: left + right,
            ast.Sub: lambda: left - right,
            ast.Mult: lambda: left * right,
            ast.Div: lambda: left / right,
        }
        if type(node.op) in operations:
            return operations[type(node.op)]()
    raise ValueError("unsupported expression")


def _property_values(items):
    """Evaluate property expressions such as "2.4 kg" or "@{ref:A}+@{ref:B}"."""
    by_ref = {item["ref"]: item for item in items.values() if item["kind"] == "PROP"}
    values = {}

    def evaluate(ref, seen):
        if ref in values:
            return values[ref]["value"]
        if ref not in by_ref or ref in seen:
            raise ValueError(f"cannot resolve {ref}")
        fields = by_ref[ref]["fields"]
        unit = fields.get("unit", "")
        expression = re.sub(
            r"@\{ref:([\w-]+)\}",
            lambda match: repr(evaluate(match.group(1), seen | {ref})),
            fields.get("expression", ""),
        )
        if unit:
            expression = expression.replace(unit, "")
        value = round(_arithmetic(ast.parse(expression.strip(), mode="eval").body), 9)
        values[ref] = {"value": value, "unit": unit}
        return value

    for ref in by_ref:
        try:
            evaluate(ref, frozenset())
        except (ValueError, SyntaxError, ZeroDivisionError):
            values[ref] = {"value": None, "unit": by_ref[ref]["fields"].get("unit", "")}
    return values


def run_tests():
    started = time.perf_counter()
    completed = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=120,
    )
    output = completed.stderr + completed.stdout
    results = []
    for line in output.splitlines():
        match = TEST_LINE.match(line)
        if match:
            name, dotted, status = match.groups()
            module = dotted.split(".")[0]
            results.append(
                {
                    "name": name,
                    "path": f"tests/{module}.py",
                    "status": status.split()[0].lower(),
                    "detail": status,
                }
            )
    return {
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "results": results,
        "output": output,
        "seconds": round(time.perf_counter() - started, 2),
        "ranAt": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_GET(self):
        if self.path.split("?")[0] == "/api/data":
            return self._json(scan())
        return super().do_GET()

    def do_POST(self):
        if self.path == "/api/tests":
            return self._json(run_tests())
        self.send_error(HTTPStatus.NOT_FOUND)

    def _json(self, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"FOREST-3 trace explorer running at http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
