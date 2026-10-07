# Review Record: Business Case BC-001, objective O6 (delta)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [BC-001], [RC-001], [SA-001], [QC-BC-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version (draft prepared by the assistant for S01 to confirm)<br>Terms confirmed by S01, verdict `Go` | pending |

---

## Artifact Under Review

- Instance reviewed: [BC-001], the revision of 2026-10-08 (second row of its Version History)
- Checklist used: [QC-BC-001], together with [QC-LANG-001] because the Business Case is written in the PO language
- Scope: delta re-review of criteria 2, 3, 4, 5 and 6 of [QC-BC-001] and criteria 3, 4, 5, 9 and 10 of [QC-LANG-001]. Reason: the revision adds objective O6, success criterion SC8, a scope item, a risk row, the contrast standard (WCAG) and a sentence in the Problem Statement, and it changes the Stakeholders row from "O1 to O5" to "O1 to O6". Earlier record: [RC-001], which passed every criterion on the first version. The other criteria are untouched by the revision and keep their earlier result: [QC-BC-001] 1 (cost-benefit), 7 (assumptions and constraints) and 8 (recommendation), and [QC-LANG-001] 1, 2, 6, 7 and 8 (metadata, headings, no translated twin, no change of language)
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none. S01 reads English and knows the IT domain. S01 is also the author; S01 accepted a documented self-review on 2026-10-07 (see [RC-001], Action Item 1)

**Status of this record:** final. The assistant read the revised Business
Case against the criteria above; S01 confirmed the open point on 2026-10-08
and the verdict is `Go`.

**Stakeholder Analysis:** [SA-001] is not revised. S01's concern "The result looks clean and the window stays open until a click" (Usability) already covers O6, and every concern still traces to an objective, so its own checklist result is unchanged.

**Evidence for SC8 and the risk row:** the palette of the reference image was measured on 2026-10-08 with the WCAG contrast ratio against white. The 30 colours range from 1.22 to 15.85; the eight palest lie between 1.22 and 1.96, the next colour is at 2.56, so a limit of 2.0 removes 8 and keeps 22. The limit was chosen by S01 on 2026-10-08.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 2 | Risks are identified with documented impact and mitigation | Pass | The Risks table now has 7 rows; the new row (the contrast cut-off removes too many colours) has the impact "The painting looks dull" and a mitigation with figures from the measurement above |
| 3 | Success criteria are measurable, stating explicit targets rather than vague aspirations | Pass | SC8 states a target (0 palette colours with a contrast ratio against white below 2.0) and a measure (the printed palette with the contrast of every colour). It is consistent with SC3, which still holds for the final palette |
| 4 | Scope explicitly separates In Scope vs Out of Scope | Pass | The new In Scope item names the faint-colour removal and its limit; Out of Scope is unchanged and still distinct (no other parameters, no interface, no packaging) |
| 5 | Stakeholders are cross-referenced to Stakeholder Analysis IDs rather than re-described inline | Pass | The Stakeholders table still cites S01 only, now for "O1 to O6"; the new text refers to S01 by ID |
| 6 | Methodology and quality-standard foundation are stated explicitly (e.g. ISO/IEC 25010, Larman) | Pass | The Methodological and Standards Foundation gains a "Contrast" bullet naming the WCAG 2.x contrast ratio computed from relative luminance, with its two reference values (1.0 for white, 21.0 for black) |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The new prose and table cells are English |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Registry gives IT Executive English for BC. The new objective, criterion and risk state decisions and targets; the technical definition (relative luminance) is confined to the standards bullet where a standard belongs |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | S01 confirmed on 2026-10-07 that no dictionary is needed. The new term *faint colour* is used in every new place (Problem Statement, In Scope, Risks) and is defined by SC8 as a contrast below 2.0; *white shade* keeps its meaning from SC3 |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 confirmed on 2026-10-08 that the new terms *faint colour* and *contrast ratio* are used correctly (Action Item 1). S01 is also the author; the self-review was accepted on 2026-10-07 |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | WCAG is spelled out at its first use ("Web Content Accessibility Guidelines (WCAG) 2.x"); O6 and SC8 are defined by their tables |

## Overall Verdict

Go — every criterion in the delta passes. S01 confirmed on 2026-10-08 that the new terms *faint colour* and *contrast ratio* are used correctly, so [QC-LANG-001] criterion 9 is closed and the action item is closed. The revision of [BC-001] can be `Accepted`, after which the new phase can be planned against O6 and SC8.

## Action Items

| # | Action | Owner | Due |
| --- | --- | --- | --- |
| 1 | Confirm that the new terms *faint colour* and *contrast ratio* are used correctly (QC-LANG-001 criterion 9). **Closed 2026-10-08:** S01 confirmed both terms | S01 | 2026-10-09 |

---

[BC-001]: ../../business-case.md
[RC-001]: ./rc-001-business-case.md
[SA-001]: ../../stakeholder-analysis.md
[QC-BC-001]: ../../../framework/qc/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
