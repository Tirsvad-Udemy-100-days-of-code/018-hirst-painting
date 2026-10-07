# MIL-002: Spot Painting

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This gate decides whether the program draws the finished painting as the
Business Case requires: a 10 by 10 grid of 100 dots of size 20 spaced 50 units
apart, each coloured at random from the palette, left on screen until a click,
with the turtle hidden and no trail between dots, and drawn in 30 seconds or
less.

## Deliverable

The runnable program in the single source file under `src/`, using the palette
function of the colour palette phase, together with its tests and one timed run
that shows the finished painting.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The painting has exactly 100 dots in 10 rows of 10 (SC1) | 100 dots counted in the tests and in the window | Any other count, or a missing last dot or row |
| 2 | Dot size is 20 and neighbouring centres are 50 units apart in rows and in columns (SC2) | Values match in the code, the tests and the window | Any other size or spacing |
| 3 | Every dot colour is a member of the palette (SC4) | The test passes for all 100 dots | A colour outside the palette |
| 4 | The turtle is hidden at the end, no line joins the dots, and the window stays open until a click (SC5) | All three seen in one full run | A visible turtle, a trail, or a window that closes by itself |
| 5 | One full run draws the painting in 30 seconds or less (SC6) | 30 seconds or less by stopwatch | More than 30 seconds |
| 6 | The phase code has a review record against `qc-programming-python` with verdict `Go` (SC7) | `RC-*` verdict `Go` | `Go-with-conditions` or `No-Go`, or no record |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The painting draws with the palette function that phase delivers, and starts only after it has a `Go` decision |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1: 10 by 10 grid of dots, size 20, spacing 50 | [BC-001]; criteria 1 and 2, SC1 and SC2 |
| O3: random colour from the palette for every dot | [BC-001]; criterion 3, SC4 |
| O4: painting kept on screen and presented cleanly | [BC-001]; criteria 4 and 5, SC5 and SC6 |
| O5: delivery through the framework, code reviewed against `qc-programming-python` | [BC-001]; criterion 6, SC7 |

No use case or user story applies: every task is a technical step, so the
Tasks column "Needs its own Use Case/User Story?" says `No` throughout.

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — the last day of the one-week limit of [BC-001] (2026-10-07 to 2026-10-14).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Set up the screen and the turtle | Create the screen and the turtle, switch to the 255-level red-green-blue (RGB) colour mode so the palette tuples work, hide the turtle and lift the pen. This removes the cursor and the trail from the result (O4, SC5). | No | |
| 2 | Compute the dot positions | Write a function that returns the 100 dot centres for 10 rows of 10 with 50 units between neighbours, starting from a corner chosen so the whole grid fits in the window. It draws nothing, so tests can check the count and the spacing without a window (O1, SC1, SC2). | No | |
| 3 | Draw the dots with random palette colours | Move to each position with the pen up and draw a dot of size 20 coloured by `random.choice` over the palette from the colour palette phase (O1, O3). The last dot of every row and the last row must be drawn, which the lecture names as a common mistake. | No | |
| 4 | Keep the window open until a click | End the program with `exitonclick` so the finished painting stays on screen until the user clicks (O4, SC5). | No | |
| 5 | Speed up the drawing | Set the turtle speed, or turn off screen updates until the end, so the full painting is drawn in 30 seconds or less, and time one full run (SC6). | No | |
| 6 | Add tests for the geometry and the colours | Add tests under `tests/` that check 100 positions in 10 rows of 10, a spacing of 50 in rows and in columns, and that every colour picked is in the palette (SC1, SC2, SC4). | No | |
| 7 | Review the phase code and check the painting | Check the code of this phase against `framework/qc/qc-programming-python.md` and record the result as an `RC-*`; then run the program once and check criteria 1 to 5 against it (SC7). | No | |

---

[BC-001]: ../business-case.md
