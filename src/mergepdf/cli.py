#!/usr/bin/env python3
"""Command-line interface for merging PDF files."""

from __future__ import annotations

import argparse
from glob import glob
from pathlib import Path

from PyPDF2 import PdfMerger


def resolve_input_files(input_patterns: list[str]) -> list[Path]:
    """Resolve input values into PDF paths, expanding wildcard patterns."""
    resolved_paths: list[Path] = []

    for pattern in input_patterns:
        matches = sorted(Path(match) for match in glob(pattern))
        if matches:
            resolved_paths.extend(path for path in matches if path.is_file())
        else:
            resolved_paths.append(Path(pattern))

    if not resolved_paths:
        raise FileNotFoundError("No input PDF files were resolved from the provided patterns.")

    return resolved_paths


def merge_pdfs(input_files: list[Path], output_file: Path) -> None:
    """Merge the provided input PDFs into a single output file."""
    merger = PdfMerger()

    try:
        for pdf_path in input_files:
            if not pdf_path.is_file():
                raise FileNotFoundError(f"Input file not found: {pdf_path}")
            merger.append(str(pdf_path))

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open("wb") as file_obj:
            merger.write(file_obj)
    finally:
        merger.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="mergepdf",
        description="Merge multiple PDF files into one using PyPDF2.",
    )
    parser.add_argument(
        "input_files",
        nargs="+",
        type=str,
        help="Input PDF paths or wildcard patterns (for example: '*.pdf').",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=Path,
        help="Path to the merged output PDF file.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_files = resolve_input_files(args.input_files)
    merge_pdfs(input_files, args.output)
    print(f"Merged {len(input_files)} file(s) into {args.output}")


if __name__ == "__main__":
    main()
