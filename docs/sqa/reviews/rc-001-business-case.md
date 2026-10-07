# Review Record: Business Case BC-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-001 |
| CrossReference | [BC-001], [SA-001], [QC-BC-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version (draft prepared by the assistant for S01 to confirm)<br>Self-review and defaults confirmed by S01 | [b823d1f] |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-BC-001], together with [QC-LANG-001] because the Business Case is written in the PO language
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none. S01 reads English and knows the IT domain. S01 is also the author; S01 accepted a documented self-review on 2026-10-07 (Action Item 1)

**Status of this record:** final. The assistant read the document against
every criterion and recorded what it found; S01 confirmed the open points on
2026-10-07 and the verdict is `Go`.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | ROI/Cost-Benefit analysis is quantitative, or where qualitative, is explicitly justified | Pass | Cost–Benefit Assessment states it is qualitative "on purpose: this is a learning exercise with no revenue, so a monetary return would be invented", and lists costs and benefits |
| 2 | Risks are identified with documented impact and mitigation | Pass | Risks table has 6 rows; each has an Impact and a Mitigation |
| 3 | Success criteria are measurable, stating explicit targets rather than vague aspirations | Pass | SC1 to SC7 each have a target and a measure. SC3 (colour threshold 240) and SC6 (30 seconds) were confirmed by S01 on 2026-10-07 (Action Item 3) |
| 4 | Scope explicitly separates In Scope vs Out of Scope | Pass | `### In Scope` and `### Out of Scope` subsections, with distinct content |
| 5 | Stakeholders are cross-referenced to Stakeholder Analysis IDs rather than re-described inline | Pass | Stakeholders table cites S01 and says roles are in [SA-001]. Prose refers to S01 by ID, not by role |
| 6 | Methodology and quality-standard foundation are stated explicitly (e.g. ISO/IEC 25010, Larman) | Pass | "Methodological and Standards Foundation" names the plan-first workflow, Larman, ISO/IEC 25010:2023 and `qc-programming-python` |
| 7 | Assumptions and constraints are explicit and clearly distinguished from one another | Pass | Separate `## Assumptions` and `## Constraints` lists. The one-week timeline is an assumption, confirmed by S01 on 2026-10-07 (Action Item 3) |
| 8 | Document supports executive decision-making with a clear, unambiguous recommendation | Pass | Recommendation is a single "Proceed" with a one-sentence rationale |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The `Language` row says `en` and the `Domain` row says `it`; `check-languages.sh --list` reports both |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list ("Software and IT") |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English; tool names (`turtle`, `colorgram`, `exitonclick`) are established technical terms |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Registry gives IT Executive English for BC. The text states decisions, targets and risks; implementation detail was removed from the risks table during drafting. Tool names stay where an objective needs them |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The project has no Domain Dictionary (`DICT`), so there is no list to check against; the terms *dot*, *palette*, *painting*, *grid* and *phase* are used consistently here and in [SA-001]. "Spot painting" is the name of the genre; the elements are always "dots". S01 confirmed on 2026-10-07 that a dictionary is not needed (Action Item 2) |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Headings follow the BC reference exactly |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | Only `docs/business-case.md` exists |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version; there is no previous accepted version |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 confirmed on 2026-10-07 that the domain terms are used correctly (Action Item 2). S01 is also the author; the self-review was accepted by S01 (Action Item 1) |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | SQA and QC are spelled out in the Executive Summary; ISO/IEC, SC and O numbering are defined where introduced |

## Overall Verdict

Go — every criterion of [QC-BC-001] and of [QC-LANG-001] passes (criterion 8 of [QC-LANG-001] is N-A for a first version). S01 accepted the documented self-review, confirmed the defaults and the stakeholder list, and confirmed on 2026-10-07 that the domain terms are used correctly and that no Domain Dictionary is needed. All action items are closed.

## Action Items

| # | Action | Owner | Due |
| --- | --- | --- | --- |
| 1 | Name a reviewer who is not the author, or record here that the review is a documented self-review accepted by S01. **Closed 2026-10-07:** S01 accepted a documented self-review | S01 | 2026-10-09 |
| 2 | Confirm that the domain terms in [BC-001] are used correctly (QC-LANG-001 criterion 9), and that a Domain Dictionary is not needed for this project. **Closed 2026-10-07:** S01 confirmed both points | S01 | 2026-10-09 |
| 3 | Confirm or change the defaults in [BC-001]: one-week timeline from 2026-10-07, colour threshold 240 (SC3), 30-second run time (SC6); say where the reference image is. **Closed 2026-10-07 for the defaults:** S01 confirmed all three. The reference image location is still open; it is a risk of [BC-001] and goes to the Open Issues of the Project Plan | S01 | 2026-10-09 |

---

[BC-001]: ../../business-case.md
[SA-001]: ../../stakeholder-analysis.md
[QC-BC-001]: ../../../framework/qc/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[b823d1f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/commit/b823d1f405ebac6b0198605edd9d802518529725
