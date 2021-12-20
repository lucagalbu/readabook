"""Defines the interface all the DAOs must comply with"""
from abc import ABC, abstractmethod
from typing import Optional, Union


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

    @abstractmethod
    def list_files(self, content_type: Optional[str] = None) -> Union[list[str], None]:
        """Get a list of all files with text content"""
        ...
