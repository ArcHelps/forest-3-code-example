"use strict";

const KIND_ORDER = ["SYS", "REQ", "PROP", "RSK", "TST", "TPL"];
const AREA_LABELS = {
  CUST: "Customer",
  MIS: "Mission",
  INT: "Integration",
  VRF: "Verification",
  OPS: "Operations",
};
const MARKER_RE = /\bARC-FOREST3-([A-Z]+)-(\d+)\b/g;
const TOKEN_RE = new RegExp(
  [
    String.raw`"""[\s\S]*?"""`,
    String.raw`'''[\s\S]*?'''`,
    String.raw`"(?:\\.|[^"\\\n])*"`,
    String.raw`'(?:\\.|[^'\\\n])*'`,
    String.raw`#[^\n]*`,
    String.raw`\b(?:False|None|True|and|as|assert|async|await|break|class|continue|def|elif|else|except|finally|for|from|if|import|in|is|lambda|not|or|pass|raise|return|try|while|with|yield)\b`,
    String.raw`\b\d+(?:\.\d+)?\b`,
  ].join("|"),
  "g",
);

const app = document.getElementById("app");
const state = {
  data: null,
  index: null,
  tests: null,
  testsRunning: false,
  kind: "ALL",
  query: "",
  highlighted: new Map(),
};

// Helpers

const esc = (value) =>
  String(value ?? "").replace(
    /[&<>"']/g,
    (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c],
  );
const escapeRegex = (text) => text.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const kindStyle = (kind) => `style="--kind: var(--k-${esc(kind)})"`;
const shortId = (id) => id.replace(/^ARC-FOREST3-/, "");
const itemHref = (id) => `#/items/${encodeURIComponent(id)}`;
const codeHref = (path, line) =>
  `#/code/${path.split("/").map(encodeURIComponent).join("/")}${line ? `?line=${line}` : ""}`;
const plural = (n, word) =>
  `${n} ${n === 1 ? word : /[^aeiou]y$/.test(word) ? `${word.slice(0, -1)}ies` : `${word}s`}`;
const formatNumber = (value) =>
  Number(value).toLocaleString(undefined, { maximumFractionDigits: 3 });
const prettyLabel = (key) => {
  const words = key.replace(/_/g, " ");
  return words.charAt(0).toUpperCase() + words.slice(1);
};
const byKindThenId = (a, b) =>
  KIND_ORDER.indexOf(a.kind) - KIND_ORDER.indexOf(b.kind) || a.id.localeCompare(b.id);

function countBy(list, key) {
  const counts = {};
  for (const entry of list) counts[key(entry)] = (counts[key(entry)] || 0) + 1;
  return counts;
}

function isVisibleIn(element, container) {
  const a = element.getBoundingClientRect();
  const b = container.getBoundingClientRect();
  return a.top >= b.top && a.bottom <= b.bottom;
}

// Data

async function load() {
  const response = await fetch("/api/data");
  if (!response.ok) throw new Error(`Scan failed (HTTP ${response.status})`);
  state.data = await response.json();
  state.index = buildIndex(state.data);
  state.highlighted.clear();
}

function buildIndex(data) {
  const items = Object.values(data.items).sort(byKindThenId);
  const byRef = new Map(items.filter((item) => item.ref).map((item) => [item.ref, item]));
  const outgoing = new Map(items.map((item) => [item.id, []]));
  const incoming = new Map(items.map((item) => [item.id, []]));

  // A record naming its own subsystem is already covered by the subsystem link.
  const subsystem = new Set(
    data.links.filter((l) => l.kind === "subsystem").map((l) => `${l.source}>${l.target}`),
  );
  for (const link of data.links) {
    if (link.kind === "mentions" && subsystem.has(`${link.source}>${link.target}`)) continue;
    outgoing.get(link.source)?.push(link);
    incoming.get(link.target)?.push(link);
  }

  const refs = [...byRef.keys()].sort((a, b) => b.length - a.length).map(escapeRegex);
  const refPattern = new RegExp(
    String.raw`\{\{property:ref:([\w-]+)\}\}|@\{ref:([\w-]+)\}` +
      (refs.length ? String.raw`|\b(${refs.join("|")})\b` : ""),
    "g",
  );

  const markersByFile = new Map();
  for (const item of items) {
    for (const location of item.locations) {
      if (!markersByFile.has(location.path)) markersByFile.set(location.path, []);
      markersByFile.get(location.path).push({ item, location });
    }
  }
  return { items, byRef, outgoing, incoming, refPattern, markersByFile };
}

function isVerified(item) {
  return state.index.incoming.get(item.id).some((link) => link.kind === "verifies");
}

function codeLocations(item) {
  return item.locations.filter((location) => location.role !== "definition");
}

// Shared rendering

function refChip(item, { showName = true } = {}) {
  const label = item.ref || shortId(item.id);
  return `<a class="chip" ${kindStyle(item.kind)} href="${itemHref(item.id)}" title="${esc(
    `${item.kindLabel} · ${shortId(item.id)}${item.name ? ` · ${item.name}` : ""}`,
  )}"><span class="dot"></span><span class="chip-ref">${esc(label)}</span>${
    showName && item.name ? `<span class="chip-name">${esc(item.name)}</span>` : ""
  }</a>`;
}

function kindPill(kind) {
  return `<span class="pill kind" ${kindStyle(kind)}><span class="dot"></span>${esc(
    state.data.kinds[kind] || kind,
  )}</span>`;
}

function linkify(text) {
  const { refPattern, byRef } = state.index;
  const source = String(text);
  let html = "";
  let last = 0;
  for (const match of source.matchAll(refPattern)) {
    html += esc(source.slice(last, match.index));
    last = match.index + match[0].length;
    const ref = match[1] || match[2] || match[3];
    const item = byRef.get(ref);
    if (!item) {
      html += esc(match[0]);
      continue;
    }
    let label = ref;
    const value = state.data.propertyValues[ref];
    if (match[1] && value && value.value !== null) {
      label = `${formatNumber(value.value)} ${value.unit}`.trim();
    }
    html += `<a class="inline-ref" ${kindStyle(item.kind)} href="${itemHref(item.id)}" title="${esc(
      `${item.kindLabel} ${ref}${item.name ? ` · ${item.name}` : ""}`,
    )}">${esc(label)}</a>`;
  }
  return html + esc(source.slice(last));
}

function markerLink(id) {
  const item = state.data.items[id];
  const kind = item ? item.kind : id.split("-")[2];
  const title = item ? `${item.kindLabel}${item.name ? ` · ${item.name}` : ""}` : "Unknown item";
  return `<a class="tok-marker" ${kindStyle(kind)} href="${itemHref(id)}" title="${esc(title)}">${esc(
    id,
  )}</a>`;
}

function highlightedLines(path) {
  if (state.highlighted.has(path)) return state.highlighted.get(path);
  const text = state.data.files[path] ?? "";
  const lines = [""];
  const push = (chunk, cls) => {
    chunk.split("\n").forEach((part, index) => {
      if (index) lines.push("");
      if (!part) return;
      let html = esc(part);
      if (cls === "comment") html = html.replace(MARKER_RE, (id) => markerLink(id));
      lines[lines.length - 1] += cls ? `<span class="tok-${cls}">${html}</span>` : html;
    });
  };
  let last = 0;
  for (const match of text.matchAll(TOKEN_RE)) {
    push(text.slice(last, match.index), null);
    const token = match[0];
    const cls = token.startsWith("#")
      ? "comment"
      : /^["']/.test(token)
        ? "string"
        : /^\d/.test(token)
          ? "number"
          : "keyword";
    push(token, cls);
    last = match.index + token.length;
  }
  push(text.slice(last), null);
  if (lines.length > 1 && lines[lines.length - 1] === "") lines.pop();
  state.highlighted.set(path, lines);
  return lines;
}

function codeLines(path, from, to, highlightLine) {
  const lines = highlightedLines(path);
  const start = Math.max(1, from);
  const end = Math.min(lines.length, to);
  let html = "";
  for (let number = start; number <= end; number += 1) {
    html += `<div class="ln${number === highlightLine ? " hl" : ""}" data-line="${number}"><a class="num" href="${codeHref(
      path,
      number,
    )}">${number}</a><span class="src">${lines[number - 1] || " "}</span></div>`;
  }
  return html;
}

// Overview

function renderOverview() {
  const { items, byRef } = state.index;
  const counts = countBy(items, (item) => item.kind);
  const requirements = items.filter((item) => item.kind === "REQ");
  const verified = requirements.filter(isVerified);
  const gaps = requirements.filter((item) => !isVerified(item));
  const located = items.filter((item) => item.locations.length);
  const inCode = items.filter((item) => codeLocations(item).length);

  const tiles = KIND_ORDER.filter((kind) => counts[kind])
    .map(
      (kind) => `<a class="tile" ${kindStyle(kind)} href="#/items?type=${kind}">
        <div class="tile-count">${counts[kind]}</div>
        <div class="tile-label">${esc(plural(counts[kind], state.data.kinds[kind]).replace(/^\d+ /, ""))}</div>
      </a>`,
    )
    .join("");

  const percent = (n, d) => (d ? Math.round((n / d) * 100) : 0);
  const metric = (label, n, d, foot = "") => `<div>
      <div class="metric-row"><span class="metric-label">${label}</span>
        <span class="metric-value"><strong>${n}</strong> / ${d}</span></div>
      <div class="bar"><span style="width:${percent(n, d)}%"></span></div>
      ${foot ? `<div class="metric-foot">${foot}</div>` : ""}
    </div>`;

  const testMetric = (() => {
    if (state.testsRunning && !state.tests) return `<span class="pill">Running…</span>`;
    if (!state.tests) return `<span class="pill">Not run yet</span>`;
    if (state.tests.error) return `<span class="pill bad">${esc(state.tests.error)}</span>`;
    const passed = state.tests.results.filter((r) => r.status === "ok").length;
    const total = state.tests.results.length;
    return `<span class="pill ${state.tests.ok ? "ok" : "bad"}">${passed} / ${total} passing</span>
      <a href="#/tests">Details</a>`;
  })();

  const traceability = `<div class="card">
      <h2>Traceability</h2>
      <p class="sub">What the markers in this repo connect.</p>
      <div class="metrics">
        ${metric("Items with a file-and-line link", located.length, items.length)}
        ${metric(
          "Requirements with a test case",
          verified.length,
          requirements.length,
          gaps.length
            ? `<span class="gap">${plural(gaps.length, "gap")}:</span> ${gaps.map((g) => refChip(g)).join("")}`
            : "Every requirement has a test case.",
        )}
        <div>
          <div class="metric-row"><span class="metric-label">Items linked from src/ or tests/</span>
            <span class="metric-value"><strong>${inCode.length}</strong> / ${items.length}</span></div>
          <div class="chips">${inCode.map((item) => refChip(item, { showName: false })).join("")}</div>
        </div>
        <div>
          <div class="metric-row"><span class="metric-label">Unit tests</span>
            <span class="metric-value">${testMetric}</span></div>
        </div>
      </div>
    </div>`;

  const areas = new Map();
  for (const item of requirements) {
    const area = (item.ref || "").split("-")[0];
    if (!areas.has(area)) areas.set(area, []);
    areas.get(area).push(item);
  }
  const areaRows = [...areas]
    .map(([area, list]) => {
      const system = byRef.get(area);
      const label =
        system && system.kind === "SYS"
          ? `<a href="${itemHref(system.id)}">${esc(system.name)}</a>`
          : esc(AREA_LABELS[area] || area);
      const done = list.filter(isVerified).length;
      const linked = list.filter((item) => codeLocations(item).length).length;
      return `<tr>
        <td><span class="mono">${esc(area)}</span> · ${label}</td>
        <td class="num">${list.length}</td>
        <td><div class="cell-bar"><div class="bar"><span style="width:${percent(done, list.length)}%"></span></div>
          <span class="mono ${done < list.length ? "gap" : ""}">${done}/${list.length}</span></div></td>
        <td class="num">${linked || "–"}</td>
      </tr>`;
    })
    .join("");

  const coverage = `<div class="card">
      <h2>Requirement coverage by area</h2>
      <p class="sub">Grouped by reference prefix. A test case <span class="mono">V-STR-001</span> covers requirement <span class="mono">STR-001</span>.</p>
      <table>
        <thead><tr><th>Area</th><th class="num">Reqs</th><th>With test case</th><th class="num">In code</th></tr></thead>
        <tbody>${areaRows}</tbody>
      </table>
    </div>`;

  const codeLinkGroups = new Map();
  for (const item of inCode) {
    for (const location of codeLocations(item)) {
      const key = `${location.path}:${location.symbol || location.line}`;
      if (!codeLinkGroups.has(key)) codeLinkGroups.set(key, { location, items: [] });
      codeLinkGroups.get(key).items.push(item);
    }
  }
  const codeLinks = `<div class="card">
      <h2>Linked in src/ and tests/</h2>
      <p class="sub">Functions and tests carrying item markers.</p>
      <div class="code-links">${[...codeLinkGroups.values()]
        .sort((a, b) => a.location.path.localeCompare(b.location.path) || a.location.line - b.location.line)
        .map(
          ({ location, items: tagged }) => `<div class="code-link">
            <div><div class="symbol">${esc(location.symbol || "(module)")}</div>
              <a class="where" href="${codeHref(location.path, location.line)}">${esc(location.path)}:${location.line}</a></div>
            <span class="pill">${location.role === "test" ? "test" : "source"}</span>
            <div class="chips" style="grid-column: 1 / -1">${tagged.sort(byKindThenId).map((item) => refChip(item)).join("")}</div>
          </div>`,
        )
        .join("")}</div>
    </div>`;

  app.innerHTML = `<div class="page">
      <h1>FOREST-3 trace explorer</h1>
      <p class="lede">Every Arc item marker in this repository, where it sits in the code, and how the items relate. Rescanned from the files on each load (${esc(state.data.scannedAt)}).</p>
      <p class="note">Illustrative sample data from Arc's FOREST-3 demo: not flight software, real mission requirements, or verification evidence. A code link records an association, not proof that a requirement is met.</p>
      <div class="tiles">${tiles}</div>
      <div class="grid grid-2">${traceability}${coverage}</div>
      <div class="grid grid-2 section">${renderBudget()}${codeLinks}</div>
    </div>`;
}

function renderBudget() {
  const { byRef } = state.index;
  const values = state.data.propertyValues;
  const rows = Object.keys(values)
    .filter((ref) => values[`${ref}_limit`] && values[ref].value !== null)
    .map((ref) => {
      const prefix = ref.split("_")[0];
      const system = byRef.get(prefix);
      return {
        ref,
        item: byRef.get(ref),
        name: system && system.kind === "SYS" ? system.name : prefix.charAt(0).toUpperCase() + prefix.slice(1),
        value: values[ref].value,
        limit: values[`${ref}_limit`].value,
        unit: values[ref].unit,
        computed: /@\{ref:/.test(byRef.get(ref)?.fields.expression || ""),
      };
    });
  if (!rows.length) return "";

  const parts = rows.filter((row) => !row.computed);
  const totals = rows.filter((row) => row.computed);
  const row = (entry, scale) => {
    const over = entry.value > entry.limit;
    const margin = entry.limit - entry.value;
    return `<a class="budget-row" href="${itemHref(entry.item.id)}" style="color: inherit; text-decoration: none"
        title="${esc(entry.ref)}">
        <span class="budget-name">${esc(entry.computed ? `${entry.name} (total)` : entry.name)}</span>
        <span class="budget-track">
          <span class="budget-fill${over ? " over" : ""}" style="width:${Math.min(100, (entry.value / scale) * 100)}%"></span>
          <span class="budget-limit" style="left:calc(${Math.min(100, (entry.limit / scale) * 100)}% - 1px)"></span>
        </span>
        <span class="budget-value">${formatNumber(entry.value)} / ${formatNumber(entry.limit)} ${esc(entry.unit)}
          <span class="margin">· ${over ? "over by " : ""}${formatNumber(Math.abs(margin))} ${over ? "" : "spare"}</span></span>
      </a>`;
  };
  const scale = Math.max(...parts.map((p) => Math.max(p.value, p.limit)));
  return `<div class="card">
      <h2>Mass budget</h2>
      <p class="sub">Evaluated from the property records. The total is the sum expression in <span class="mono">vehicle_mass</span>.</p>
      <div class="budget">
        ${parts.map((p) => row(p, scale)).join("")}
        ${totals.map((t) => `<div class="budget-total">${row(t, Math.max(t.value, t.limit))}</div>`).join("")}
      </div>
      <div class="legend"><span><i></i>Current mass</span><span><i class="limit"></i>Limit</span></div>
    </div>`;
}

// Items

function filteredItems() {
  const query = state.query.trim().toLowerCase();
  return state.index.items.filter((item) => {
    if (state.kind !== "ALL" && item.kind !== state.kind) return false;
    if (!query) return true;
    const haystack = [item.id, item.ref, item.name, ...Object.values(item.fields)]
      .join(" ")
      .toLowerCase();
    return haystack.includes(query);
  });
}

function renderItemList(selectedId) {
  const list = document.getElementById("item-list");
  const count = document.getElementById("item-count");
  if (!list) return;
  const items = filteredItems();
  count.textContent = `${plural(items.length, "item")}${state.query ? ` matching “${state.query}”` : ""}`;
  list.innerHTML = items.length
    ? items
        .map(
          (item) => `<a href="${itemHref(item.id)}" class="${item.id === selectedId ? "selected" : ""}" ${kindStyle(item.kind)}>
            <span class="dot"></span>
            <span class="row-top"><span class="row-ref">${esc(item.ref || shortId(item.id))}</span>
              <span class="row-id">${esc(shortId(item.id))}</span></span>
            <span class="row-name">${esc(item.name || "")}</span>
          </a>`,
        )
        .join("")
    : `<div class="empty">No items match.</div>`;
}

function renderItems(route) {
  if (route.params.has("type") || route.params.has("q")) {
    state.kind = route.params.get("type") || "ALL";
    state.query = route.params.get("q") || "";
  }
  const selected = route.rest[0] ? state.data.items[route.rest[0]] : null;
  const counts = countBy(state.index.items, (item) => item.kind);
  const base = selected ? itemHref(selected.id) : "#/items";
  const filterLink = (kind, label, n) => {
    const style = kind === "ALL" ? "" : kindStyle(kind);
    const params = new URLSearchParams({ type: kind });
    if (state.query) params.set("q", state.query);
    return `<a href="${base}?${params}" class="${state.kind === kind ? "active" : ""}" ${style}>
      ${kind === "ALL" ? "" : `<span class="dot"></span>`}${esc(label)} <span class="n">${n}</span></a>`;
  };

  app.innerHTML = `<div class="split ${selected ? "has-selection" : ""}">
      <aside class="pane-left">
        <div class="filters">
          <input id="item-search" class="search" type="search" placeholder="Search IDs, names and text…"
            value="${esc(state.query)}" autocomplete="off" aria-label="Search items" />
          <div class="kind-filter">
            ${filterLink("ALL", "All", state.index.items.length)}
            ${KIND_ORDER.filter((k) => counts[k]).map((k) => filterLink(k, state.data.kinds[k], counts[k])).join("")}
          </div>
          <div class="result-count" id="item-count"></div>
        </div>
        <nav class="list" id="item-list" data-keep-scroll="items-list" aria-label="Items"></nav>
      </aside>
      <section class="pane-right">${
        selected
          ? renderItemDetail(selected)
          : route.rest[0]
            ? `<div class="empty-state">No item <span class="mono">${esc(route.rest[0])}</span> in this repository.</div>`
            : `<div class="empty-state">
                <h1 style="font-size:20px;margin:0 0 8px;color:var(--text)">Pick an item</h1>
                Each item is a <span class="mono">ARC-FOREST3-&lt;TYPE&gt;-&lt;NUMBER&gt;</span> marker comment in the code.
                Select one to see its record, every place it is tagged, and the items it relates to.
              </div>`
      }</section>
    </div>`;
  renderItemList(selected?.id);
}

function renderItemDetail(item) {
  const { outgoing, incoming } = state.index;
  const items = state.data.items;
  const out = outgoing.get(item.id);
  const inc = incoming.get(item.id);
  const targets = (links) => links.map((link) => items[link.target]);
  const sources = (links) => links.map((link) => items[link.source]);
  const ofKind = (links, kind) => links.filter((link) => link.kind === kind);

  const fields = Object.entries(item.fields)
    .map(([key, value]) => {
      const rendered = key === "method" ? `<span class="pill">${esc(value)}</span>` : linkify(value);
      return `<div><div class="field-label">${esc(prettyLabel(key))}</div>
        <div class="field-value">${key === "expression" ? `<code>${rendered}</code>` : rendered}</div></div>`;
    })
    .join("");

  let valueCallout = "";
  const value = item.kind === "PROP" && state.data.propertyValues[item.ref];
  if (value && value.value !== null) {
    valueCallout = `<div class="value-callout"><span>Value</span><strong>${formatNumber(value.value)}</strong>
      <span>${esc(value.unit)}</span></div>`;
  }

  const locations = item.locations
    .map((location) => {
      let from = location.line;
      let to = location.endLine || location.line;
      if (location.role === "definition") {
        const raw = (state.data.files[location.path] || "").split("\n");
        to = location.line;
        while (to < raw.length && !raw[to - 1].trim().startsWith("}")) to += 1;
      }
      to = Math.min(to, from + 40);
      const role = {
        definition: `<span class="pill">record</span>`,
        source: `<span class="pill kind" ${kindStyle("REQ")}>source</span>`,
        test: `<span class="pill kind" ${kindStyle("TST")}>test</span>`,
      }[location.role];
      return `<div class="location">
          <div class="location-head">${role}
            <a class="where" href="${codeHref(location.path, location.line)}">${esc(location.path)}:${location.line}</a>
            ${location.symbol ? `<span class="symbol">${esc(location.symbol)}</span>` : ""}</div>
          <div class="code snippet">${codeLines(location.path, from, to, location.line)}</div>
        </div>`;
    })
    .join("");

  const coTagged = [
    ...ofKind(out, "co-tagged").map((link) => items[link.target]),
    ...ofKind(inc, "co-tagged").map((link) => items[link.source]),
  ];
  const groups = [
    ["Verified by", sources(ofKind(inc, "verifies")), "Matched by reference: V-<requirement>."],
    ["Verifies", targets(ofKind(out, "verifies")), "Matched by reference: V-<requirement>."],
    ["Subsystem", targets(ofKind(out, "subsystem")), "Inferred from the reference prefix."],
    ["Tagged alongside in code", coTagged, "Markers on the same function or test."],
    ["Mentions", targets(ofKind(out, "mentions")), "References that appear in this record's text."],
    ["Mentioned by", sources(ofKind(inc, "mentions")), ""],
    ["Subsystem members", sources(ofKind(inc, "subsystem")), ""],
  ].filter(([, list]) => list.length);

  const relations = groups
    .map(
      ([label, list, note]) => `<div>
        <div class="relation-label">${esc(label)} <span class="n">${list.length}</span></div>
        ${note ? `<div class="relation-note">${esc(note)}</div>` : ""}
        <div class="chips">${[...new Set(list)].sort(byKindThenId).map((other) => refChip(other)).join("")}</div>
      </div>`,
    )
    .join("");

  const flags = [];
  if (item.kind === "REQ" && !isVerified(item)) flags.push(`<span class="pill bad">No test case</span>`);
  if (codeLocations(item).length) flags.push(`<span class="pill ok">Linked in code</span>`);

  return `<article class="detail">
      <a class="back-link" href="#/items">← All items</a>
      <div class="detail-head">${kindPill(item.kind)}<span class="mono">${esc(item.ref || "")}</span>${flags.join("")}</div>
      <h1>${esc(item.name || shortId(item.id))}</h1>
      <div class="item-id">${esc(item.id)}</div>
      ${valueCallout ? `<h3>Value</h3>${valueCallout}` : ""}
      ${fields ? `<h3>Record</h3><div class="fields">${fields}</div>` : ""}
      <h3>Where it's tagged · ${plural(item.locations.length, "place")}</h3>
      <div class="locations">${locations}</div>
      <h3>Relationships</h3>
      ${
        relations
          ? `<p class="relation-note" style="margin:0 0 12px">Inferred by this explorer from references and text; Arc may model them differently.</p>
             <div class="relations">${relations}</div>`
          : `<p class="relation-note">No related items found.</p>`
      }
    </article>`;
}

// Code

function renderCode(route) {
  const files = Object.keys(state.data.files);
  const path = route.rest.length ? route.rest.join("/") : files.find((f) => f.startsWith("src/")) || files[0];
  const line = Number(route.params.get("line")) || null;
  const groups = new Map();
  for (const file of files) {
    const dir = file.split("/")[0];
    if (!groups.has(dir)) groups.set(dir, []);
    groups.get(dir).push(file);
  }
  const fileList = [...groups]
    .map(
      ([dir, list]) => `<div class="file-group">${esc(dir)}/</div>${list
        .map((file) => {
          const n = state.index.markersByFile.get(file)?.length || 0;
          return `<a href="${codeHref(file)}" class="${file === path ? "selected" : ""}">
            <span>${esc(file.slice(dir.length + 1))}</span><span class="n">${n || ""}</span></a>`;
        })
        .join("")}`,
    )
    .join("");

  const exists = path in state.data.files;
  const markers = state.index.markersByFile.get(path) || [];
  const total = exists ? highlightedLines(path).length : 0;

  app.innerHTML = `<div class="split has-selection">
      <aside class="pane-left"><nav class="file-list" data-keep-scroll="file-list" aria-label="Files">${fileList}</nav></aside>
      <section class="pane-right" data-keep-scroll="code:${esc(path)}">
        ${
          exists
            ? `<div class="code-head"><a class="back-link" href="#/code" style="margin:0">← Files</a>
                <span class="path">${esc(path)}</span>
                <span class="meta">${plural(total, "line")} · ${plural(markers.length, "marker")}</span></div>
               <div class="code">${codeLines(path, 1, total, line)}</div>`
            : `<div class="empty-state">File <span class="mono">${esc(path)}</span> was not scanned.</div>`
        }
      </section>
    </div>`;
}

// Tests

async function runTests() {
  if (state.testsRunning) return;
  state.testsRunning = true;
  rerenderIfOn("overview", "tests");
  try {
    const response = await fetch("/api/tests", { method: "POST" });
    state.tests = response.ok ? await response.json() : { error: `Test run failed (HTTP ${response.status})` };
  } catch (error) {
    state.tests = { error: `Could not reach the server: ${error.message}` };
  } finally {
    state.testsRunning = false;
    rerenderIfOn("overview", "tests");
  }
}

function renderTests() {
  const tests = state.tests;
  const scanned = new Map();
  for (const item of state.index.items) {
    for (const location of item.locations) {
      if (location.role !== "test" || !location.symbol) continue;
      const key = `${location.path}::${location.symbol}`;
      if (!scanned.has(key)) scanned.set(key, { location, items: [] });
      scanned.get(key).items.push(item);
    }
  }
  const results = tests && !tests.error ? tests.results : [];
  const rows = results.length
    ? results.map((r) => ({ ...r, linked: scanned.get(`${r.path}::${r.name}`) }))
    : [...scanned.values()].map((s) => ({
        name: s.location.symbol,
        path: s.location.path,
        status: null,
        linked: s,
      }));

  const statusPill = (row) => {
    if (state.testsRunning) return `<span class="pill">Running…</span>`;
    if (!row.status) return `<span class="pill">Not run</span>`;
    const cls = row.status === "ok" ? "ok" : row.status === "skipped" ? "warn" : "bad";
    return `<span class="pill ${cls}">${esc(row.status === "ok" ? "passed" : row.detail)}</span>`;
  };

  let summary = "";
  if (tests?.error) summary = `<span class="pill bad">${esc(tests.error)}</span>`;
  else if (tests) {
    const passed = tests.results.filter((r) => r.status === "ok").length;
    summary = `<span class="test-summary"><strong>${passed}</strong> of ${tests.results.length} passed ·
      ${tests.seconds}s · ran ${esc(tests.ranAt)}</span>`;
  }

  app.innerHTML = `<div class="page">
      <h1>Unit tests</h1>
      <p class="lede">Runs <span class="command">python -m unittest discover -s tests -v</span> from the repository root, as the README describes. These illustrative checks are not flight qualification.</p>
      <div class="test-bar">
        <button type="button" data-action="run-tests" ${state.testsRunning ? "disabled" : ""}>${
          state.testsRunning ? "Running…" : tests ? "Run again" : "Run tests"
        }</button>
        ${summary}
      </div>
      <div class="card" style="padding:6px 8px">
        <table>
          <thead><tr><th>Test</th><th>Result</th><th>Linked items</th></tr></thead>
          <tbody>${rows
            .map(
              (row) => `<tr>
                <td><div class="test-name">${esc(row.name)}</div>
                  ${
                    row.linked
                      ? `<a class="mono" href="${codeHref(row.linked.location.path, row.linked.location.line)}">${esc(
                          row.linked.location.path,
                        )}:${row.linked.location.line}</a>`
                      : `<span class="mono">${esc(row.path)}</span>`
                  }</td>
                <td>${statusPill(row)}</td>
                <td><div class="chips">${
                  row.linked ? row.linked.items.sort(byKindThenId).map((item) => refChip(item)).join("") : "–"
                }</div></td>
              </tr>`,
            )
            .join("")}</tbody>
        </table>
      </div>
      ${
        tests?.output
          ? `<details class="raw"><summary>Raw output</summary><pre>${esc(tests.output)}</pre></details>`
          : ""
      }
    </div>`;
}

// Routing

function parseRoute() {
  const raw = location.hash.replace(/^#\/?/, "");
  const [pathPart, queryPart = ""] = raw.split("?");
  const parts = pathPart.split("/").filter(Boolean).map(decodeURIComponent);
  return { section: parts[0] || "overview", rest: parts.slice(1), params: new URLSearchParams(queryPart) };
}

function currentSection() {
  return parseRoute().section;
}

function rerenderIfOn(...sections) {
  if (state.data && sections.includes(currentSection())) render();
}

function render() {
  if (!state.data) return;
  const route = parseRoute();
  const views = { overview: renderOverview, items: renderItems, code: renderCode, tests: renderTests };
  const section = views[route.section] ? route.section : "overview";
  document.querySelectorAll(".tabs a").forEach((tab) => {
    tab.classList.toggle("active", tab.dataset.tab === section);
  });

  const kept = {};
  app.querySelectorAll("[data-keep-scroll]").forEach((el) => {
    kept[el.dataset.keepScroll] = el.scrollTop;
  });
  views[section](route);
  app.querySelectorAll("[data-keep-scroll]").forEach((el) => {
    if (el.dataset.keepScroll in kept) el.scrollTop = kept[el.dataset.keepScroll];
    const target = el.querySelector(".selected, .ln.hl");
    if (target && !isVisibleIn(target, el)) target.scrollIntoView({ block: "center" });
  });
  if (!(section === "code" && route.params.has("line"))) {
    const right = app.querySelector(".pane-right:not([data-keep-scroll])");
    if (right) right.scrollTop = 0;
  }
}

// Events

app.addEventListener("input", (event) => {
  if (event.target.id === "item-search") {
    state.query = event.target.value;
    const route = parseRoute();
    renderItemList(route.rest[0]);
  }
});

app.addEventListener("click", (event) => {
  if (event.target.closest("[data-action='run-tests']")) runTests();
});

document.addEventListener("keydown", (event) => {
  const search = document.getElementById("item-search");
  if (event.key === "/" && search && document.activeElement !== search) {
    event.preventDefault();
    search.focus();
  }
});

document.getElementById("rescan").addEventListener("click", async (event) => {
  const button = event.currentTarget;
  button.disabled = true;
  try {
    await load();
    render();
  } catch (error) {
    app.innerHTML = `<p class="error-box">${esc(error.message)}</p>`;
  } finally {
    button.disabled = false;
  }
});

window.addEventListener("hashchange", render);

(async () => {
  try {
    await load();
    render();
    runTests();
  } catch (error) {
    app.innerHTML = `<p class="error-box">${esc(error.message)}. Is <span class="mono">python web/server.py</span> running?</p>`;
  }
})();
