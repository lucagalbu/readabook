"""Implements text analysis using NLP from the spaCy package"""
import enum
from typing import Counter, Dict, Optional, TypeVar
import spacy
from spacy.language import Language
from spacy import tokens
from text_service.services.nlp_base import NLPBase, UniversalPos


T = TypeVar("T")  # pylint: disable=invalid-name


class Languages(enum.Enum):
    """Enumeration with the possible languages."""

    RUSSIAN = enum.auto()


class SpaCy(NLPBase):
    """Class that implements the NLP analyses using spaCy."""

    _nlp: Language
    _doc: tokens.Doc
    _map_pos: Dict[UniversalPos, list[str]]

    def __init__(self, language: Languages):
        self._create_nlp(language)
        self._create_map_pos()
        self._doc = self.nlp("")

    def load_text(self, text: str):
        self._doc = self.nlp(text)

    def lemmas_frequency(
        self,
        include: Optional[list[UniversalPos]] = None,
        exclude: Optional[list[UniversalPos]] = None,
    ) -> Counter[str]:
        include_mapped = (
            self._convert_list_pos_to_internal(include)
            if include is not None
            else self._get_all_internal_pos()
        )

        exclude_mapped = (
            self._convert_list_pos_to_internal(exclude) if exclude is not None else []
        )

        words = [
            token.lemma_
            for token in self._doc
            if token.pos_ in include_mapped and token.pos_ not in exclude_mapped
        ]
        counts = Counter(words)
        normalized = self._normalize_counter(counts)
        return normalized

    # Private methods

    def _create_nlp(self, language: Languages):
        excluded_pipes = self._get_excluded_pipes()
        language_pack = self._get_language_pack(language)
        self.nlp = spacy.load(language_pack, exclude=excluded_pipes)

    def _create_map_pos(self):
        mapping = {
            UniversalPos.ADJ: ["ADJ"],
            UniversalPos.ADP: ["ADP"],
            UniversalPos.ADV: ["ADV"],
            UniversalPos.AUX: ["AUX"],
            UniversalPos.CCONJ: ["CCONJ"],
            UniversalPos.DET: ["DET"],
            UniversalPos.INTJ: ["INTJ"],
            UniversalPos.NOUN: ["NOUN"],
            UniversalPos.NUM: ["NUM"],
            UniversalPos.PART: ["PART"],
            UniversalPos.PRON: ["PRON"],
            UniversalPos.PROPN: ["PROPN"],
            UniversalPos.PUNCT: ["PUNCT"],
            UniversalPos.SCONJ: ["SCONJ"],
            UniversalPos.SYM: ["SYM"],
            UniversalPos.VERB: ["VERB"],
            UniversalPos.X: ["X", "SPACE"],
        }

        self._map_pos = mapping

    @staticmethod
    def _get_excluded_pipes() -> list[str]:
        excluded_pipes = [
            "parser",
            "textcat",
        ]
        return excluded_pipes

    @staticmethod
    def _get_language_pack(language: Languages) -> str:
        if language == Languages.RUSSIAN:
            return "ru_core_news_sm"

        raise NotImplementedError("The requested language is not implemented")

    def _convert_list_pos_to_internal(self, pos: list[UniversalPos]) -> list[str]:
        mapped_iterator = map(lambda element: self._map_pos[element], pos)
        mapped_list = list(mapped_iterator)
        mapped_flatten = [item for sublist in mapped_list for item in sublist]
        return mapped_flatten

    def _get_all_internal_pos(self):
        internal_pos = list(self._map_pos.values())
        internal_flatten = self._flatten_list(internal_pos)
        return internal_flatten

    @staticmethod
    def _normalize_counter(counts: Counter[T]) -> Counter[T]:
        total = sum(counts.values())
        normalized = Counter({key: counts[key] / total for key in counts})
        return normalized

    @staticmethod
    def _flatten_list(original: list[list[T]]) -> list[T]:
        flatten = [item for sublist in original for item in sublist]
        return flatten


with open("C:\\Users\\luke\\Documents\\Емеля ожотник.txt", encoding="utf-8") as file:
    text_current = file.read()

nlp = SpaCy(Languages.RUSSIAN)
nlp.load_text(text_current)
result = nlp.lemmas_frequency(include=[UniversalPos.NOUN, UniversalPos.VERB])
print(result.most_common()[:-10:-1])
print(len(result))
