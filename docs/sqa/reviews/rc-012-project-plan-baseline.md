# Review Record: PP-001 against QC-PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record; verdict Go (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / education
- Language reviewer: none (the stand-in reads English and knows the education domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions give the start and end dates (2026-10-07 to 2026-10-14, and 2026-11-15 to 2026-11-22 for MIL-004) and cite BC-001. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | The Gateway Schedule lists MIL-001 to MIL-003 and MIL-004 once each with document, decision date and owner; every document exists and no gateway is missing from the plan or from the milestones. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Every decision date lies in its window and equals the Target Date of its milestone (2026-11-22 for MIL-004; 2026-10-09, 2026-10-14 and 2026-10-10 for MIL-001 to MIL-003). |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every In Scope item of BC-001 to a gateway; the baseline item maps to MIL-004. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | The chain MIL-001 to MIL-004 is acyclic and in schedule order, as the Dependencies section says. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies state that a No-Go on a gateway moves the later dates or leaves the accepted program as it is, and that S01 decides. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 and reviewer S01 (stand-in for MIL-004) are stakeholder IDs of SA-001; no governance document exists, so there is no RACI to contradict. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Each planning assumption names its source or is a decision of S01; the move of the end date is recorded with its reason (the agreed minimum quality baseline). |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks give impact and mitigation for each risk; the CI risk traces to success criterion SC9 of BC-001. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues lists the open points; the stale remark that the plan has no quality checklist was updated, so none contradicts the rest of the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | The main deliverable of each gateway is the first-named deliverable of its milestone; for MIL-004 it names the same items as its Deliverable section. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | The Stories column says `none` for every gateway; the plan states that no user stories exist. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | The Gantt bars use the dates of the schedule table; the dependency view agrees with the order. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | MIL-001 to MIL-003 link milestones 68, 69 and 74 of the git host; MIL-004 links its milestone after the sync. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | PP-001 is the only Project Plan; its Version History records each change in its own row and only the latest row is Accepted. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table has `Language | en` and `Domain | education`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `education` is a row of the domain list of docs/artifact-registry.md. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only file names, commands and IDs are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register `IT Executive English` for this type; the text is short, plain and written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | No dictionary (DICT) exists in this project and none is in scope. The terms project, gateway, milestone, dot, palette and colour are used in one meaning each. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | The `Domain` row changed from `it` to `education` in this version (the language `en` is unchanged). The Version History row records the change and this review covers it. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the education domain and checked the terms; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out where they are first used (SQA, QC, CI, FURPS+, WCAG, API) or are established names (README, RGB). |

## Overall Verdict

Go — every Mandatory criterion of QC-PP-001 and QC-LANG-001 passes after the edits of this change; the document is Accepted. Review of the whole document after the edits of this change.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No open action | S01 | 2026-11-22 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
