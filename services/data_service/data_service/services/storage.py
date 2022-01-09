"""Business logic of the data service"""
from typing import Union
from data_service.daos.base import DaoBase
from data_service.typings.book_info import BookInfo


class StorageService:
    """Class that implements the business logic"""

    dao: DaoBase

    def __init__(self, dao: DaoBase):
        self.dao = dao

    def upload(
        self, info: BookInfo, content_type: str, content: Union[str, bytes]
    ) -> None:
        """upload a text to a file in the database"""
        if content_type == "text/plain":
            content_str = content if isinstance(content, str) else content.decode()
            self._upload_from_string(info=info, content=content_str)
        else:
            raise NotImplementedError(f"Upload of {content_type} is not supported")

    def _upload_from_string(self, info: BookInfo, content: str) -> None:
        """Upload a book whose content is read from a string"""
        self.dao.upload_from_string(content=content, book_info=info)
