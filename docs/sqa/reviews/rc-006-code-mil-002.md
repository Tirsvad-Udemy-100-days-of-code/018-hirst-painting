# Review Record: Code of MIL-002 (Spot Painting)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-006 |
| CrossReference | [MIL-002], [MIL-001], [BC-001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version (draft prepared by the assistant for S01 to confirm)<br>Verdict `Go` confirmed by S01 | [c3cfb64] |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Recorded S01's acceptance of the display requirement (Action Item 2) | [3868ea6] |

---

## Artifact Under Review

- Instance reviewed: the code of [MIL-002] tasks 1 to 6 (issues #7 to #12): the additions to `src/hirst_painting.py` (`create_pen`, `dot_positions`, `DotPen`, `draw_dots`, `main` and their constants) and the 22 new tests in `tests/test_hirst_painting.py` (40 tests in all, 18 of them from [MIL-001]). The tool configuration in `pyproject.toml` is unchanged from the version merged with [MIL-001]
- Checklist used: [QC-PY-001]
- Scope: full review of the MIL-002 additions, as they stand in the working tree of branch `mil-002-spot-painting` on 2026-10-08 (not yet committed). A change to the code before it is committed needs a delta re-review
- Language and domain: n/a (source code is a technical type, always IT Professional English)
- Language reviewer: none. S01 is also the author of record; S01 accepted a documented self-review on 2026-10-07 (see the review record of BC-001, Action Item 1)

**Status of this record:** final. The assistant read the code against every
criterion and ran the checks named below; S01 confirmed the verdict `Go` on
2026-10-08.

Evidence gathered on 2026-10-08 with Python 3.13.14, `ruff` 0.16.10, `mypy`
2.4.0 and `pytest` 9.1.1:

- `ruff format --check .` reports no changes and `ruff check .` reports "All checks passed!"
- `mypy` (strict, set in `pyproject.toml`) reports "no issues found in 2 source files"
- `pytest` reports 40 passed; the same 40 pass in reverse order and each passes when run alone; eight full runs in a row passed after the Tk start-up fix described under criterion 11
- A search of `src/` and `tests/` for `print(`, `logging`, `except`, `noqa` and `nosec` finds nothing; the only `type: ignore` is explained (criterion 3)
- A syntax-tree scan finds every function in `src/` annotated and documented, no `Any`, and no mutable or call-valued default argument. It lists one name that is also a module attribute of `builtins`, `__init__`, which is the constructor of the test fake `RecordingPen`, not a shadowed builtin
- 19 broken copies of the MIL-002 code (mutants), each run with the reference image beside it, each failed the intended tests: the pen setup (no `hideturtle`, no `penup`, no `colormode`), the geometry (spacing 49, 9 rows, 11 columns, grid not centred), the dots (size 21, colour chooser ignored, no move, no empty-palette check), `main` (no `exitonclick`, wrong palette, click wait before drawing), and the speed-up (no `tracer(0)`, `tracer(1)`, no `update`, `update` after the click wait, `update` and click wait swapped)
- A real run of `main()` on a real window drew the painting in 0.35 seconds in three runs, stayed open, and closed on a click; a captured picture shows 100 dots in a centred 10 by 10 grid with no trail and no turtle cursor

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | New names: `create_pen`, `dot_positions`, `draw_dots`, `main`; constants `GRID_ROWS`, `GRID_COLUMNS`, `DOT_SIZE`, `DOT_SPACING`; `Position` and the protocol `DotPen`; test classes `RecordingPen`, `MainRun`, `RecordingScreen`; helpers `_item_option`, `_drawn_dots`, `_other_lines`, `_write_stripes`. The `ruff` rule set `N` is on and clean |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names follow the PO terms of [BC-001] (dot, palette, painting, grid, colour). The only one-letter names are the coordinates `x` and `y`, in the tests, in scopes of a few lines. `RGB` appears in docstrings as the domain's own term |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | Both commands above are clean. The one suppression, `# type: ignore[no-untyped-call]` in `_item_option`, sits in a single helper with a comment saying that typeshed leaves `Canvas.itemcget` untyped; strict mypy would report it as unused if it stopped being needed |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | The syntax-tree scan shows every function in `src/` annotated, including the two `DotPen` methods; every test, fixture, helper and fake method in `tests/` is annotated; `ANN` rules and `mypy --strict` enforce it |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | The code has no `try` or `except`. `draw_dots` raises `ValueError` with a message for an empty palette, and its docstring says so; `test_draw_dots_raises_when_the_palette_is_empty` proves it. A missing reference image raises `FileNotFoundError` out of `main`, unhandled and visible. No exception is re-raised, so no `raise ... from` is needed |
| 6 | No mutable default arguments and no shadowed builtins | Pass | The only defaults are the integer `EXTRACTED_COLOUR_COUNT` and the function reference `random.choice`; the scan finds no mutable or call-valued default and no shadowed builtin (see the note on `__init__` above) |
| 7 | Files, locks and connections are managed with context managers | Pass | `src/` opens nothing itself. The tests do hold a resource, the hidden Tk window; it is created and destroyed by the `tk_root` and `canvas` fixtures, the form pytest gives to context-managed set-up and tear-down |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module, every public function and the `DotPen` protocol and its methods have docstrings; `ruff` rules `D` (pydocstyle, PEP 257) are on and clean. Observation, not a defect: the `...` after each docstring in `DotPen` is redundant and can be dropped |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `src/` has no `print`, no logging and no secrets; the program reads `assets/20260524_132700.jpg` and nothing else. It does not read `.env` |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists: design artifacts are out of scope in [BC-001]. The only class-like element, the protocol `DotPen`, exists so that `draw_dots` can be tested without a window. The functions trace to the tasks of [MIL-002] instead: `create_pen` to task 1, `dot_positions` to task 2, `draw_dots` to task 3, `main` to tasks 4 and 5 |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 22 new tests named `test_<behaviour>_<condition>`, covering tasks 1 to 5 and the checks of task 6 (100 positions in 10 rows of 10, spacing 50, palette membership). Order independence was run, not assumed. The tests need a display for Tk, which S01 accepted on 2026-10-08 (Action Item 2); they need no network. Review found one flaw during development, fixed before this record: starting Tk once per test failed now and then on Windows, so all tests share one hidden Tk window (`tk_root`, scope `session`) |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` strict is clean and the code contains no `Any`. The `colorgram` override from [MIL-001] still has its comment in `pyproject.toml` |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `pyproject.toml` is unchanged from the version merged with [MIL-001] and still pins `colorgram.py==1.2.0` and the dev tools `mypy==2.4.0`, `pillow==12.3.0`, `pytest==9.1.1` and `ruff==0.16.10`. The new code adds only standard-library imports (`random`, `turtle`, `tkinter`, `dataclasses`, `typing`) |

## Overall Verdict

Go — confirmed by S01 on 2026-10-08. All 12 applicable criteria of [QC-PY-001] pass,
including the 3 optional ones (8, 12, 13); criterion 10 is N-A with the reason
above. A `Go` here is Go criterion 6 of [MIL-002], the last open one. The
code satisfies criteria 1 to 5 of [MIL-002] on the evidence above. Action item
2 is closed (S01 accepted the display requirement); item 3 is a decision for S01 that does not block the verdict; only item 1 did, and it is closed.

## Action Items

| # | Action | Owner | Due |
| --- | --- | --- | --- |
| 1 | Confirm the verdict `Go` for the code of [MIL-002], or name the criterion you disagree with. **Closed 2026-10-08:** S01 confirmed `Go` | S01 | 2026-10-10 |
| 2 | Decide whether the tests may need a display: they cannot run on a machine without one, such as a build server. Accept this for the project, or ask for a change. **Closed 2026-10-08:** S01 accepted the display requirement for the project. 10 of the 33 test functions (10 of 40 test cases) need a display for Tk: the pen-setup tests, the three real-turtle drawing tests and the three `main` tests. The other 23 functions (30 cases) run anywhere. The code and the tests stay as they are | S01 | 2026-10-10 |
| 3 | Decide whether to raise the white threshold or reduce the colour count, because a few pale colours of the palette are faint on the white background (observation from the captured picture, not a criterion of [QC-PY-001]). Raising the threshold changes SC3 of [BC-001] and so needs a new row and a re-review of it; reducing the colour count does not. **Open:** a decision for S01 that does not block the verdict | S01 | 2026-10-10 |

---

[MIL-002]: ../../milestones/mil-002-painting.md
[MIL-001]: ../../milestones/mil-001-palette.md
[BC-001]: ../../business-case.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[c3cfb64]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/c3cfb6462e4b8b0a6fe37cf953a601703e352538
[3868ea6]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/3868ea6f8bb540612189782e95d19b2e4c93cbae
