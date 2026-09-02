"""Command-line entry point for the Task-9 preprocessing pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

import pandas as pd

from config import COLS_TO_DROP
from preprocessing import (
    Check_data_type,
    Drop_unnecessary_features,
    Read_data_file,
)


def run_pipeline(
    file_path: str | Path,
    cols_to_drop: list[str] | tuple[str, ...] = COLS_TO_DROP,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Read, inspect, and clean a dataset.

    Args:
        file_path: Path to the CSV input.
        cols_to_drop: Configured columns to remove.

    Returns:
        tuple: Original DataFrame, original data-quality report, and cleaned
            DataFrame. A cleaned report can be generated with ``Check_data_type``.
    """

    dataframe = Read_data_file(file_path)
    before_report = Check_data_type(dataframe)
    cleaned_dataframe = Drop_unnecessary_features(dataframe, cols_to_drop)
    return dataframe, before_report, cleaned_dataframe


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(description="Run the Titanic preprocessing pipeline")
    parser.add_argument(
        "file_path",
        nargs="?",
        help="Path to the Titanic CSV file (prompted when omitted)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path where the cleaned CSV should be written",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the pipeline and print data-quality reports.

    Returns:
        int: ``0`` for success and ``1`` when a user-facing input error occurs.
    """

    args = build_parser().parse_args(argv)
    file_path = args.file_path or input("Enter the path to the Titanic CSV file: ").strip()

    try:
        dataframe, before_report, cleaned_dataframe = run_pipeline(
            file_path,
            COLS_TO_DROP,
        )
    except (FileNotFoundError, TypeError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    print(f"Loaded {len(dataframe)} rows and {len(dataframe.columns)} columns.")
    print("\nData-quality report before dropping features:")
    print(before_report)

    print("\nConfigured columns to drop:")
    print(COLS_TO_DROP)
    print("\nCleaned columns:")
    print(list(cleaned_dataframe.columns))
    print("\nData-quality report after dropping features:")
    print(Check_data_type(cleaned_dataframe))

    if args.output:
        cleaned_dataframe.to_csv(args.output, index=False)
        print(f"\nCleaned dataset saved to: {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
