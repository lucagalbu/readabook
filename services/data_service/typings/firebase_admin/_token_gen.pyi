"""
This type stub file was generated by pyright.
"""

from google.auth import transport
from firebase_admin import _auth_utils, exceptions

"""Firebase token minting and validation sub module."""
ID_TOKEN_ISSUER_PREFIX = ...
ID_TOKEN_CERT_URI = ...
COOKIE_ISSUER_PREFIX = ...
COOKIE_CERT_URI = ...
MIN_SESSION_COOKIE_DURATION_SECONDS = ...
MAX_SESSION_COOKIE_DURATION_SECONDS = ...
MAX_TOKEN_LIFETIME_SECONDS = ...
FIREBASE_AUDIENCE = ...
RESERVED_CLAIMS = ...
METADATA_SERVICE_URL = ...
ALGORITHM_RS256 = ...
ALGORITHM_NONE = ...
AUTH_EMULATOR_EMAIL = ...

class _EmulatedSigner(google.auth.crypt.Signer):
    key_id = ...
    def __init__(self) -> None: ...
    def sign(self, message): ...

class _SigningProvider:
    """Stores a reference to a google.auth.crypto.Signer."""

    def __init__(self, signer, signer_email, alg=...) -> None: ...
    @property
    def signer(self): ...
    @property
    def signer_email(self): ...
    @property
    def alg(self): ...
    @classmethod
    def from_credential(cls, google_cred): ...
    @classmethod
    def from_iam(cls, request, google_cred, service_account): ...
    @classmethod
    def for_emulator(cls): ...

class TokenGenerator:
    """Generates custom tokens and session cookies."""

    ID_TOOLKIT_URL = ...
    def __init__(self, app, http_client, url_override=...) -> None: ...
    @property
    def signing_provider(self):  # -> _SigningProvider:
        """Initializes and returns the SigningProvider instance to be used."""
        ...
    def create_custom_token(self, uid, developer_claims=..., tenant_id=...):
        """Builds and signs a Firebase custom auth token."""
        ...
    def create_session_cookie(self, id_token, expires_in):
        """Creates a session cookie from the provided ID token."""
        ...

class CertificateFetchRequest(transport.Request):
    """A google-auth transport that supports HTTP cache-control.

    Also injects a timeout to each outgoing HTTP request.
    """

    def __init__(self, timeout_seconds=...) -> None: ...
    @property
    def session(self): ...
    @property
    def timeout_seconds(self): ...
    def __call__(
        self, url, method=..., body=..., headers=..., timeout=..., **kwargs
    ): ...

class TokenVerifier:
    """Verifies ID tokens and session cookies."""

    def __init__(self, app) -> None: ...
    def verify_id_token(self, id_token): ...
    def verify_session_cookie(self, cookie): ...

class _JWTVerifier:
    """Verifies Firebase JWTs (ID tokens or session cookies)."""

    def __init__(self, **kwargs) -> None: ...
    def verify(self, token, request):
        """Verifies the signature and data for the provided JWT."""
        ...

class TokenSignError(exceptions.UnknownError):
    """Unexpected error while signing a Firebase custom token."""

    def __init__(self, message, cause) -> None: ...

class CertificateFetchError(exceptions.UnknownError):
    """Failed to fetch some public key certificates required to verify a token."""

    def __init__(self, message, cause) -> None: ...

class ExpiredIdTokenError(_auth_utils.InvalidIdTokenError):
    """The provided ID token is expired."""

    def __init__(self, message, cause) -> None: ...

class RevokedIdTokenError(_auth_utils.InvalidIdTokenError):
    """The provided ID token has been revoked."""

    def __init__(self, message) -> None: ...

class InvalidSessionCookieError(exceptions.InvalidArgumentError):
    """The provided string is not a valid Firebase session cookie."""

    def __init__(self, message, cause=...) -> None: ...

class ExpiredSessionCookieError(InvalidSessionCookieError):
    """The provided session cookie is expired."""

    def __init__(self, message, cause) -> None: ...

class RevokedSessionCookieError(InvalidSessionCookieError):
    """The provided session cookie has been revoked."""

    def __init__(self, message) -> None: ...
