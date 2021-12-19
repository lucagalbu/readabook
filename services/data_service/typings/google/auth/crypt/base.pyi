"""
This type stub file was generated by pyright.
"""

import abc
import six

"""Base classes for cryptographic signers and verifiers."""
_JSON_FILE_PRIVATE_KEY = ...
_JSON_FILE_PRIVATE_KEY_ID = ...

@six.add_metaclass(abc.ABCMeta)
class Verifier:
    """Abstract base class for crytographic signature verifiers."""

    @abc.abstractmethod
    def verify(self, message, signature):
        """Verifies a message against a cryptographic signature.

        Args:
            message (Union[str, bytes]): The message to verify.
            signature (Union[str, bytes]): The cryptography signature to check.

        Returns:
            bool: True if message was signed by the private key associated
            with the public key that this object was constructed with.
        """
        ...

@six.add_metaclass(abc.ABCMeta)
class Signer:
    """Abstract base class for cryptographic signers."""

    @abc.abstractproperty
    def key_id(self):
        """Optional[str]: The key ID used to identify this private key."""
        ...
    @abc.abstractmethod
    def sign(self, message):
        """Signs a message.

        Args:
            message (Union[str, bytes]): The message to be signed.

        Returns:
            bytes: The signature of the message.
        """
        ...

@six.add_metaclass(abc.ABCMeta)
class FromServiceAccountMixin:
    """Mix-in to enable factory constructors for a Signer."""

    @abc.abstractmethod
    def from_string(cls, key, key_id=...):
        """Construct an Signer instance from a private key string.

        Args:
            key (str): Private key as a string.
            key_id (str): An optional key id used to identify the private key.

        Returns:
            google.auth.crypt.Signer: The constructed signer.

        Raises:
            ValueError: If the key cannot be parsed.
        """
        ...
    @classmethod
    def from_service_account_info(cls, info):
        """Creates a Signer instance instance from a dictionary containing
        service account info in Google format.

        Args:
            info (Mapping[str, str]): The service account info in Google
                format.

        Returns:
            google.auth.crypt.Signer: The constructed signer.

        Raises:
            ValueError: If the info is not in the expected format.
        """
        ...
    @classmethod
    def from_service_account_file(cls, filename):
        """Creates a Signer instance from a service account .json file
        in Google format.

        Args:
            filename (str): The path to the service account .json file.

        Returns:
            google.auth.crypt.Signer: The constructed signer.
        """
        ...
