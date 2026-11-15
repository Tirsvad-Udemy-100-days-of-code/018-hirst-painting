[English](Getting-Started) · **Dansk** · [Bahasa Melayu](Getting-Started-ms)

# Kom godt i gang

## Krav

Python 3.13 eller nyere og `pytest` til testene. Programmet kræver `colorgram.py` 1.2.0 (som medbringer Pillow) og Tk til `turtle`-vinduet, så en skærm er nødvendig. For at køre testene og kodekontrollerne installerer du udviklingsværktøjerne (`pytest`, `ruff` og `mypy`) med `python -m pip install -e . --group dev`.

## Opsætning

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e . --group dev
```

## Kør

```bash
python src/hirst_painting.py
```

## Tests

```bash
python -m pytest
```

## Licens

Koden er udgivet under licensen GNU Affero General Public License v3.0 (AGPL-3.0-only). Se filen `LICENSE`.
