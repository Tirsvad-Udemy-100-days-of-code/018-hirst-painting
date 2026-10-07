# Project Plan: Hirst Painting

## Metadata
| Key | Value |
| --- | --- |
| ID | PP-001 |
| CrossReference | [BC-001], [SA-001], [MIL-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [b823d1f] |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Recorded the Go decisions of MIL-001 and MIL-002<br>Closed the reference-image open issue | [a6b17d3] |

---

## Purpose

This plan schedules the two phases of the Hirst painting project, the colour
palette and the spot painting, inside the one-week limit that [BC-001] sets
(2026-10-07 to 2026-10-14). Each phase is a gateway with its own milestone
document, and each gateway ends with a Go/No-Go decision by S01.

## Planning Assumptions

- Week 1 starts 2026-10-07; the plan ends by 2026-10-14, per the Business Case assumption confirmed by S01.
- The baseline documents ([BC-001], [SA-001] and their review records) are finished on 2026-10-07, before the first phase starts.
- Phase length: two to five days, because the work is one small script. The palette phase is shorter because it is the smaller of the two.
- S01 owns both phases and takes both Go/No-Go decisions; S01 is the only stakeholder in [SA-001], so communication follows the review gates in that document.
- No user stories exist: the program has no user interaction beyond the exit click, so the Stories column is empty.

## Gateway Schedule

| Gateway | Document | Window | Decision date | Owner | Stories | Main deliverable | Milestone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Colour palette | [MIL-001] | 2026-10-07 to 2026-10-09 | 2026-10-09 | S01 | none | Palette function that returns the reference image's colours without white shades | [MIL-001 milestone] |
| Spot painting | [MIL-002] | 2026-10-10 to 2026-10-14 | 2026-10-14 | S01 | none | Program that draws the 10 by 10 painting and meets SC1 to SC7 of [BC-001] | [MIL-002 milestone] |

```plantuml
@startgantt
Project starts 2026-10-07
[Colour palette] starts 2026-10-07 and ends 2026-10-09
[Colour palette Go/No-Go] happens 2026-10-09
[Spot painting] starts 2026-10-10 and ends 2026-10-14
[Spot painting Go/No-Go] happens 2026-10-14
@endgantt
```

## Scope Coverage

| Business Case scope item | Gateway |
| --- | --- |
| One Python program using `turtle`, `random` and `colorgram` | [MIL-001] (`colorgram` part), [MIL-002] (`turtle` and `random` part) |
| Palette extracted from one reference image, white shades removed | [MIL-001] |
| Drawing the 10 by 10 dot grid: size, spacing, row change, heading | [MIL-002] |
| Screen handling: `exitonclick`, hidden turtle, pen up, drawing speed | [MIL-002] |
| Framework documents and review records for the plan-first workflow | Finished before the first gateway ([BC-001], [SA-001], this plan, [MIL-001], [MIL-002] and their reviews); the review of each phase's code is a task in that phase |

## Dependencies

```
Baseline documents → [MIL-001] Colour palette → [MIL-002] Spot painting
```

[MIL-002] needs the palette function from [MIL-001]. A No-Go on [MIL-001] moves
the start of [MIL-002] by the days needed to rework and re-review; the
one-week limit then has no slack, so S01 decides whether to extend it.

## Plan Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The reference image is not supplied before the palette phase starts | [MIL-001] cannot start its extraction task; the window of two to three days is lost | The tasks that do not need the image (toolchain check, white filter and its tests) come first; S01 decides on another image if this one stays unavailable |
| A No-Go on the palette phase | [MIL-002] starts late and the one-week limit is missed | The palette phase is the smaller one and ends 2026-10-09, leaving five days for the painting phase |
| Review effort is large compared with the code | Time goes to documents instead of the program | Two phases, plain tasks, no use cases or design artifacts, as set out in [BC-001] |
| The Project Plan has no quality checklist | The plan is accepted on S01's judgement alone | S01 checks the plan against the one-week limit of [BC-001] and the Go/No-Go criteria of both milestones |

## Open Issues

- **Reference image:** resolved. S01 supplied `assets/20260524_132700.jpg` on 2026-10-07, which completed task 4 of [MIL-001].
- **Project Plan review:** the Project Plan has no quality checklist yet, so it is `Accepted` when S01 says so in chat (done on 2026-10-07, and again on 2026-10-08 for the gateway decisions); no review record is written for it.
- **Milestone links:** `sync-project.sh --apply` ran on 2026-10-07 and created the two Milestones and issues #1 to #13 on the git host; the Milestone column links to them.

## Gateway Decisions

The Go/No-Go decision of each gateway, taken by its owner (S01) in chat and recorded here by the assistant. The Decision date in the Gateway Schedule is the planned date; the date below is the actual one.

| Gateway | Document | Decision | Decided by | Decision date | Planned date | Basis |
| --- | --- | --- | --- | --- | --- | --- |
| Colour palette | [MIL-001] | Go | S01 | 2026-10-08 | 2026-10-09 | All five Go criteria met: imports and window, 30 colours, no white shade, 18 tests passing, code review RC-005 with verdict `Go`. Pull request [PR 14] merged; Milestone closed on the git host |
| Spot painting | [MIL-002] | Go | S01 | 2026-10-08 | 2026-10-14 | All six Go criteria met: 100 dots in 10 rows of 10, size 20 and 50 apart, colours from the palette, clean result with the window open until a click, drawn in 0.35 seconds, code review RC-006 with verdict `Go`. Pull request [PR 16] merged; Milestone closed on the git host |

Both decisions came before the planned dates because every Go criterion was already met. The two open decisions on RC-006 (the display requirement of the tests and the pale palette colours) did not block either one.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-001]: ./milestones/mil-001-palette.md
[MIL-002]: ./milestones/mil-002-painting.md
[MIL-001 milestone]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/milestone/68
[MIL-002 milestone]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/milestone/69
[PR 14]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/pulls/14
[PR 16]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/pulls/16
[b823d1f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/b823d1f405ebac6b0198605edd9d802518529725
[a6b17d3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/a6b17d30bc0778b7f80c57bfd22a505df5fe9ee1
