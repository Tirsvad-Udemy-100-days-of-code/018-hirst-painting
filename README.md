# 🚀 Hirst Painting

A Python program that draws a Hirst-style spot painting with `turtle`: a 10 by 10 grid of dots, each coloured at random from a palette extracted from an image with `colorgram`. It is Day 18 of Udemy's 100 Days of Code course, and a small project delivered through the SQA and QC framework.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The program opens a `turtle` window and draws 100 dots of size 20, 50 units apart, in 10 rows of 10, centred in the window. Each dot takes a random colour from a palette that `colorgram` extracts from a reference image. White shades (red, green and blue all at 240 or above) and other faint colours, those whose contrast with white is below 2.0 (the contrast ratio of the Web Content Accessibility Guidelines), are removed from the palette, because their dots would hardly show on the white background. The reference image gives a palette of 22 colours. The drawing runs without animation, takes well under a second, and the window stays open until you click it.

| Part | What it is for |
| --- | --- |
| `src/hirst_painting.py` | The program: the palette (`extract_palette`, the white-shade and faint-colour filters and the contrast measure), the dot positions, the pen setup, the drawing and `main` |
| `tests/test_hirst_painting.py` | The tests, 77 test cases for `pytest` |
| `assets/` | The reference image `20260524_132700.jpg`, which the palette is taken from |
| `docs/` | The project documents; see the appendix |
| `framework/` | The SQA and QC framework this project uses, a git submodule |
| `pyproject.toml` | The Python version, the pinned dependencies, and the settings of `ruff`, `mypy` and `pytest` |

## 📋 Requirements

- **Python 3.13 or newer, with Tk.** The `turtle` module needs Tk to open a window. The python.org and Microsoft Store installers include it; on Debian and Ubuntu the package is `python3-tk`.
- **A display.** The program opens a window, and 10 of the 77 test cases, the ones that use Tk, need a display as well.
- **`colorgram.py` 1.2.0**, which brings Pillow, to extract the palette from the image. It is pinned in `pyproject.toml`.
- **`pytest`, `ruff` and `mypy`**, pinned in the `dev` group, to test, format, lint and type-check.
- **pip 25.1 or newer**, for the `--group` option in the setup command below.

Verified with Python 3.13.14 and Tk 8.6 on Windows 11.

## 🛠️ Setup

```bash
git clone ssh://git@git.tirsystem.com:10022/Tirsvad-Udemy-100-days-of-code/018-hirst-painting.git
cd 018-hirst-painting
python -m venv .venv
source .venv/bin/activate          # on Windows: .venv\Scripts\activate
python -m pip install -e . --group dev
```

The `framework/` submodule is only needed to work on the project documents; the program and its tests do not use it. Add `--recurse-submodules` to the clone command if you have access to it.

## ▶️ Run

```bash
python src/hirst_painting.py
```

A window opens, the painting appears at once, and a click closes it. The image the palette is taken from is the constant `REFERENCE_IMAGE_PATH` in `src/hirst_painting.py`.

## 🧪 Tests

```bash
python -m pytest
python -m ruff format --check .
python -m ruff check .
python -m mypy
```

`mypy` runs in strict mode. Ten of the 77 test cases need a display for Tk; this was accepted in the review record of the code ([RC-006][RC-006]).

## 📄 License

GNU Affero General Public License v3.0; see [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways, their schedule and the Go/No-Go decisions |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Review records][reviews] | One record per review of a document or of the code, against its quality checklist |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Framework][framework] | The SQA and QC framework this project uses, mounted as a submodule |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting
[documentation]: ./docs/
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-hirst-painting/issues
[license]: ./LICENSE
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[reviews]: ./docs/sqa/reviews/
[RC-006]: ./docs/sqa/reviews/rc-006-code-mil-002.md
[registry]: ./docs/artifact-registry.md
[framework]: ./framework
