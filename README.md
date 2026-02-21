# MergePDF

A Python project that merges multiple PDF files into a single PDF using the
`PyPDF2` library.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Usage

```bash
mergepdf input1.pdf input2.pdf input3.pdf --output merged.pdf
```

You can also use wildcard patterns (quote them so the app can expand `*`):

```bash
mergepdf "./invoices/*.pdf" --output merged.pdf
```

You can also run it directly as a module:

```bash
PYTHONPATH=src python -m mergepdf.cli input1.pdf input2.pdf --output merged.pdf
```

## Downloadable project bundle

To create a single zip file you can copy/download to your PC:

```bash
./scripts/create_download_bundle.sh
```

This generates:

- `downloads/mergepdf_project.zip`
