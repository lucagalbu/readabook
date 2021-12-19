"""
This type stub file was generated by pyright.
"""

import abc
import six
from six.moves import http_client

"""Transport - HTTP client library support.

:mod:`google.auth` is designed to work with various HTTP client libraries such
as urllib3 and requests. In order to work across these libraries with different
interfaces some abstraction is needed.

This module provides two interfaces that are implemented by transport adapters
to support HTTP libraries. :class:`Request` defines the interface expected by
:mod:`google.auth` to make requests. :class:`Response` defines the interface
for the return value of :class:`Request`.
"""
DEFAULT_REFRESH_STATUS_CODES = ...
DEFAULT_MAX_REFRESH_ATTEMPTS = ...

@six.add_metaclass(abc.ABCMeta)
class Response:
    """HTTP Response data."""

    @abc.abstractproperty
    def status(self):
        """int: The HTTP status code."""
        ...
    @abc.abstractproperty
    def headers(self):
        """Mapping[str, str]: The HTTP response headers."""
        ...
    @abc.abstractproperty
    def data(self):
        """bytes: The response body."""
        ...

@six.add_metaclass(abc.ABCMeta)
class Request:
    """Interface for a callable that makes HTTP requests.

    Specific transport implementations should provide an implementation of
    this that adapts their specific request / response API.

    .. automethod:: __call__
    """

    @abc.abstractmethod
    def __call__(self, url, method=..., body=..., headers=..., timeout=..., **kwargs):
        """Make an HTTP request.

        Args:
            url (str): The URI to be requested.
            method (str): The HTTP method to use for the request. Defaults
                to 'GET'.
            body (bytes): The payload / body in HTTP request.
            headers (Mapping[str, str]): Request headers.
            timeout (Optional[int]): The number of seconds to wait for a
                response from the server. If not specified or if None, the
                transport-specific default timeout will be used.
            kwargs: Additionally arguments passed on to the transport's
                request method.

        Returns:
            Response: The HTTP response.

        Raises:
            google.auth.exceptions.TransportError: If any exception occurred.
        """
        ...
