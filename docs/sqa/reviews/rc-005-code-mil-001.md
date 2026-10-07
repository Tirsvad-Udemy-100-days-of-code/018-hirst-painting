# Review Record: Code of MIL-001 (Colour Palette)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-005 |
| CrossReference | [MIL-001], [BC-001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version (draft prepared by the assistant for S01 to confirm)<br>Verdict `Go` confirmed by S01 | [b7119ef] |

---

## Artifact Under Review

- Instance reviewed: the code of [MIL-001] tasks 2, 3 and 5 (issues #2, #3 and #5): `src/hirst_painting.py` (`is_white_shade`, `remove_white_shades`, `extract_palette`), `tests/test_hirst_painting.py` (18 tests), and the tool configuration in `pyproject.toml`
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (source code is a technical type, always IT Professional English)
- Language reviewer: none. S01 is also the author of record; S01 accepted a documented self-review on 2026-10-07 (see the review record of BC-001, Action Item 1)

**Status of this record:** final. The assistant read the code against every
criterion and ran the checks named below; S01 confirmed the verdict `Go` on
2026-10-07.

Evidence gathered on 2026-10-07 with Python 3.13.14, `ruff` 0.16.10, `mypy`
2.4.0 and `pytest` 9.1.1:

- `ruff format --check .` reports no changes and `ruff check .` reports "All checks passed!"
- `mypy` (strict, set in `pyproject.toml`) reports "no issues found in 2 source files"
- `pytest` reports 18 passed; the same 18 pass in reverse order and each passes when run alone
- A search of `src/` and `tests/` for `print(`, `logging`, `except`, `noqa`, `type: ignore` and `nosec` finds nothing
- An abstract-syntax-tree scan of both files finds no shadowed builtin

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Module `hirst_painting`; functions `is_white_shade`, `remove_white_shades`, `extract_palette`; constants `WHITE_THRESHOLD`, `EXTRACTED_COLOUR_COUNT`, `REFERENCE_IMAGE_PATH`, `STRIPE_WIDTH`; type alias `Colour`; private test helper `_write_stripes`; `ruff` rule set `N` (pep8-naming) is on and clean |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names follow the PO terms of [BC-001] (colour, palette, white shade). No single-letter names; `rgb.r`, `rgb.g` and `rgb.b` are the `colorgram` library's own attribute names. The code spells "colour" as the documents do, while library calls keep their own spelling |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | Both commands above are clean. There is no inline suppression. The only configured exemption is `D103` for `tests/*`, and `pyproject.toml` explains it (test names state the behaviour) |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function in `src/` and `tests/`, including each test and the helper, is annotated; the `ANN` rules and `mypy --strict` enforce it |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | The code has no `try` or `except`. A missing image raises `FileNotFoundError` from the library and propagates; `test_extract_palette_raises_when_image_is_missing` proves it. The code raises no exception of its own, so no `raise ... from` is needed |
| 6 | No mutable default arguments and no shadowed builtins | Pass | The only default argument is the integer constant `EXTRACTED_COLOUR_COUNT`; the syntax-tree scan finds no shadowed builtin |
| 7 | Files, locks and connections are managed with context managers | N-A | The code opens no file itself: `colorgram` opens the image from its path. After `extract_palette` the file can be deleted on Windows, which shows that no handle stays open |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module docstring and a docstring on each public function; `extract_palette` also states its `FileNotFoundError`. `ruff` rules `D` (pydocstyle, PEP 257) are on and clean |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `src/` has no `print`, no logging and no secrets. The program does not read `.env` |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists: design artifacts are out of scope in [BC-001] and the code has no classes. The functions trace to tasks 2, 3 and 5 of [MIL-001] instead |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 18 tests named `test_<behaviour>_<condition>`; they use `tmp_path` and the repository's own image, and need no network. Order independence was run, not assumed (reverse order and each test alone). Review found one test name that said "at most" while asserting an exact count; it was renamed to `test_extract_palette_returns_requested_count_when_image_has_more_colours` before this record |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` strict is clean. `colorgram` ships no type information, so `pyproject.toml` sets `ignore_missing_imports` for that one module with a comment saying so; its values are converted to `Colour` at the boundary in `extract_palette` |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `pyproject.toml` pins `colorgram.py==1.2.0` and, in the `dev` group, `mypy==2.4.0`, `pillow==12.3.0`, `pytest==9.1.1` and `ruff==0.16.10`. Each is used: `pillow` by the tests, the others by the code and tools. There is no lock file; the pins are in `pyproject.toml` |

## Overall Verdict

Go — confirmed by S01 on 2026-10-07. All 11 applicable criteria of [QC-PY-001] pass,
including the 3 optional ones (8, 12, 13); criteria 7 and 10 are N-A with the
reasons above. The one defect found in review (a misleading test name) was
fixed before the record. A `Go` here is Go criterion 5 of [MIL-001], the last
open one.

## Action Items

| # | Action | Owner | Due |
| --- | --- | --- | --- |
| 1 | Confirm the verdict `Go` for the code of [MIL-001], or name the criterion you disagree with. **Closed 2026-10-07:** S01 confirmed `Go` | S01 | 2026-10-09 |

---

[MIL-001]: ../../milestones/mil-001-palette.md
[BC-001]: ../../business-case.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[b7119ef]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/b7119ef907b1ae56d7aa231a460aeab8fa2f2e11
