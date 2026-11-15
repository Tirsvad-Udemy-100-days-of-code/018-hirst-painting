# Traceability Matrix: Hirst Painting

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; created with the review records of the baseline (autonomous, not independent) | [1b1a439] |

---

## Purpose

Tracks backward and forward links between the artifact instances of Hirst Painting so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-010] |
| [SA-001] | Stakeholder Analysis | en | education | [BC-001] | [PP-001] | [RC-011] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-012] |
| [MIL-001] | Milestone / Gateway | en | education | [BC-001], [PP-001] | [MIL-002] | [RC-013] |
| [MIL-002] | Milestone / Gateway | en | education | [BC-001], [MIL-001] | [MIL-003] | [RC-014] |
| [MIL-003] | Milestone / Gateway | en | education | [BC-001], [MIL-002] | [MIL-004] | [RC-015] |
| [MIL-004] | Milestone / Gateway | en | education | [BC-001], [PP-001], [MIL-003] | - | [RC-016] |
| Wiki | Wiki | en, da, ms | education | [BC-001] | - | [RC-017] |
| Python code of MIL-001 (`src/hirst_painting.py`, `tests/test_hirst_painting.py`) | Python Source Code (PY) | - | - | [MIL-001] | - | [RC-005] |
| Python code of MIL-002 (`src/hirst_painting.py`, `tests/test_hirst_painting.py`) | Python Source Code (PY) | - | - | [MIL-002] | - | [RC-006] |
| Python code of MIL-003 (`src/hirst_painting.py`, `tests/test_hirst_painting.py`) | Python Source Code (PY) | - | - | [MIL-003] | - | [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-001] (criteria on the palette), [MIL-002] (criteria on the dots and colours) | - | - | Covered |
| CN-002 | [MIL-002] (criteria on the clean result and the open window) | - | - | Covered |
| CN-003 | [MIL-002] (criterion on the drawing time) | - | - | Covered |
| CN-004 | [MIL-001] (code review), [MIL-002] (code review), [MIL-003] (criterion 5) | - | - | Covered |
| CN-005 | [PP-001] (few gateways, plain tasks, no use cases) | - | - | Covered |
| CN-006 | [MIL-004] (criteria 1, 3, 4 and 5) | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

- No view, design or test-plan artifact exists (the scope excludes them), so the concerns are covered by the Go/No-Go criteria of the milestones. In Upstream, `-` means foundational; in Downstream, `-` means nothing is built on it yet.
- The source code is reviewed in [RC-005], [RC-006] and [RC-009] and not again in [MIL-004]. These records and this matrix have no QC checklist for themselves and are not reviewed.
- The domain of every artifact is `education` since [MIL-004]; the earlier review records [RC-001] to [RC-009] state the former domain `it` as it was at the time.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-palette.md
[MIL-002]: ../milestones/mil-002-painting.md
[MIL-003]: ../milestones/mil-003-visible-colours.md
[MIL-004]: ../milestones/mil-004-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-005]: ./reviews/rc-005-code-mil-001.md
[RC-006]: ./reviews/rc-006-code-mil-002.md
[RC-009]: ./reviews/rc-009-code-mil-003.md
[RC-010]: ./reviews/rc-010-business-case-baseline.md
[RC-011]: ./reviews/rc-011-stakeholder-analysis-baseline.md
[RC-012]: ./reviews/rc-012-project-plan-baseline.md
[RC-013]: ./reviews/rc-013-milestone-001-baseline.md
[RC-014]: ./reviews/rc-014-milestone-002-baseline.md
[RC-015]: ./reviews/rc-015-milestone-003-baseline.md
[RC-016]: ./reviews/rc-016-milestone-004.md
[RC-017]: ./reviews/rc-017-wiki.md
[1b1a439]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/1b1a439da2fc5e409ff12782214f07a0aab8b168
