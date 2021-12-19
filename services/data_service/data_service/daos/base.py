"""Defines the interface all the DAOs must comply with"""
from abc import ABC, abstractmethod


class DaoBase(ABC):
    """Dao interface"""

    @abstractmethod
    def upload_text(self, filename: str, content: str) -> None:
        """upload text to a file in the database"""
        ...

    @abstractmethod
    def download_text(self, filename: str) -> str:
        """read content from text file in the database"""
        ...

    @abstractmethod
    def delete_file(self, filename: str) -> None:
        """delete a file from the database"""
        ...
