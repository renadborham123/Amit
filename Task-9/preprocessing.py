"""Reusable preprocessing functions for tabular CSV datasets."""

from __future__ import annotations

from os import PathLike, fspath
from pathlib import Path
from typing import Iterable

import pandas as pd


def Read_data_file(file_path: str | PathLike[str]) -> pd.DataFrame:
    """Read a CSV file and return its contents as a pandas DataFrame.

    Args:
        file_path: Path to the CSV file.

    Returns:
        pandas.DataFrame: Data loaded from the CSV file.

    Raises:
        ValueError: If the path is empty, points to a directory, or the CSV
            cannot be parsed/read.
        FileNotFoundError: If the path does not exist.
        TypeError: If ``file_path`` is not a path-like value.
    """

    if not isinstance(file_path, (str, PathLike)):
        raise TypeError("file_path must be a string or path-like value")

    raw_path = fspath(file_path)
    if not raw_path or not str(raw_path).strip():
        raise ValueError("file_path cannot be empty")

    path = Path(raw_path).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"CSV file was not found: {path}")
    if not path.is_file():
        raise ValueError(f"The provided path is not a file: {path}")

    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError as error:
        raise ValueError(f"The CSV file is empty: {path}") from error
    except pd.errors.ParserError as error:
        raise ValueError(f"The CSV file could not be parsed: {path}") from error
    except UnicodeDecodeError as error:
        raise ValueError(f"The CSV file encoding could not be read: {path}") from error
    except OSError as error:
        raise ValueError(f"The CSV file could not be read: {path}") from error


def Drop_unnecessary_features(
    df: pd.DataFrame,
    cols_to_drop: Iterable[str],
) -> pd.DataFrame:
    """Return a copy of ``df`` without the configured unnecessary columns.

    The function is dataset-agnostic: callers provide the columns to remove,
    usually from a configuration module. Missing column names are ignored so
    the same configuration can safely be used with related datasets.

    Args:
        df: Input DataFrame.
        cols_to_drop: Iterable of column names to remove.

    Returns:
        pandas.DataFrame: A new DataFrame with requested columns removed.

    Raises:
        TypeError: If ``df`` is not a DataFrame or column names are invalid.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    if isinstance(cols_to_drop, (str, bytes)):
        raise TypeError("cols_to_drop must be an iterable of column names")

    try:
        columns = list(cols_to_drop)
    except TypeError as error:
        raise TypeError("cols_to_drop must be an iterable of column names") from error

    if any(not isinstance(column, str) for column in columns):
        raise TypeError("every column name in cols_to_drop must be a string")

    return df.drop(columns=columns, errors="ignore").copy()


def Check_data_type(df: pd.DataFrame) -> pd.DataFrame:
    """Build a transposed data-quality report for every DataFrame column.

    The returned report uses the original column names as columns and report
    fields as rows, including datatype and the number of unique values. Nulls
    count as a value so the uniqueness count reflects the complete dataset.

    Args:
        df: DataFrame to inspect.

    Returns:
        pandas.DataFrame: Transposed report with ``data_type`` and
            ``unique_values`` rows.

    Raises:
        TypeError: If ``df`` is not a pandas DataFrame.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")

    report = pd.DataFrame(
        {
            "data_type": df.dtypes.astype(str),
            "unique_values": df.nunique(dropna=False),
        }
    )
    return report.T


# Lowercase aliases make the functions convenient in normal Python code while
# preserving the exact names required by the assignment.
read_data_file = Read_data_file
drop_unnecessary_features = Drop_unnecessary_features
check_data_type = Check_data_type
