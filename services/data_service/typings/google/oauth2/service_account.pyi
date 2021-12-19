"""
This type stub file was generated by pyright.
"""

from google.auth import _helpers, credentials

"""Service Accounts: JSON Web Token (JWT) Profile for OAuth 2.0

This module implements the JWT Profile for OAuth 2.0 Authorization Grants
as defined by `RFC 7523`_ with particular support for how this RFC is
implemented in Google's infrastructure. Google refers to these credentials
as *Service Accounts*.

Service accounts are used for server-to-server communication, such as
interactions between a web application server and a Google service. The
service account belongs to your application instead of to an individual end
user. In contrast to other OAuth 2.0 profiles, no users are involved and your
application "acts" as the service account.

Typically an application uses a service account when the application uses
Google APIs to work with its own data rather than a user's data. For example,
an application that uses Google Cloud Datastore for data persistence would use
a service account to authenticate its calls to the Google Cloud Datastore API.
However, an application that needs to access a user's Drive documents would
use the normal OAuth 2.0 profile.

Additionally, Google Apps domain administrators can grant service accounts
`domain-wide delegation`_ authority to access user data on behalf of users in
the domain.

This profile uses a JWT to acquire an OAuth 2.0 access token. The JWT is used
in place of the usual authorization token returned during the standard
OAuth 2.0 Authorization Code grant. The JWT is only used for this purpose, as
the acquired access token is used as the bearer token when making requests
using these credentials.

This profile differs from normal OAuth 2.0 profile because no user consent
step is required. The use of the private key allows this profile to assert
identity directly.

This profile also differs from the :mod:`google.auth.jwt` authentication
because the JWT credentials use the JWT directly as the bearer token. This
profile instead only uses the JWT to obtain an OAuth 2.0 access token. The
obtained OAuth 2.0 access token is used as the bearer token.

Domain-wide delegation
----------------------

Domain-wide delegation allows a service account to access user data on
behalf of any user in a Google Apps domain without consent from the user.
For example, an application that uses the Google Calendar API to add events to
the calendars of all users in a Google Apps domain would use a service account
to access the Google Calendar API on behalf of users.

The Google Apps administrator must explicitly authorize the service account to
do this. This authorization step is referred to as "delegating domain-wide
authority" to a service account.

You can use domain-wise delegation by creating a set of credentials with a
specific subject using :meth:`~Credentials.with_subject`.

.. _RFC 7523: https://tools.ietf.org/html/rfc7523
"""
_DEFAULT_TOKEN_LIFETIME_SECS = ...
_GOOGLE_OAUTH2_TOKEN_ENDPOINT = ...

class Credentials(
    credentials.Signing, credentials.Scoped, credentials.CredentialsWithQuotaProject
):
    """Service account credentials

    Usually, you'll create these credentials with one of the helper
    constructors. To create credentials using a Google service account
    private key JSON file::

        credentials = service_account.Credentials.from_service_account_file(
            'service-account.json')

    Or if you already have the service account file loaded::

        service_account_info = json.load(open('service_account.json'))
        credentials = service_account.Credentials.from_service_account_info(
            service_account_info)

    Both helper methods pass on arguments to the constructor, so you can
    specify additional scopes and a subject if necessary::

        credentials = service_account.Credentials.from_service_account_file(
            'service-account.json',
            scopes=['email'],
            subject='user@example.com')

    The credentials are considered immutable. If you want to modify the scopes
    or the subject used for delegation, use :meth:`with_scopes` or
    :meth:`with_subject`::

        scoped_credentials = credentials.with_scopes(['email'])
        delegated_credentials = credentials.with_subject(subject)

    To add a quota project, use :meth:`with_quota_project`::

        credentials = credentials.with_quota_project('myproject-123')
    """

    def __init__(
        self,
        signer,
        service_account_email,
        token_uri,
        scopes=...,
        default_scopes=...,
        subject=...,
        project_id=...,
        quota_project_id=...,
        additional_claims=...,
        always_use_jwt_access=...,
    ) -> None:
        """
        Args:
            signer (google.auth.crypt.Signer): The signer used to sign JWTs.
            service_account_email (str): The service account's email.
            scopes (Sequence[str]): User-defined scopes to request during the
                authorization grant.
            default_scopes (Sequence[str]): Default scopes passed by a
                Google client library. Use 'scopes' for user-defined scopes.
            token_uri (str): The OAuth 2.0 Token URI.
            subject (str): For domain-wide delegation, the email address of the
                user to for which to request delegated access.
            project_id  (str): Project ID associated with the service account
                credential.
            quota_project_id (Optional[str]): The project ID used for quota and
                billing.
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT assertion used in the authorization grant.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be always used.

        .. note:: Typically one of the helper constructors
            :meth:`from_service_account_file` or
            :meth:`from_service_account_info` are used instead of calling the
            constructor directly.
        """
        ...
    @classmethod
    def from_service_account_info(cls, info, **kwargs):  # -> Self@Credentials:
        """Creates a Credentials instance from parsed service account info.

        Args:
            info (Mapping[str, str]): The service account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.service_account.Credentials: The constructed
                credentials.

        Raises:
            ValueError: If the info is not in the expected format.
        """
        ...
    @classmethod
    def from_service_account_file(cls, filename, **kwargs):  # -> Self@Credentials:
        """Creates a Credentials instance from a service account json file.

        Args:
            filename (str): The path to the service account json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.service_account.Credentials: The constructed
                credentials.
        """
        ...
    @property
    def service_account_email(self):  # -> Unknown:
        """The service account email."""
        ...
    @property
    def project_id(self):  # -> Unknown:
        """Project ID associated with this credential."""
        ...
    @property
    def requires_scopes(self):  # -> bool:
        """Checks if the credentials requires scopes.

        Returns:
            bool: True if there are no scopes set otherwise False.
        """
        ...
    @_helpers.copy_docstring(credentials.Scoped)
    def with_scopes(self, scopes, default_scopes=...): ...
    def with_always_use_jwt_access(self, always_use_jwt_access):  # -> Self@Credentials:
        """Create a copy of these credentials with the specified always_use_jwt_access value.

        Args:
            always_use_jwt_access (bool): Whether always use self signed JWT or not.

        Returns:
            google.auth.service_account.Credentials: A new credentials
                instance.
        """
        ...
    def with_subject(self, subject):  # -> Self@Credentials:
        """Create a copy of these credentials with the specified subject.

        Args:
            subject (str): The subject claim.

        Returns:
            google.auth.service_account.Credentials: A new credentials
                instance.
        """
        ...
    def with_claims(self, additional_claims):  # -> Self@Credentials:
        """Returns a copy of these credentials with modified claims.

        Args:
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT payload. This will be merged with the current
                additional claims.

        Returns:
            google.auth.service_account.Credentials: A new credentials
                instance.
        """
        ...
    @_helpers.copy_docstring(credentials.CredentialsWithQuotaProject)
    def with_quota_project(self, quota_project_id): ...
    @_helpers.copy_docstring(credentials.Credentials)
    def refresh(self, request): ...
    @_helpers.copy_docstring(credentials.Signing)
    def sign_bytes(self, message): ...
    @property
    @_helpers.copy_docstring(credentials.Signing)
    def signer(self): ...
    @property
    @_helpers.copy_docstring(credentials.Signing)
    def signer_email(self): ...

class IDTokenCredentials(credentials.Signing, credentials.CredentialsWithQuotaProject):
    """Open ID Connect ID Token-based service account credentials.

    These credentials are largely similar to :class:`.Credentials`, but instead
    of using an OAuth 2.0 Access Token as the bearer token, they use an Open
    ID Connect ID Token as the bearer token. These credentials are useful when
    communicating to services that require ID Tokens and can not accept access
    tokens.

    Usually, you'll create these credentials with one of the helper
    constructors. To create credentials using a Google service account
    private key JSON file::

        credentials = (
            service_account.IDTokenCredentials.from_service_account_file(
                'service-account.json'))


    Or if you already have the service account file loaded::

        service_account_info = json.load(open('service_account.json'))
        credentials = (
            service_account.IDTokenCredentials.from_service_account_info(
                service_account_info))


    Both helper methods pass on arguments to the constructor, so you can
    specify additional scopes and a subject if necessary::

        credentials = (
            service_account.IDTokenCredentials.from_service_account_file(
                'service-account.json',
                scopes=['email'],
                subject='user@example.com'))


    The credentials are considered immutable. If you want to modify the scopes
    or the subject used for delegation, use :meth:`with_scopes` or
    :meth:`with_subject`::

        scoped_credentials = credentials.with_scopes(['email'])
        delegated_credentials = credentials.with_subject(subject)

    """

    def __init__(
        self,
        signer,
        service_account_email,
        token_uri,
        target_audience,
        additional_claims=...,
        quota_project_id=...,
    ) -> None:
        """
        Args:
            signer (google.auth.crypt.Signer): The signer used to sign JWTs.
            service_account_email (str): The service account's email.
            token_uri (str): The OAuth 2.0 Token URI.
            target_audience (str): The intended audience for these credentials,
                used when requesting the ID Token. The ID Token's ``aud`` claim
                will be set to this string.
            additional_claims (Mapping[str, str]): Any additional claims for
                the JWT assertion used in the authorization grant.
            quota_project_id (Optional[str]): The project ID used for quota and billing.
        .. note:: Typically one of the helper constructors
            :meth:`from_service_account_file` or
            :meth:`from_service_account_info` are used instead of calling the
            constructor directly.
        """
        ...
    @classmethod
    def from_service_account_info(cls, info, **kwargs):  # -> Self@IDTokenCredentials:
        """Creates a credentials instance from parsed service account info.

        Args:
            info (Mapping[str, str]): The service account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.service_account.IDTokenCredentials: The constructed
                credentials.

        Raises:
            ValueError: If the info is not in the expected format.
        """
        ...
    @classmethod
    def from_service_account_file(
        cls, filename, **kwargs
    ):  # -> Self@IDTokenCredentials:
        """Creates a credentials instance from a service account json file.

        Args:
            filename (str): The path to the service account json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.service_account.IDTokenCredentials: The constructed
                credentials.
        """
        ...
    def with_target_audience(self, target_audience):  # -> Self@IDTokenCredentials:
        """Create a copy of these credentials with the specified target
        audience.

        Args:
            target_audience (str): The intended audience for these credentials,
            used when requesting the ID Token.

        Returns:
            google.auth.service_account.IDTokenCredentials: A new credentials
                instance.
        """
        ...
    @_helpers.copy_docstring(credentials.CredentialsWithQuotaProject)
    def with_quota_project(self, quota_project_id): ...
    @_helpers.copy_docstring(credentials.Credentials)
    def refresh(self, request): ...
    @property
    def service_account_email(self):  # -> Unknown:
        """The service account email."""
        ...
    @_helpers.copy_docstring(credentials.Signing)
    def sign_bytes(self, message): ...
    @property
    @_helpers.copy_docstring(credentials.Signing)
    def signer(self): ...
    @property
    @_helpers.copy_docstring(credentials.Signing)
    def signer_email(self): ...
