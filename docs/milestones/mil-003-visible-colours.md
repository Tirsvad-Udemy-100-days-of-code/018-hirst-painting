# MIL-003: Visible Colours

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [188b2e9] |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Renamed task 6 so that its issue title is unique across the milestones (issue #27) | pending |

---

## Purpose

This gate decides whether the palette keeps only colours that stand out from
the white background, so that every dot of the painting is clearly visible
(objective O6 of the Business Case). The palette must contain no colour whose
contrast with white is below 2.0, and the painting must still meet every
earlier criterion.

## Deliverable

A contrast measure and a faint-colour filter in the program's source file under
`src/`, applied when the palette is extracted, together with their tests and
one real run that shows the painting drawn from the filtered palette.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The contrast measure gives 1.0 for white and 21.0 for black, and the filter keeps a colour only when its contrast with white is 2.0 or more (SC8) | The tests of the measure and the filter pass | Any of those tests fails |
| 2 | The palette of the reference image has no colour with a contrast below 2.0, still has at least 2 colours, and still has no white shade (SC8, SC3) | The printed palette with the contrast of every colour meets all three | A colour below 2.0, fewer than 2 colours, or a white shade |
| 3 | The earlier behaviour is unchanged: all tests pass, and `ruff` and `mypy --strict` are clean | All tests pass and both tools report no problem | A failing test or a reported problem |
| 4 | A real run still draws the painting in 30 seconds or less, with 100 dots, no trail and no turtle, and the window stays open until a click (SC1, SC5, SC6) | A timed run and a captured picture show all of it, and every dot is clearly visible | Any of them fails |
| 5 | The phase code has a review record against `qc-programming-python` with verdict `Go` (SC7) | `RC-*` verdict `Go` | `Go-with-conditions` or `No-Go`, or no record |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The filter is applied inside the palette function that phase delivered, beside its white-shade filter |
| MIL-002 | The painting is drawn again with the filtered palette, and its tests must keep passing |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O6: every dot clearly visible, contrast with white of 2.0 or more | [BC-001]; criteria 1, 2 and 4, SC8 |
| O2: palette without white shades | [BC-001]; criterion 2, SC3 (still holds) |
| O1, O4: the painting and its clean presentation | [BC-001]; criteria 3 and 4, SC1, SC5 and SC6 |
| O5: delivery through the framework, code reviewed against `qc-programming-python` | [BC-001]; criterion 5, SC7 |

No use case or user story applies: every task is a technical step, so the
Tasks column "Needs its own Use Case/User Story?" says `No` throughout.

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-10 — inside the one-week limit of [BC-001] (2026-10-07 to 2026-10-14), and leaves four days of slack.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the contrast measure | Add a function that returns the contrast ratio of a colour against white, as the Web Content Accessibility Guidelines (WCAG) 2.x define it from relative luminance: 1.0 for white and 21.0 for black. It is the measure that objective O6 and criterion SC8 of the Business Case rest on. | No | |
| 2 | Add the faint-colour filter | Add a named constant for the limit, 2.0, and a function that drops every colour whose contrast with white is below it, keeping the order of the rest. It sits beside the white-shade filter, which stays as it is, so SC3 keeps its own check. | No | |
| 3 | Add tests for the measure and the filter | Add tests under `tests/` with known values (white 1.0, black 21.0, a mid grey) and with the boundary: a colour just below 2.0 is dropped and one just above is kept. They pin the limit before the real image is involved, as the white-shade tests do for 240. | No | |
| 4 | Apply the filter when the palette is extracted | Make `extract_palette` apply the faint-colour filter after the white-shade filter, update its tests, and add one that checks the palette of the reference image: no colour below 2.0 and at least 2 colours. Print the palette with each contrast; the measurement on 2026-10-08 predicts 22 colours. | No | |
| 5 | Check the painting again with a real run | Run `main` on a real window, time it and capture the picture: 100 dots in 10 rows of 10, no trail, no turtle cursor, the window open until a click, and every dot clearly visible on the white background. This rechecks SC1 to SC8 together. | No | |
| 6 | Review the visible-colours code against qc-programming-python | Check the code of this phase against `framework/qc/qc-programming-python.md` and record the result as an `RC-*`; a `Go` verdict is Go criterion 5 (SC7). | No | |

---

[BC-001]: ../business-case.md
[188b2e9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/188b2e97000d761802d4384c160598f785860a28
