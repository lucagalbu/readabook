"""Implements the DAO using Google Firebase"""
from __future__ import annotations
from firebase_admin import storage, App, initialize_app


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
