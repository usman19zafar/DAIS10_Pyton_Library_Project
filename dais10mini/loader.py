"""
DAIS-10 Mini Multi-Format Loader (Final Version)

Supported Formats:
- CSV
- JSON (array or object)

Deterministic loader with safe validation.
"""

import csv
import json
from pathlib import Path
from typing import List, Dict, Any


class MultiFormatLoader:
    """Deterministic file loader"""

    # -------------------------------------------------
    # Format Detection
    # -------------------------------------------------

    @staticmethod
    def detect_format(filepath: str) -> str:
        """Detect file extension format"""

        ext = Path(filepath).suffix.lower().replace(".", "")

        return ext

    # -------------------------------------------------
    # CSV Loader
    # -------------------------------------------------

    @staticmethod
    def load_csv(filepath: str) -> List[Dict[str, Any]]:
        """Load CSV file"""

        if not Path(filepath).exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)

    # -------------------------------------------------
    # JSON Loader
    # -------------------------------------------------

    @staticmethod
    def load_json(filepath: str) -> List[Dict[str, Any]]:
        """Load JSON file"""

        if not Path(filepath).exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            return data

        if isinstance(data, dict):
            return [data]

        raise ValueError(
            f"Invalid JSON structure in {filepath}. "
            "Must be object or array."
        )

    # -------------------------------------------------
    # Universal Loader
    # -------------------------------------------------

    @staticmethod
    def load(filepath: str) -> List[Dict[str, Any]]:
        """Auto-detect and load file"""

        fmt = MultiFormatLoader.detect_format(filepath)

        if fmt == "json":
            return MultiFormatLoader.load_json(filepath)

        if fmt == "csv":
            return MultiFormatLoader.load_csv(filepath)

        raise ValueError(
            f"Unsupported format '.{fmt}'. "
            "Supported formats: CSV, JSON"
        )