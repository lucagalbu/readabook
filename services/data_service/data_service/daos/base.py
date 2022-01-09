"""Defines the interface all the DAOs must comply with"""
from abc import ABC, abstractmethod
from data_service.typings.book_info import BookInfo


class DaoBase(ABC):
    """Dao interface"""

    @abstractmethod
    def upload_from_string(self, content: str, book_info: BookInfo) -> None:
        """
        Upload a file to the database, reading the content as a string.
        It creates the entry with the book info in the realtime database,
        and a file with the book content in the cloud storage. The filename
        is the md5 of the content.
        """
        ...
