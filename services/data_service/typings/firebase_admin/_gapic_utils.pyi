"""
This type stub file was generated by pyright.
"""

"""Internal utilities for interacting with Google API client."""

def handle_platform_error_from_googleapiclient(error, handle_func=...):
    """Constructs a ``FirebaseError`` from the given googleapiclient error.

    This can be used to handle errors returned by Google Cloud Platform (GCP) APIs.

    Args:
        error: An error raised by the googleapiclient while making an HTTP call to a GCP API.
        handle_func: A function that can be used to handle platform errors in a custom way. When
            specified, this function will be called with three arguments. It has the same
            signature as ```_handle_func_googleapiclient``, but may return ``None``.

    Returns:
        FirebaseError: A ``FirebaseError`` that can be raised to the user code.
    """
    ...

def handle_googleapiclient_error(error, message=..., code=..., http_response=...):
    """Constructs a ``FirebaseError`` from the given googleapiclient error.

    This method is agnostic of the remote service that produced the error, whether it is a GCP
    service or otherwise. Therefore, this method does not attempt to parse the error response in
    any way.

    Args:
        error: An error raised by the googleapiclient module while making an HTTP call.
        message: A message to be included in the resulting ``FirebaseError`` (optional). If not
            specified the string representation of the ``error`` argument is used as the message.
        code: A GCP error code that will be used to determine the resulting error type (optional).
            If not specified the HTTP status code on the error response is used to determine a
            suitable error code.
        http_response: A requests HTTP response object to associate with the exception (optional).
            If not specified, one will be created from the ``error``.

    Returns:
        FirebaseError: A ``FirebaseError`` that can be raised to the user code.
    """
    ...
