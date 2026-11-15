**English** · [Dansk](Getting-Started-da) · [Bahasa Melayu](Getting-Started-ms)

# Getting Started

## Requirements

Python 3.13 or newer and `pytest` for the tests. The program needs `colorgram.py` 1.2.0 (which brings Pillow) and Tk for the `turtle` window, so a display is required. To run the tests and the code checks, install the development tools (`pytest`, `ruff` and `mypy`) with `python -m pip install -e . --group dev`.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e . --group dev
```

## Run

```bash
python src/hirst_painting.py
```

## Tests

```bash
python -m pytest
```

## Licence

The code is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0-only). See the `LICENSE` file.
