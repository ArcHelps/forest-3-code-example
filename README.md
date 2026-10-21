# FOREST-3 code-link example

This repository contains illustrative sample code for Arc's FOREST-3 demo.
It is not actual FOREST-3 flight software, a complete implementation of its
requirements, or qualification/verification evidence. There is no affiliation
with the real mission or its software suppliers.

Comments associate example functions and tests with the demo's canonical Arc
item identifiers. The Arc CLI's deterministic scanner finds those markers and
produces a schema-versioned report of file paths and line numbers; source code
is not uploaded to Arc. A code link records an association, not proof that a
requirement is satisfied or a test has passed.

A saved report from this repository's exact commit is preloaded when you create
the FOREST-3 example in Arc. Every one of the 269 demo Items has a file-and-line link. The `examples/`
folder contains the illustrative system definitions, requirement specifications,
property values, risk scenarios, test cases and test plans. Processing outputs
and selected software Items also link to the sample functions and tests.
No account connection, token or CI configuration is needed for the demo. This
repository has no live sync workflow; new commits do not update existing demos.

Run the small illustrative tests from the repository root:

```sh
python -m unittest discover -s tests -v
```
