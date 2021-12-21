"""Defines the interface for each service implementing text analysis."""
import enum
from abc import ABC, abstractmethod
from typing import Counter, Optional


class UniversalPos(enum.Enum):
    """Enum with the standard part of the speech (pos) categories"""

    ADJ = enum.auto()
    ADP = enum.auto()
    ADV = enum.auto()
    AUX = enum.auto()
    CCONJ = enum.auto()
    DET = enum.auto()
    INTJ = enum.auto()
    NOUN = enum.auto()
    NUM = enum.auto()
    PART = enum.auto()
    PRON = enum.auto()
    PROPN = enum.auto()
    PUNCT = enum.auto()
    SCONJ = enum.auto()
    SYM = enum.auto()
    VERB = enum.auto()
    X = enum.auto()


class NLPBase(ABC):
    """Base class to analyze texts"""

    @abstractmethod
    def load_text(self, text: str) -> None:
        """Load a text to analyse.
        This function must be called before any analysis can be performed."""
        ...

    @abstractmethod
    def lemmas_frequency(
        self,
        include: Optional[list[UniversalPos]] = None,
        exclude: Optional[list[UniversalPos]] = None,
    ) -> Counter[str]:
        """Return the frequency of the different lemmas found in the text.
        Specific pos categories can be included or excluded using the provided arguments."""
        ...
