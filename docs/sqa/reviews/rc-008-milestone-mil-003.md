# Review Record: Milestone MIL-003

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [MIL-003], [BC-001], [QC-MIL-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version (draft prepared by the assistant for S01 to confirm)<br>Terms confirmed by S01, verdict `Go` | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-003]
- Checklist used: [QC-MIL-001], together with [QC-LANG-001] because the milestone is written in the PO language
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none. S01 reads English and knows the IT domain. S01 is also the author; S01 accepted a documented self-review on 2026-10-07 (see the review record of BC-001, Action Item 1)

**Status of this record:** final. The assistant read the milestone against
every criterion and recorded what it found; S01 confirmed the open point on
2026-10-08 and the verdict is `Go`.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | A concrete deliverable is defined for every gate | Pass | Deliverable: a contrast measure and a faint-colour filter in the source file under `src/`, applied when the palette is extracted, with their tests and one real run that shows the painting. It is a tangible output, not a date |
| 2 | Explicit Go/No-Go criteria are stated for each gate | Pass | Five criteria, each with a Go and a No-Go column and a check that can be run: the measure's values and the filter's limit by tests, the printed palette with every contrast, all tests and both tools, a timed run with a captured picture, and the review record |
| 3 | Dependencies on other milestones are explicitly mapped | Pass | Dependencies table names MIL-001 (the filter is applied inside its palette function) and MIL-002 (the painting is redrawn and its tests must keep passing), each with its reason; both were decided Go on 2026-10-08 |
| 4 | Each milestone is traceable to a Business Case objective or KPI | Pass | Traceability table maps O6 (criteria 1, 2 and 4, SC8), O2 (criterion 2, SC3), O1 and O4 (criteria 3 and 4, SC1, SC5 and SC6) and O5 (criterion 5, SC7) of [BC-001]; O6 and SC8 are in the Business Case revision accepted with RC-007 |
| 5 | Milestone owner and approving reviewer are identified | Pass | Ownership table gives S01 for both; the shared identity is the accepted self-review |
| 6 | Milestone has a defined target date consistent with project constraints | Pass | 2026-10-10, inside the one-week limit of [BC-001] (2026-10-07 to 2026-10-14) and in agreement with the Project Plan, leaving four days of slack |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The `Language` row says `en` and the `Domain` row says `it`; `check-languages.sh --list` reports both |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list ("Software and IT") |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English; tool names are established technical terms |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Registry gives IT Executive English for MIL. Purpose, Deliverable and the Go/No-Go table state decisions and checks. The Tasks table is more technical (function names, `ruff`, `mypy --strict`) because the milestone reference requires each summary to be understood as an Issue without opening the file; S01 confirmed the same reading for MIL-001 and MIL-002 on 2026-10-07 |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | S01 confirmed that no dictionary is needed. The terms *faint colour*, *contrast* and *palette* match [BC-001] as revised and confirmed with RC-007, and *white shade* keeps its meaning from SC3. The new compound names *contrast measure* and *faint-colour filter* are used in the same form throughout |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Headings follow the MIL reference exactly |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | Only `docs/milestones/mil-003-visible-colours.md` exists |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version; there is no previous accepted version |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 confirmed on 2026-10-08 that the domain terms are used correctly, including the new compound names *contrast measure* and *faint-colour filter* (Action Item 1). S01 is also the author; the self-review was accepted on 2026-10-07 |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | WCAG is spelled out at its first use, in task 1 ("Web Content Accessibility Guidelines (WCAG) 2.x"); O1 to O6, SC1 to SC8 are defined in [BC-001] and cited with it; RC is the project's review-record prefix |

## Overall Verdict

Go — every criterion of [QC-MIL-001] and of [QC-LANG-001] passes (criterion 8 of [QC-LANG-001] is N-A for a first version). S01 accepted the documented self-review and confirmed on 2026-10-08 that the domain terms are used correctly and that the technical wording of the Tasks table is acceptable. The action item is closed. The milestone may now be synced to the git host and its tasks may start (plan-first gate).

## Action Items

| # | Action | Owner | Due |
| --- | --- | --- | --- |
| 1 | Confirm that the domain terms are used correctly, including *contrast measure* and *faint-colour filter* (QC-LANG-001 criterion 9), and that the technical wording of the Tasks table is acceptable in a milestone of register IT Executive English. **Closed 2026-10-08:** S01 confirmed both points | S01 | 2026-10-09 |

---

[MIL-003]: ../../milestones/mil-003-visible-colours.md
[BC-001]: ../../business-case.md
[QC-MIL-001]: ../../../framework/qc/qc-milestones-gateways.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
