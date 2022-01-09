"""
Implements the DAO using Google Firebase.

- The DAO is supposed to be created only once. If it is created multiple
times, the firebase app is initialized multiple times and an exception
is raised.
- The authorization is read from the .env file.
"""
import firebase_admin
from firebase_admin import App
from data_service.daos.base import DaoBase


class FirebaseDao(DaoBase):
    """Firebase DAO"""

    app: App

    def __init__(self):
        self._init_app()

    def _init_app(self):
        """Init a Firebase app and rises an exception if the app has already been initialized."""
        try:
            self.app = firebase_admin.initialize_app()
        except ValueError as exc:
            error = "Firebase app already in use or error in creating it. \
                Check if this DAO has already been initialized and if the authorization is correct."

            raise RuntimeError(error) from exc
