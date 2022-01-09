"""
Implements the DAO using Google Firebase.

- The DAO is supposed to be created only once. If it is created multiple
times, the firebase app is initialized multiple times and an exception
is raised.
- The authorization is read from the .env file.
- The app config is read from the json specified in the .env file.
- The DAO retrieves the bucket, whose name is read from the app config.
"""
import hashlib
import firebase_admin
from firebase_admin import App, storage, db
from google.cloud.storage.bucket import Bucket
from data_service.daos.base import DaoBase
from data_service.typings.book_info import BookInfo


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

    def upload_from_string(self, content: str, book_info: BookInfo) -> None:
        """Upload a book to Firebase. It creates the file in the cloud and
        add the info to the database. The filename name is the md5 of the content."""
        md5_content = hashlib.md5(content.encode()).hexdigest()
        self._add_string_to_bucket(filename=md5_content, content=content)
        self._add_book_to_db(book_info=book_info, name=md5_content)

    def _add_string_to_bucket(self, filename: str, content: str):
        """Add a file to the cloud storage reading the content from a string."""
        blob = self.bucket.blob(blob_name=filename)
        blob.upload_from_string(data=content)

    def _add_book_to_db(self, book_info: BookInfo, name: str):
        """Add an entry to the db with the book info"""
        db_ref = db.reference("/books")
        db_ref.set({name: {"title": book_info.title, "author": book_info.author}})

    def _get_bucket(self):
        """Get the bucket associated to the firebase account and specified in the global setting.
        If no bucket is found, an error is returned."""
        try:
            self.bucket = storage.bucket()
        except ValueError as exc:
            error = "Bucket not found. Check if the settings are correct."
            raise RuntimeError(error) from exc
