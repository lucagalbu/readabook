"""Type BookInfo"""
import dataclasses


@dataclasses.dataclass
class BookInfo:
    """dataclass to store the information about a book"""

    title: str
    author: str
