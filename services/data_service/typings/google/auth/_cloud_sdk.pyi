"""
This type stub file was generated by pyright.
"""

"""Helpers for reading the Google Cloud SDK's configuration."""
_CONFIG_DIRECTORY = ...
_WINDOWS_CONFIG_ROOT_ENV_VAR = ...
_CREDENTIALS_FILENAME = ...
_CLOUD_SDK_POSIX_COMMAND = ...
_CLOUD_SDK_WINDOWS_COMMAND = ...
_CLOUD_SDK_CONFIG_COMMAND = ...
_CLOUD_SDK_USER_ACCESS_TOKEN_COMMAND = ...
CLOUD_SDK_CLIENT_ID = ...

def get_config_path():  # -> str:
    """Returns the absolute path the the Cloud SDK's configuration directory.

    Returns:
        str: The Cloud SDK config path.
    """
    ...

def get_application_default_credentials_path():  # -> str:
    """Gets the path to the application default credentials file.

    The path may or may not exist.

    Returns:
        str: The full path to application default credentials.
    """
    ...

def get_project_id():  # -> Any | None:
    """Gets the project ID from the Cloud SDK.

    Returns:
        Optional[str]: The project ID.
    """
    ...

def get_auth_access_token(account=...):  # -> str:
    """Load user access token with the ``gcloud auth print-access-token`` command.

    Args:
        account (Optional[str]): Account to get the access token for. If not
            specified, the current active account will be used.

    Returns:
        str: The user access token.

    Raises:
        google.auth.exceptions.UserAccessTokenError: if failed to get access
            token from gcloud.
    """
    ...
