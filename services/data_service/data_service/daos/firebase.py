"""Implements the DAO using Google Firebase"""
from __future__ import annotations
from typing import TYPE_CHECKING
from firebase_admin import storage, App, initialize_app
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
