"""
Implements the DAO using Google Firebase.

- The DAO is supposed to be created only once. If it is created multiple
times, the firebase app is initialized multiple times and an exception
is raised.
- The authorization is read from the .env file.
- The app config is read from the json specified in the .env file.
- The DAO retrieves the bucket, whose name is read from the app config.
"""
import firebase_admin
from firebase_admin import App, storage
from google.cloud.storage.bucket import Bucket
from data_service.daos.base import DaoBase


class FirebaseDao(DaoBase):
    """Firebase DAO"""

    app: App
    bucket: Bucket

    def __init__(self):
        self._init_app()
        self.bucket = storage.bucket()

    def _init_app(self):
        """Init a Firebase app and rises an exception if the app has already been initialized."""
        try:
            self.app = firebase_admin.initialize_app()
        except ValueError as exc:
            error = "Firebase app already in use or error in creating it. \
                Check if this DAO has already been initialized and if the authorization is correct."

            raise RuntimeError(error) from exc

    def _get_bucket(self):
        """Get the bucket associated to the firebase account and specified in the global setting.
        If no bucket is found, an error is returned."""
        try:
            self.bucket = storage.bucket()
        except ValueError as exc:
            error = "Bucket not found. Check if the settings are correct."
            raise RuntimeError(error) from exc
