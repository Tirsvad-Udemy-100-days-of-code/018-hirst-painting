# MIL-001: Colour Palette

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This gate decides whether the colour palette is usable, so that the painting
phase can build on it. The palette must come from the reference image through
`colorgram`, must contain no white shades, and the toolchain it depends on
(`colorgram` and the `turtle` graphical toolkit) must work on the developer
machine.

## Deliverable

A palette function in the program's source file under `src/` that reads the
reference image with `colorgram`, drops white shades and returns the remaining
colours as RGB tuples, together with the tests that check it and the printed
palette of the real image.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `import colorgram` and `import turtle` succeed and a `turtle` window opens on the developer machine | Both imports succeed and the window opens | An import fails or no window opens |
| 2 | The palette of the reference image has at least 2 colours (SC3) | 2 or more colours printed | 0 or 1 colour |
| 3 | The palette has no colour with red, green and blue all at 240 or above (SC3) | 0 such colours in the printed palette | 1 or more such colours |
| 4 | The tests of the white-shade filter and of the palette pass | All tests pass | Any test fails |
| 5 | The phase code has a review record against `qc-programming-python` with verdict `Go` (SC7) | `RC-*` verdict `Go` | `Go-with-conditions` or `No-Go`, or no record |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | The baseline documents are `Accepted`; this is the first gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2: palette from a reference image with `colorgram`, without white shades | [BC-001]; criteria 1 to 4 and SC3 |
| O5: delivery through the framework, code reviewed against `qc-programming-python` | [BC-001]; criterion 5 and SC7 |

No use case or user story applies: every task is a technical step, so the
Tasks column "Needs its own Use Case/User Story?" says `No` throughout.

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-09 — inside the one-week limit of [BC-001] (2026-10-07 to 2026-10-14), and leaves five days for the painting phase.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Check the toolchain | Confirm that Python 3 with Tk (the graphical toolkit behind `turtle`) runs `import turtle` and opens a window, install `colorgram` with `pip`, and record the versions. The Business Case lists a missing toolchain as a risk, so this comes before any other work depends on it. | No | |
| 2 | Write the white-shade filter | Write a function that drops every colour whose red, green and blue are all at or above 240; the threshold is a named constant (SC3 of the Business Case). It needs no image, so it can be written and tested first. | No | |
| 3 | Add tests for the white-shade filter | Add tests under `tests/` that feed the filter synthetic colours (pure white, near-white, an ordinary colour) and check which are kept. They pin down the threshold before the real image is involved. | No | |
| 4 | Get the reference image into the project | S01 supplies the reference image the lecture uses; store it in the repository and note its path. Without it the palette cannot be extracted, and the location is an open issue of the Project Plan. | No | |
| 5 | Write the palette extraction and check the palette | Write a function that reads the image with `colorgram`, turns each extracted colour into a red-green-blue (RGB) tuple, applies the filter and returns the list (O2). Print the palette of the real image and check it against SC3: at least 2 colours and no white shade. The painting phase imports this function. | No | |
| 6 | Review the phase code against qc-programming-python | Check the code of this phase against `framework/qc/qc-programming-python.md` and record the result as an `RC-*`; a `Go` verdict is Go criterion 5 (SC7). | No | |

---

[BC-001]: ../business-case.md
