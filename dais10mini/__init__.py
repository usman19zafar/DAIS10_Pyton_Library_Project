"""
DAIS-10 Mini Library
Deterministic schema-driven completeness scoring utility.

Version: 1.1.3
Author: Dr. Usman Zafar
"""

__version__ = "1.1.3"

from .analyzer import Analyzer
from .loader import MultiFormatLoader

__all__ = [
    "Analyzer",
    "MultiFormatLoader",
    "__version__"
]