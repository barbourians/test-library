"""Data ingestion functions.

TODO: Complete these functions for the library project.
"""

import json

import pandas as pd
from pathlib import Path


def load_csv(filepath):
    """Load CSV file with error handling.

    Args:
        filepath: Path to CSV file

    Returns:
        DataFrame with loaded data

    TODO: Add error handling
    """
    return pd.read_csv(filepath)


def load_json(filepath):
    """Load JSON file and flatten structure.

    Args:
        filepath: Path to JSON file

    Returns:
        DataFrame with flattened data

    TODO: Implement JSON loading and flattening
    """
    with open(filepath, "r") as f:
        data = json.load(f)
    return pd.json_normalize(data)


def load_excel(filepath, sheet_name=0, **kwargs):
    """Load Excel file into DataFrame.

    Args:
        filepath (str | Path): Path to Excel file
        sheet_name (str|int|list[str|int]|None): Sheets to read
        **kwargs: Additional arguments for pd.read_excel()

    Returns:
        pd.DataFrame | dict[str, pd.DataFrame]: Loaded data. Dict when multiple sheets requested.

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If the sheet doesn't exist or file is invalid
        ImportError: If the required Excel engine isn't installed

    Example:
        >>> df = load_excel('../data/catalogue.xlsx', sheet_name='Catalogue')
        >>> print(len(df))
    """
    filepath = Path(filepath)

    # Check file exists
    if not filepath.exists():
        raise FileNotFoundError(f"Excel File not found: {filepath}")

    return pd.read_excel(filepath, sheet_name=sheet_name, **kwargs)
