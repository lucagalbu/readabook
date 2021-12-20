"""Implements the DAO using Google Firebase"""
from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
from firebase_admin import storage, App, initialize_app
from google.cloud.storage.blob import Blob
from data_service.daos.base import DaoBase

if TYPE_CHECKING:
    import google.cloud.storage


class FirebaseClient:
    """Client to communicate with Firebase"""

    _app: App

    def __init__(self):
        self._app = initialize_app()

    @property
    def app(self):
        """Return a default Firebase app"""
        return self._app

    @property
    def bucket(self):
        """Return a Firebase Bucket from default app"""
        return storage.bucket()


class FirebaseDao(DaoBase):
    """Firebase DAO"""

    bucket: google.cloud.storage.Bucket

    def __init__(self, firebase_client: FirebaseClient):
        self.bucket = firebase_client.bucket

    def upload_text(self, filename: str, content: str):
        blob = self.bucket.blob(blob_name=filename)
        blob.upload_from_string(data=content)

    def download_text(self, filename: str) -> str:
        blob = self.bucket.blob(blob_name=filename)
        text = blob.download_as_text()
        return text

    def delete_file(self, filename: str) -> None:
        blob = self.bucket.blob(blob_name=filename)
        blob.delete()

    def list_files(self, content_type: Optional[str] = None) -> Union[list[str], None]:
        blobs = self._get_list_blobs()
        filtered_blobs = self._filter_blobs_by_content(blobs, content_type)
        name_blobs = [blob.name for blob in filtered_blobs]
        return name_blobs

    def _get_list_blobs(self) -> list[Blob]:
        client = self.bucket.client
        blobs_iterator = client.list_blobs(self.bucket)
        blobs_list = list(blobs_iterator)
        return blobs_list

    @staticmethod
    def _filter_blobs_by_content(blobs: list[Blob], content_type: Optional[str] = None):
        if content_type is not None:
            filtered_blobs = [
                blob for blob in blobs if blob.content_type == content_type
            ]
        else:
            filtered_blobs = blobs
        return filtered_blobs
