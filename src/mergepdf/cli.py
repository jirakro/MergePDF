#!/usr/bin/env python3
"""Command-line interface for merging PDF files."""

from __future__ import annotations

import argparse
from pathlib import Path

from PyPDF2 import PdfMerger


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
        type=Path,
        help="Paths to the input PDF files in merge order.",
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
    merge_pdfs(args.input_files, args.output)
    print(f"Merged {len(args.input_files)} file(s) into {args.output}")


if __name__ == "__main__":
    main()
