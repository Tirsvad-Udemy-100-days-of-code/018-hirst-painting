[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Melayu**

# Bermula

## Keperluan

Python 3.13 atau lebih baharu dan `pytest` untuk ujian. Program ini memerlukan `colorgram.py` 1.2.0 (yang membawa Pillow) dan Tk untuk tetingkap `turtle`, jadi paparan diperlukan. Untuk menjalankan ujian dan semakan kod, pasang alat pembangunan (`pytest`, `ruff` dan `mypy`) dengan `python -m pip install -e . --group dev`.

## Persediaan

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e . --group dev
```

## Jalankan

```bash
python src/hirst_painting.py
```

## Ujian

```bash
python -m pytest
```

## Lesen

Kod ini dilesenkan di bawah GNU Affero General Public License v3.0 (AGPL-3.0-only). Lihat fail `LICENSE`.
