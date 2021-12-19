"""
This type stub file was generated by pyright.
"""

"""Cloud Firestore module.

This module contains utilities for accessing the Google Cloud Firestore databases associated with
Firebase apps. This requires the ``google-cloud-firestore`` Python module.
"""
_FIRESTORE_ATTRIBUTE = ...

def client(app=...):
    """Returns a client that can be used to interact with Google Cloud Firestore.

    Args:
      app: An App instance (optional).

    Returns:
      google.cloud.firestore.Firestore: A `Firestore Client`_.

    Raises:
      ValueError: If a project ID is not specified either via options, credentials or
          environment variables, or if the specified project ID is not a valid string.

    .. _Firestore Client: https://googlecloudplatform.github.io/google-cloud-python/latest\
          /firestore/client.html
    """
    ...

class _FirestoreClient:
    """Holds a Google Cloud Firestore client instance."""

    def __init__(self, credentials, project) -> None: ...
    def get(self): ...
    @classmethod
    def from_app(cls, app):  # -> _FirestoreClient:
        """Creates a new _FirestoreClient for the specified app."""
        ...
