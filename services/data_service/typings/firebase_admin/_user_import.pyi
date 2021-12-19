"""
This type stub file was generated by pyright.
"""

"""Firebase user import sub module."""

def b64_encode(bytes_value): ...

class UserProvider:
    """Represents a user identity provider that can be associated with a Firebase user.

    One or more providers can be specified in an ``ImportUserRecord`` when importing users via
    ``auth.import_users()``.

    Args:
        uid: User's unique ID assigned by the identity provider.
        provider_id: ID of the identity provider. This can be a short domain name or the identifier
            of an OpenID identity provider.
        email: User's email address (optional).
        display_name: User's display name (optional).
        photo_url: User's photo URL (optional).
    """

    def __init__(
        self, uid, provider_id, email=..., display_name=..., photo_url=...
    ) -> None: ...
    @property
    def uid(self): ...
    @uid.setter
    def uid(self, uid): ...
    @property
    def provider_id(self): ...
    @provider_id.setter
    def provider_id(self, provider_id): ...
    @property
    def email(self): ...
    @email.setter
    def email(self, email): ...
    @property
    def display_name(self): ...
    @display_name.setter
    def display_name(self, display_name): ...
    @property
    def photo_url(self): ...
    @photo_url.setter
    def photo_url(self, photo_url): ...
    def to_dict(self): ...

class ImportUserRecord:
    """Represents a user account to be imported to Firebase Auth.

    Must specify the ``uid`` field at a minimum. A sequence of ``ImportUserRecord`` objects can be
    passed to the ``auth.import_users()`` function, in order to import those users into Firebase
    Auth in bulk. If the ``password_hash`` is set on a user, a hash configuration must be
    specified when calling ``import_users()``.

    Args:
        uid: User's unique ID. Must be a non-empty string not longer than 128 characters.
        email: User's email address (optional).
        email_verified: A boolean indicating whether the user's email has been verified (optional).
        display_name: User's display name (optional).
        phone_number: User's phone number (optional).
        photo_url: User's photo URL (optional).
        disabled: A boolean indicating whether this user account has been disabled (optional).
        user_metadata: An ``auth.UserMetadata`` instance with additional user metadata (optional).
        provider_data: A list of ``auth.UserProvider`` instances (optional).
        custom_claims: A ``dict`` of custom claims to be set on the user account (optional).
        password_hash: User's password hash as a ``bytes`` sequence (optional).
        password_salt: User's password salt as a ``bytes`` sequence (optional).

    Raises:
        ValueError: If provided arguments are invalid.
    """

    def __init__(
        self,
        uid,
        email=...,
        email_verified=...,
        display_name=...,
        phone_number=...,
        photo_url=...,
        disabled=...,
        user_metadata=...,
        provider_data=...,
        custom_claims=...,
        password_hash=...,
        password_salt=...,
    ) -> None: ...
    @property
    def uid(self): ...
    @uid.setter
    def uid(self, uid): ...
    @property
    def email(self): ...
    @email.setter
    def email(self, email): ...
    @property
    def display_name(self): ...
    @display_name.setter
    def display_name(self, display_name): ...
    @property
    def phone_number(self): ...
    @phone_number.setter
    def phone_number(self, phone_number): ...
    @property
    def photo_url(self): ...
    @photo_url.setter
    def photo_url(self, photo_url): ...
    @property
    def password_hash(self): ...
    @password_hash.setter
    def password_hash(self, password_hash): ...
    @property
    def password_salt(self): ...
    @password_salt.setter
    def password_salt(self, password_salt): ...
    @property
    def user_metadata(self): ...
    @user_metadata.setter
    def user_metadata(self, user_metadata): ...
    @property
    def provider_data(self): ...
    @provider_data.setter
    def provider_data(self, provider_data): ...
    @property
    def custom_claims(self): ...
    @custom_claims.setter
    def custom_claims(self, custom_claims): ...
    def to_dict(self):  # -> dict[str, Unknown | bool | str]:
        """Returns a dict representation of the user. For internal use only."""
        ...

class UserImportHash:
    """Represents a hash algorithm used to hash user passwords.

    An instance of this class must be specified when importing users with passwords via the
    ``auth.import_users()`` API. Use one of the provided class methods to obtain new
    instances when required. Refer to `documentation`_ for more details.

    .. _documentation: https://firebase.google.com/docs/auth/admin/import-users
    """

    def __init__(self, name, data=...) -> None: ...
    def to_dict(self): ...
    @classmethod
    def hmac_sha512(cls, key):  # -> UserImportHash:
        """Creates a new HMAC SHA512 algorithm instance.

        Args:
            key: Signer key as a byte sequence.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def hmac_sha256(cls, key):  # -> UserImportHash:
        """Creates a new HMAC SHA256 algorithm instance.

        Args:
            key: Signer key as a byte sequence.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def hmac_sha1(cls, key):  # -> UserImportHash:
        """Creates a new HMAC SHA1 algorithm instance.

        Args:
            key: Signer key as a byte sequence.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def hmac_md5(cls, key):  # -> UserImportHash:
        """Creates a new HMAC MD5 algorithm instance.

        Args:
            key: Signer key as a byte sequence.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def md5(cls, rounds):  # -> UserImportHash:
        """Creates a new MD5 algorithm instance.

        Args:
            rounds: Number of rounds. Must be an integer between 0 and 8192.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def sha1(cls, rounds):  # -> UserImportHash:
        """Creates a new SHA1 algorithm instance.

        Args:
            rounds: Number of rounds. Must be an integer between 1 and 8192.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def sha256(cls, rounds):  # -> UserImportHash:
        """Creates a new SHA256 algorithm instance.

        Args:
            rounds: Number of rounds. Must be an integer between 1 and 8192.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def sha512(cls, rounds):  # -> UserImportHash:
        """Creates a new SHA512 algorithm instance.

        Args:
            rounds: Number of rounds. Must be an integer between 1 and 8192.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def pbkdf_sha1(cls, rounds):  # -> UserImportHash:
        """Creates a new PBKDF SHA1 algorithm instance.

        Args:
            rounds: Number of rounds. Must be an integer between 0 and 120000.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def pbkdf2_sha256(cls, rounds):  # -> UserImportHash:
        """Creates a new PBKDF2 SHA256 algorithm instance.

        Args:
            rounds: Number of rounds. Must be an integer between 0 and 120000.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def scrypt(cls, key, rounds, memory_cost, salt_separator=...):  # -> UserImportHash:
        """Creates a new Scrypt algorithm instance.

        This is the modified Scrypt algorithm used by Firebase Auth. See ``standard_scrypt()``
        function for the standard Scrypt algorith,

        Args:
            key: Signer key as a byte sequence.
            rounds: Number of rounds. Must be an integer between 1 and 8.
            memory_cost: Memory cost as an integer between 1 and 14.
            salt_separator: Salt separator as a byte sequence (optional).

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def bcrypt(cls):  # -> UserImportHash:
        """Creates a new Bcrypt algorithm instance.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...
    @classmethod
    def standard_scrypt(
        cls, memory_cost, parallelization, block_size, derived_key_length
    ):  # -> UserImportHash:
        """Creates a new standard Scrypt algorithm instance.

        Args:
            memory_cost: Memory cost as a non-negaive integer.
            parallelization: Parallelization as a non-negative integer.
            block_size: Block size as a non-negative integer.
            derived_key_length: Derived key length as a non-negative integer.

        Returns:
            UserImportHash: A new ``UserImportHash``.
        """
        ...

class ErrorInfo:
    """Represents an error encountered while performing a batch operation such
    as importing users or deleting multiple user accounts.
    """

    def __init__(self, error) -> None: ...
    @property
    def index(self): ...
    @property
    def reason(self): ...

class UserImportResult:
    """Represents the result of a bulk user import operation.

    See ``auth.import_users()`` API for more details.
    """

    def __init__(self, result, total) -> None: ...
    @property
    def success_count(self):
        """Returns the number of users successfully imported."""
        ...
    @property
    def failure_count(self):  # -> int:
        """Returns the number of users that failed to be imported."""
        ...
    @property
    def errors(self):  # -> list[ErrorInfo]:
        """Returns a list of ``auth.ErrorInfo`` instances describing the errors encountered."""
        ...
