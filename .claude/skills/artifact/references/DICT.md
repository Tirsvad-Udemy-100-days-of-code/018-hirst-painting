# Domain Dictionary (DICT)

Cite in `CrossReference` only if the instance exists (`new-artifact.sh` checks this for you):

- **BC** — The business goals the vocabulary serves
- **SA** — The Product Owner (and other business stakeholders) whose terms are recorded
- **DM** — Concepts whose PO terms are recorded

## Required sections (after Metadata / Version History)

1. **Purpose and Scope** — the PO language and domain (from the registry's
   `Languages` section, also in the `Language` and `Domain` Metadata rows) and
   what the dictionary covers.
2. **Dictionary** — one row per term:
   `PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in`.
   The definition is written in the PO language. "Used as PO term in" and
   "Used as IT term in" list artifact types (for example `DM` and `OC, SD,
   DCD, ERD`).
3. **Rules** — the register split (PO term in the Domain Model, use cases and
   user stories; IT term in the Operation Contract, Sequence Diagram, Design
   Class Diagram and ERD) and one IT term per PO term.

One dictionary has one domain: the PO terms are the domain's own words (for
example `medical`), the IT terms are professional IT. A project whose PO terms
come from two domains keeps one dictionary per domain, each with its own
`Domain` row; a term never appears in two.

Keep the dictionary in step with the Domain Model: a new concept gets a row
in the same change. When the PO language is English, the PO and IT columns can
still differ (a business word against a technical one); keep the file anyway
when the two registers use different words.
