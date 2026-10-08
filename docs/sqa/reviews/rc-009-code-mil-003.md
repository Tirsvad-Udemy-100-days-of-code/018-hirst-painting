# Review Record: Code of MIL-003 (Visible Colours)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-003], [MIL-001], [MIL-002], [BC-001], [QC-PY-001], [RC-006] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version (draft prepared by the assistant for S01 to confirm)<br>Verdict `Go` confirmed by S01 | pending |

---

## Artifact Under Review

- Instance reviewed: the code of [MIL-003] tasks 1 to 5 (issues #22 to #26): the additions to `src/hirst_painting.py` (the constants of the WCAG formula and `MINIMUM_CONTRAST`, `_linearise`, `relative_luminance`, `contrast_with_white`, `is_faint_colour`, `remove_faint_colours`, and the change to `extract_palette`) and the 37 new test cases in `tests/test_hirst_painting.py` (77 in all, 40 of them from [MIL-001] and [MIL-002]). `pyproject.toml` is unchanged from `origin/main`
- Checklist used: [QC-PY-001]
- Scope: full review of the MIL-003 additions, as they stand in the working tree of branch `mil-003-visible-colours` on 2026-10-08 (not yet committed). A change to the code before it is committed needs a delta re-review. Task 6 of [MIL-003] (issue #27) is this review
- Language and domain: n/a (source code is a technical type, always IT Professional English)
- Language reviewer: none. S01 is also the author of record; S01 accepted a documented self-review on 2026-10-07 (see the review record of BC-001, Action Item 1)

**Status of this record:** final. The assistant read the code against every
criterion and ran the checks named below; S01 confirmed the verdict `Go` on
2026-10-08.

Evidence gathered on 2026-10-08 with Python 3.13.14, `ruff` 0.16.10, `mypy`
2.4.0 and `pytest` 9.1.1:

- The three tool commands, exactly as the CI workflow runs them, are clean: `ruff check src tests` reports "All checks passed!", `ruff format --check src tests` reports no change, and `mypy src tests` (strict, set in `pyproject.toml`) reports "no issues found in 2 source files"
- `pytest` reports 77 passed; the same 77 pass in reverse order and each of the 77 passes when run alone
- A search of `src/` and `tests/` for `print(`, `logging`, `except`, `noqa` and `nosec` finds nothing; the only `type: ignore` is the explained one from [RC-006]
- A syntax-tree scan finds every new function annotated and documented, no `Any`, no mutable or call-valued default argument, and no shadowed builtin
- 23 broken copies of the MIL-003 code (mutants), each run with the reference image beside it. 22 failed the intended tests: ten of the contrast formula (each constant of the WCAG definition, the weights, the direction of the ratio), nine of the filter (the limit moved to 1.9, 2.1 and, by only 0.0001, to 1.9998 and 2.0001; the predicate inverted; the filter keeping the faint colours, losing the order, dropping nothing, or using the white-shade rule), and three of `extract_palette` (filter not applied, white filter applied twice, only 20 colours extracted). One passed: removing the white-shade call from `extract_palette`, which gives the same palette because every white shade is also a faint colour (see Action Item 2). A tenth filter mutant, `<` changed to `<=`, differs only for a colour whose contrast is exactly 2.0; none was found among about 636,000 colours scanned, so it was reasoned about, not run
- Three real runs of `main()` on a real window each drew the painting in 0.35 seconds (SC6), the window stayed open at 1, 2 and 3 seconds with no click, and the click closed it. A captured picture of the window, analysed pixel by pixel without project code, shows 100 marks of one size and none of another (no trail, no turtle cursor), 10 rows of 10 with 50 pixels between neighbours, 22 distinct flat colours all in the palette, no white shade, and a lowest contrast with white of 2.56 against the limit of 2.0 (SC8). This is the evidence for criteria 2 and 4 of [MIL-003]

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | New functions `relative_luminance`, `contrast_with_white`, `is_faint_colour`, `remove_faint_colours`; internal `_linearise` with its leading underscore; constants `MINIMUM_CONTRAST`, `CHANNEL_MAXIMUM`, `LINEAR_BREAK`, `LINEAR_SLOPE`, `CURVE_OFFSET`, `CURVE_SCALE`, `CURVE_EXPONENT`, `LUMINANCE_WEIGHTS`, `WHITE_LUMINANCE`, `CONTRAST_OFFSET`. The `ruff` rule set `N` is on and clean |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | *Faint colour*, *contrast* and *palette* are the terms of [BC-001] as revised. The constants of the formula are named after their part in it (a break, a slope, an offset, a scale, an exponent) and the comment above them cites the WCAG definition and explains each. There are no single-letter names in the new code |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | The commands above are clean and the MIL-003 change adds no suppression. The one `type: ignore[no-untyped-call]` was reviewed in [RC-006] and still carries its comment |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | The scan shows every new function annotated and every test annotated; the `ANN` rules and `mypy --strict` enforce it |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | The new code has no `try` or `except` and raises nothing. It cannot fail for a valid `Colour`; an out-of-range channel is a caller error that the type does not rule out, and is not handled, which is consistent with the rest of the module |
| 6 | No mutable default arguments and no shadowed builtins | Pass | The scan finds no mutable or call-valued default and no shadowed builtin |
| 7 | Files, locks and connections are managed with context managers | N-A | The new code opens nothing. The tests that read the reference image go through `extract_palette`, and the Tk fixtures from [RC-006] are unchanged |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every new function has a docstring, including the internal `_linearise`; `contrast_with_white` states its two reference values. `ruff` rules `D` (pydocstyle, PEP 257) are on and clean |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `src/` has no `print`, no logging and no secrets |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists: design artifacts are out of scope in [BC-001]. The functions trace to the tasks of [MIL-003] instead: `relative_luminance` and `contrast_with_white` to task 1, `MINIMUM_CONTRAST`, `is_faint_colour` and `remove_faint_colours` to task 2, `extract_palette` to task 4 |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 37 new test cases named `test_<behaviour>_<condition>`, written before the code and seen to fail for the right reason. They cover the formula (known values from the WCAG definition and published figures, both sides of the break of the curve), the filter (the boundary pinned to about 0.0001 with real colours found by search, and the palette colours of [BC-001]), the palette (synthetic and real image) and the property that every white shade is a faint colour. Order independence was run, not assumed. The 10 cases that need a display for Tk are unchanged and accepted in [RC-006]; the CI runs them under `xvfb` |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy` strict is clean and the code contains no `Any`. Strict mode caught one real issue during development: `float ** float` is typed as `Any`, so `_linearise` uses `math.pow`, which is typed as `float`, instead of a suppression |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `pyproject.toml` is identical to `origin/main`. The new code adds one standard-library import, `math` |

## Overall Verdict

Go — confirmed by S01 on 2026-10-08. All 11 applicable criteria of [QC-PY-001] pass,
including the 3 optional ones (8, 12, 13); criteria 7 and 10 are N-A with the
reasons above. A `Go` here is Go criterion 5 of [MIL-003], the last open one:
criteria 1 to 4 are met on the evidence above. Action item 2 is a decision for
S01 and does not block the verdict; only item 1 did, and it is closed.

## Action Items

| # | Action | Owner | Due |
| --- | --- | --- | --- |
| 1 | Confirm the verdict `Go` for the code of [MIL-003], or name the criterion you disagree with. **Closed 2026-10-08:** S01 confirmed `Go` | S01 | 2026-10-10 |
| 2 | Decide whether `extract_palette` keeps its call to `remove_white_shades`. It changes nothing now, because every white shade is also a faint colour, and the one surviving mutant shows it. Keeping it leaves the function and its tests used by the program and keeps SC3's own step visible, as the code comment says; removing it would leave `is_white_shade` and `remove_white_shades` used only by tests. Both are defensible; the code keeps the call. **Open:** a decision for S01 that does not block the verdict | S01 | 2026-10-10 |

---

[MIL-003]: ../../milestones/mil-003-visible-colours.md
[MIL-001]: ../../milestones/mil-001-palette.md
[MIL-002]: ../../milestones/mil-002-painting.md
[BC-001]: ../../business-case.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[RC-006]: ./rc-006-code-mil-002.md
