# Stakeholder Analysis: Hirst Painting

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [b823d1f] |

---

## Purpose

This analysis identifies who has a stake in the Hirst painting program and
classifies each stakeholder by power and interest, so that other artifacts can
cite stable stakeholder IDs for ownership, review and RACI (responsible,
accountable, consulted, informed). It follows the power/interest grid and maps
each concern to a FURPS+ attribute (functionality, usability, reliability,
performance, supportability, plus further constraints). The project is a
one-person learning exercise, so the list has a single entry on purpose; a
stakeholder is added only when someone or something actually shapes the work.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Product Owner, developer and reviewer | Tirsvad (individual) | HIGH | HIGH | Manage Closely | Finish the Day 18 exercise as a working, reviewed painting program that behaves as the lecture teaches, and learn from it without more process than the work needs |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** S01 decides scope, accepts every artifact, owns
  every phase and is the only person who works on the project, so power and
  interest are both high. S01 is consulted at every review gate.
- **Other quadrants:** no stakeholder falls in Keep Satisfied, Keep Informed or
  Monitor. The course lecture is the source of the required behaviour, but it
  is a document, not a stakeholder: it is cited as the requirements source in
  [BC-001] and takes no part in the project.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | The program draws the painting correctly and as the lecture teaches: 100 dots, right size and spacing, palette without white, random colours | Functionality |
| S01 | The result looks clean and the window stays open until a click | Usability |
| S01 | The drawing finishes quickly enough to not be tedious | Performance |
| S01 | The code is readable and passes the Python checklist | Supportability |
| S01 | The process stays proportionate to a one-script project | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat with the assistant, working-tree review | At each review gate: Business Case and Stakeholder Analysis, Project Plan, each milestone, the code | Documents in `docs/`, review records `RC-*`, dry-run output of `sync-project.sh` | Every review gate before the next step starts |
| S01 | Pull request on the git host | Once, when S01 asks for it | Pull request closing the completed issues | Code review before the pull request |

## Conflicting Interests and Mitigations

With one stakeholder there is no conflict between people; the conflicts below
are tensions inside S01's own interests, and one process conflict.

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants to practise the full framework workflow but also to finish a small exercise quickly | S01 | Two phases only, plain technical tasks, no use cases or design artifacts; the Business Case names this as a risk and as Out of Scope |
| S01 may want to change values from the lecture (dot size, spacing, thresholds) while the Business Case fixes them as targets | S01 | S01 owns the decision; a change is made through a new Version History row of [BC-001] and a re-review |
| The framework asks for a reviewer who is not the author, but S01 is the only person on the project | S01 | S01 accepted a documented self-review on 2026-10-07, recorded in the review records of [BC-001] and this document; the assistant never marks a document `Accepted` itself |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct painting, as the lecture teaches | O1, O2, O3 of [BC-001] |
| S01 | Clean, quick result | O4 of [BC-001] |
| S01 | Reviewed, proportionate delivery | O5 of [BC-001] |

Actor mapping: S01 is the only actor, as the person who runs the program and
clicks the window to close it. The program has no other user, so no use cases
are modelled; this is recorded as out of scope in [BC-001].

## Sign-Off

Pending. Sign-off is recorded by the review record (`RC-*`) of this document.
The assistant does not mark the document `Accepted`.

---

[BC-001]: ./business-case.md
[b823d1f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/b823d1f405ebac6b0198605edd9d802518529725
