# Business Case: Hirst Painting (Spot Painting with Turtle)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Executive Summary

Day 18 of the 100 Days of Code course asks for a Python program that draws a
Hirst-style spot painting with the standard `turtle` module: a 10 by 10 grid of
round dots, each coloured at random from a palette taken from a reference image
with the `colorgram` library. The work is small and self-contained. This
business case proposes to deliver it as one script in two phases (palette, then
painting) under the software quality assurance and quality control (SQA and QC) framework, so that the exercise doubles as a
proportionate practice run of the plan-first workflow. The proposal is to
proceed.

## Methodological and Standards Foundation

- **Method:** the framework's plan-first workflow (Business Case, Stakeholder
  Analysis, Project Plan, milestones, tasks as issues, code), with analysis and
  design artifacts in the style of Larman's *Applying UML and Patterns*; only
  the artifacts the work needs are created.
- **Quality standards:** every quality criterion is tagged with an ISO/IEC
  25010:2023 characteristic. The code is reviewed against `qc-programming-python`
  before the pull request.
- **Source requirements:** the course lecture "The Hirst Painting Project
  Part 2 - Drawing the Dots" (a written summary of the lecture is the only
  source supplied; the reference image is not).

## Problem Statement

The course exercise has no working implementation in this repository yet.
Without one, the loops, the `turtle` positioning logic and the colour handling
taught in the lecture stay theory. The lecture itself names the usual
failures: a visible trail between dots, a missing last dot, white shades in
the palette that make dots invisible, and a slow, visibly drawing turtle.

## Business Opportunity

A finished and reviewed implementation gives S01 verified
practice of loops, `random`, third-party library use and `turtle` positioning,
and it shows the plan-first workflow applied to a deliberately small project,
so the effort the framework adds can be judged against the size of the work.

## Objectives

| # | Objective |
| --- | --- |
| O1 | Draw a 10 by 10 grid of 100 dots, each of size 20, with the centres of neighbouring dots 50 units apart. |
| O2 | Build the colour palette from a reference image with `colorgram`, excluding white shades. |
| O3 | Colour every dot by a random choice from that palette. |
| O4 | Keep the finished painting on screen until the user clicks, and present it cleanly: turtle hidden, no trail between dots. |
| O5 | Deliver the work through the framework: plan and issues first, then code reviewed against `qc-programming-python` (`RC-*` verdict `Go`) before the pull request. |

## Scope

### In Scope

- One Python program using the standard `turtle` module, the `random` module and the `colorgram` library.
- Extraction of the palette from one reference image, with white shades removed.
- Drawing of the 10 by 10 dot grid: dot size, spacing, row change and heading handling.
- Screen handling: `exitonclick`, hiding the turtle, pen up between dots, drawing speed.
- The framework documents the plan-first workflow requires for this work (Business Case, Stakeholder Analysis, Project Plan, milestones), and the review records for them and for the code.

### Out of Scope

- Any grid size, dot size or spacing other than the values in O1, and any user-configurable parameters.
- A graphical interface, command-line options, or saving the painting to an image file.
- Packaging or publishing the program as a library or application.
- Painting any image other than the dot grid.
- Use cases, domain models, class and database designs: the program has no persistent data and no user interaction beyond the exit click.

## Expected Benefits

### Tangible Benefits

- A working program that produces the painting described in O1 to O4.
- A reviewed codebase with a recorded review (`RC-*`) against the Python checklist.
- A traceable record from objective to milestone to issue to code.

### Intangible Benefits

- Practice with loops, random selection, library use and `turtle` positioning.
- Experience of how much framework process a small project needs.

## Strategic Alignment

The project completes one exercise of the 100 Days of Code course, which is
S01's learning goal for this repository, and it exercises the SQA and QC
framework that the repository is built on.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| SC1 | Number and layout of dots (O1) | Exactly 100 dots, in 10 rows of 10 | Count of dot calls in a run, and visual check of the window |
| SC2 | Dot size and spacing (O1) | Dot size 20; 50 units between neighbouring centres, in rows and in columns | Constants in the code, and visual check |
| SC3 | Palette content (O2) | At least 2 colours, and 0 colours with red, green and blue all at 240 or above | Print of the extracted palette checked against the threshold (value confirmed by S01) |
| SC4 | Colour choice (O3) | Every dot colour is a member of the palette | Check in code review |
| SC5 | Clean result (O4) | Turtle hidden at the end; no line drawn between dots; window stays open until a click | Visual check of one full run |
| SC6 | Run time (O4) | The full painting is drawn in 30 seconds or less | Timed run on the developer machine (value confirmed by S01) |
| SC7 | Review gate (O5) | `RC-*` for the code has verdict `Go`; the pull request closes every issue it completes | Review record and pull request description |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The reference image is not available to the project | Palette cannot be extracted from the source the lecture uses | Ask S01 for the image before the palette phase starts; if it stays unavailable, S01 decides on another image and the change is recorded in the milestone |
| `colorgram` or the `turtle` graphical toolkit (Tk) cannot be installed or does not run on the developer machine | The program cannot be run or checked | Check both in the first task of the palette phase, before any other work depends on them |
| White or near-white shades stay in the palette | Dots are invisible on the white background, so SC1 looks failed | SC3 sets an explicit threshold and is checked on the printed palette |
| Off-by-one errors: last dot of a row or the last row missing, or a trail drawn | SC1 or SC5 fails | SC1 counts the dots and SC5 checks for a trail; both are verified in the code review |
| Framework process outweighs the size of the work | Schedule slips and the exercise stops being a small one | Keep to two phases and plain tasks; no use cases or design artifacts (see Out of Scope) |
| The only named reviewer is also the author | Reviews are not independent, as the review process requires | S01 accepted a documented self-review on 2026-10-07; each review record states it |

## Assumptions

- The Product Owner (S01) is the author, the owner of every phase, and the person who accepts the work.
- Python 3 with Tk support is available on the developer machine, and `colorgram` can be installed with `pip`.
- The reference image is supplied by S01 from the course material.
- The lecture summary is a faithful statement of the required behaviour.
- The phases are completed within one week of the start date, 2026-10-07 (confirmed by S01).

## Constraints

- Only the standard `turtle` and `random` modules plus `colorgram` are used.
- The program is one source file under `src/`; its tests, if any, are under `tests/`.
- No code is written until a milestone is `Accepted`, has a review record with verdict `Go`, and the task is a row in it (plan-first gate).
- Nothing is committed, pushed or opened as a pull request unless S01 asks.
- Project documents are written in English (PO language `en`, domain `it`).

## Cost–Benefit Assessment

The assessment is qualitative on purpose: this is a learning exercise with no
revenue, so a monetary return would be invented. The cost is S01's
time; the tools are free.

| Costs | Benefits |
| --- | --- |
| S01's time for the documents, reviews and code (hours, not tracked) | Working painting program meeting SC1 to SC6 |
| No licence or infrastructure cost (Python, `turtle`, `colorgram`) | Verified practice of the lecture's techniques |
| Overhead of the framework documents relative to a one-script program | Experience of the plan-first workflow at the smallest practical size |

## Stakeholders

Roles, power and interest are in [SA-001]; they are not repeated here.

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owner of all objectives (O1 to O5); accepts the work and answers the open questions above |

## Recommendation

Proceed — the work is small, the cost is only S01's time, and every objective can be verified against an explicit target.

---

[SA-001]: ./stakeholder-analysis.md
