# MIL-004: Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [PP-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | [1b1a439] |

---

## Purpose

This gate decides whether Hirst Painting has the baseline of the framework: the adopted framework release, a wiki in English, Danish and Malay, complete licence metadata and reviewed documents, merged to the default branch with a green build.

## Deliverable

A merged pull request that holds: the updated Business Case, Stakeholder Analysis, Project Plan and milestones with their review records; the traceability matrix; the wiki in English, Danish and Malay; `pyproject.toml` with complete licence metadata; and the framework release adopted by the project. The program and its tests do not change.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, SA-001, PP-001, MIL-001 to MIL-003 and MIL-004 each have an `Accepted` Version History row and a review record with the verdict `Go` | All of them | Any missing or `Go-with-conditions` |
| 2 | `python -m pytest` runs on a machine with a display | Exit code 0 | Any failure |
| 3 | `docs/wiki/` has `_Sidebar.md` and the pages Home, Getting-Started and Project-Documents in en, da and ms | 9 pages and the sidebar | A page or language missing |
| 4 | `framework/scripts/check-readme.sh` and `framework/scripts/check-languages.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` sets `license` and `license-files` | Both set | Either missing |
| 6 | All CI (continuous integration) checks of the pull request | Green | Red or pending |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | Documents and baselines the finished program |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 to O6 | Criterion 2 (the behaviour is unchanged and its tests pass) |
| O7 | Criteria 1, 3, 4 and 5 (documents, wiki, README and licence) |
| SC9 | Criteria 1 and 6 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-22: one week after the start, as the Business Case assumption requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Track the `framework/` submodule and `.gitmodules`, install the skills, hooks and `.editorconfig`, add a `.gitignore`, and track `.env.example` so the project follows the same rules as the other projects of the portfolio. | No | O7 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case and Project Plan, add concern IDs to the Stakeholder Analysis, create the traceability matrix and review each changed document against its QC checklist, so the plan-first gate is met. | No | O7 |
| 3 | Publish the wiki in English, Danish and Malay | Write the pages Home, Getting-Started and Project-Documents and the sidebar in `docs/wiki/`, so a visitor can learn what the exercise is and how to run it in their own language. | No | O7 |
| 4 | Add licence metadata to pyproject.toml | Set `license`, `license-files`, the authors and the project URLs so package tools can read the licence. | No | O7 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[1b1a439]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/1b1a439da2fc5e409ff12782214f07a0aab8b168
