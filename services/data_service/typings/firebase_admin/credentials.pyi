"""
This type stub file was generated by pyright.
"""

"""Firebase credentials module."""
_request = ...
_scopes = ...
AccessTokenInfo = ...

class Base:
    """Provides OAuth2 access tokens for accessing Firebase services."""

    def get_access_token(self):  # -> AccessTokenInfo:
        """Fetches a Google OAuth2 access token using this credential instance.

        Returns:
          AccessTokenInfo: An access token obtained using the credential.
        """
        ...
    def get_credential(self):
        """Returns the Google credential instance used for authentication."""
        ...

class Certificate(Base):
    """A credential initialized from a JSON certificate keyfile."""

    _CREDENTIAL_TYPE = ...
    def __init__(self, cert) -> None:
        """Initializes a credential from a Google service account certificate.

        Service account certificates can be downloaded as JSON files from the Firebase console.
        To instantiate a credential from a certificate file, either specify the file path or a
        dict representing the parsed contents of the file.

        Args:
          cert: Path to a certificate file or a dict representing the contents of a certificate.

        Raises:
          IOError: If the specified certificate file doesn't exist or cannot be read.
          ValueError: If the specified certificate is invalid.
        """
        ...
    @property
    def project_id(self): ...
    @property
    def signer(self): ...
    @property
    def service_account_email(self): ...
    def get_credential(self):  # -> Credentials:
        """Returns the underlying Google credential.

        Returns:
          google.auth.credentials.Credentials: A Google Auth credential instance."""
        ...

class ApplicationDefault(Base):
    """A Google Application Default credential."""

    def __init__(self) -> None:
        """Creates an instance that will use Application Default credentials.

        The credentials will be lazily initialized when get_credential() or
        project_id() is called. See those methods for possible errors raised.
        """
        ...
    def get_credential(self):  # -> Credentials | None:
        """Returns the underlying Google credential.

        Raises:
          google.auth.exceptions.DefaultCredentialsError: If Application Default
              credentials cannot be initialized in the current environment.
        Returns:
          google.auth.credentials.Credentials: A Google Auth credential instance."""
        ...
    @property
    def project_id(self):  # -> str | Any | None:
        """Returns the project_id from the underlying Google credential.

        Raises:
          google.auth.exceptions.DefaultCredentialsError: If Application Default
              credentials cannot be initialized in the current environment.
        Returns:
          str: The project id."""
        ...

class RefreshToken(Base):
    """A credential initialized from an existing refresh token."""

    _CREDENTIAL_TYPE = ...
    def __init__(self, refresh_token) -> None:
        """Initializes a credential from a refresh token JSON file.

        The JSON must consist of client_id, client_secret and refresh_token fields. Refresh
        token files are typically created and managed by the gcloud SDK. To instantiate
        a credential from a refresh token file, either specify the file path or a dict
        representing the parsed contents of the file.

        Args:
          refresh_token: Path to a refresh token file or a dict representing the contents of a
              refresh token file.

        Raises:
          IOError: If the specified file doesn't exist or cannot be read.
          ValueError: If the refresh token configuration is invalid.
        """
        ...
    @property
    def client_id(self): ...
    @property
    def client_secret(self): ...
    @property
    def refresh_token(self): ...
    def get_credential(self):  # -> Credentials:
        """Returns the underlying Google credential.

        Returns:
          google.auth.credentials.Credentials: A Google Auth credential instance."""
        ...
