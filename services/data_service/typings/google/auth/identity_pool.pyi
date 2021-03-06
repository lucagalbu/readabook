"""
This type stub file was generated by pyright.
"""

from google.auth import _helpers, external_account

"""Identity Pool Credentials.

This module provides credentials to access Google Cloud resources from on-prem
or non-Google Cloud platforms which support external credentials (e.g. OIDC ID
tokens) retrieved from local file locations or local servers. This includes
Microsoft Azure and OIDC identity providers (e.g. K8s workloads registered with
Hub with Hub workload identity enabled).

These credentials are recommended over the use of service account credentials
in on-prem/non-Google Cloud platforms as they do not involve the management of
long-live service account private keys.

Identity Pool Credentials are initialized using external_account
arguments which are typically loaded from an external credentials file or
an external credentials URL. Unlike other Credentials that can be initialized
with a list of explicit arguments, secrets or credentials, external account
clients use the environment and hints/guidelines provided by the
external_account JSON file to retrieve credentials and exchange them for Google
access tokens.
"""

class Credentials(external_account.Credentials):
    """External account credentials sourced from files and URLs."""

    def __init__(
        self,
        audience,
        subject_token_type,
        token_url,
        credential_source,
        service_account_impersonation_url=...,
        client_id=...,
        client_secret=...,
        quota_project_id=...,
        scopes=...,
        default_scopes=...,
        workforce_pool_user_project=...,
    ) -> None:
        """Instantiates an external account credentials object from a file/URL.

        Args:
            audience (str): The STS audience field.
            subject_token_type (str): The subject token type.
            token_url (str): The STS endpoint URL.
            credential_source (Mapping): The credential source dictionary used to
                provide instructions on how to retrieve external credential to be
                exchanged for Google access tokens.

                Example credential_source for url-sourced credential::

                    {
                        "url": "http://www.example.com",
                        "format": {
                            "type": "json",
                            "subject_token_field_name": "access_token",
                        },
                        "headers": {"foo": "bar"},
                    }

                Example credential_source for file-sourced credential::

                    {
                        "file": "/path/to/token/file.txt"
                    }

            service_account_impersonation_url (Optional[str]): The optional service account
                impersonation getAccessToken URL.
            client_id (Optional[str]): The optional client ID.
            client_secret (Optional[str]): The optional client secret.
            quota_project_id (Optional[str]): The optional quota project ID.
            scopes (Optional[Sequence[str]]): Optional scopes to request during the
                authorization grant.
            default_scopes (Optional[Sequence[str]]): Default scopes passed by a
                Google client library. Use 'scopes' for user-defined scopes.
            workforce_pool_user_project (Optona[str]): The optional workforce pool user
                project number when the credential corresponds to a workforce pool and not
                a workload identity pool. The underlying principal must still have
                serviceusage.services.use IAM permission to use the project for
                billing/quota.

        Raises:
            google.auth.exceptions.RefreshError: If an error is encountered during
                access token retrieval logic.
            ValueError: For invalid parameters.

        .. note:: Typically one of the helper constructors
            :meth:`from_file` or
            :meth:`from_info` are used instead of calling the constructor directly.
        """
        ...
    @_helpers.copy_docstring(external_account.Credentials)
    def retrieve_subject_token(self, request): ...
    @classmethod
    def from_info(cls, info, **kwargs):  # -> Self@Credentials:
        """Creates an Identity Pool Credentials instance from parsed external account info.

        Args:
            info (Mapping[str, str]): The Identity Pool external account info in Google
                format.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.identity_pool.Credentials: The constructed
                credentials.

        Raises:
            ValueError: For invalid parameters.
        """
        ...
    @classmethod
    def from_file(cls, filename, **kwargs):  # -> Self@Credentials:
        """Creates an IdentityPool Credentials instance from an external account json file.

        Args:
            filename (str): The path to the IdentityPool external account json file.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            google.auth.identity_pool.Credentials: The constructed
                credentials.
        """
        ...
