"""Business logic of the data service"""
from __future__ import annotations
import pathlib
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from data_service.daos.base import DaoBase


class StorageService:
    """Class that implements the business logic"""

    dao: DaoBase

    def __init__(self, dao: DaoBase):
        self.dao = dao

    def upload(
        self, content: Union[str, bytes], filename: str, content_type: str
    ) -> None:
        """upload a text to a file in the database"""
        if content_type == "text/plain":
            self._upload_text(content=content, filename=filename)
        else:
            raise NotImplementedError(f"Upload of {content_type} is not supported")

    def download_text(self, filename: str) -> str:
        """Read a textfile from the database"""
        extension = pathlib.Path(filename).suffix
        if extension != ".txt":
            raise NotImplementedError(f"File extension {extension} is not supported")

        return self.dao.download_text(filename)

    def delete_file(self, filename: str) -> None:
        """Delete an uploaded file"""
        self.dao.delete_file(filename)

    def get_text_files(self) -> Union[list[str], None]:
        """Get a list of text files from the database"""
        return self.dao.list_files(content_type="text/plain")

    def _upload_text(self, content: Union[str, bytes], filename: str) -> None:
        content_str = content if isinstance(content, str) else content.decode()
        if pathlib.Path(filename).suffix != ".txt":
            filename += ".txt"
        self.dao.upload_text(filename=filename, content=content_str)
