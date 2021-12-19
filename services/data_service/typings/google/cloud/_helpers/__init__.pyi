"""
This type stub file was generated by pyright.
"""

import calendar
import datetime
import http.client
import os
import re
import google.auth
import google.auth.transport.requests
from __future__ import absolute_import
from threading import local as Local
from typing import Union
from google.protobuf import duration_pb2, timestamp_pb2

"""Shared helpers for Google Cloud packages.

This module is not part of the public API surface.
"""
_NOW = ...
UTC = ...
_EPOCH = ...
_RFC3339_MICROS = ...
_RFC3339_NO_FRACTION = ...
_TIMEONLY_W_MICROS = ...
_TIMEONLY_NO_FRACTION = ...
_RFC3339_NANOS = ...
_USER_ROOT: Union[str, None]
_GCLOUD_CONFIG_FILE = ...
_GCLOUD_CONFIG_SECTION = ...
_GCLOUD_CONFIG_KEY = ...

class _LocalStack(Local):
    """Manage a thread-local LIFO stack of resources.

    Intended for use in :class:`google.cloud.datastore.batch.Batch.__enter__`,
    :class:`google.cloud.storage.batch.Batch.__enter__`, etc.
    """

    def __init__(self) -> None: ...
    def __iter__(self):
        """Iterate the stack in LIFO order."""
        ...
    def push(self, resource):
        """Push a resource onto our stack."""
        ...
    def pop(self):
        """Pop a resource from our stack.

        :rtype: object
        :returns: the top-most resource, after removing it.
        :raises IndexError: if the stack is empty.
        """
        ...
    @property
    def top(self):
        """Get the top-most resource

        :rtype: object
        :returns: the top-most item, or None if the stack is empty.
        """
        ...

def make_secure_channel(credentials, user_agent, host, extra_options=...):
    """Makes a secure channel for an RPC service.

    Uses / depends on gRPC.

    :type credentials: :class:`google.auth.credentials.Credentials`
    :param credentials: The OAuth2 Credentials to use for creating
                        access tokens.

    :type user_agent: str
    :param user_agent: The user agent to be used with API requests.

    :type host: str
    :param host: The host for the service.

    :type extra_options: tuple
    :param extra_options: (Optional) Extra gRPC options used when creating the
                          channel.

    :rtype: :class:`grpc._channel.Channel`
    :returns: gRPC secure channel with credentials attached.
    """
    ...

def make_secure_stub(credentials, user_agent, stub_class, host, extra_options=...):
    """Makes a secure stub for an RPC service.

    Uses / depends on gRPC.

    :type credentials: :class:`google.auth.credentials.Credentials`
    :param credentials: The OAuth2 Credentials to use for creating
                        access tokens.

    :type user_agent: str
    :param user_agent: The user agent to be used with API requests.

    :type stub_class: type
    :param stub_class: A gRPC stub type for a given service.

    :type host: str
    :param host: The host for the service.

    :type extra_options: tuple
    :param extra_options: (Optional) Extra gRPC options passed when creating
                          the channel.

    :rtype: object, instance of ``stub_class``
    :returns: The stub object used to make gRPC requests to a given API.
    """
    ...

def make_insecure_stub(stub_class, host, port=...):
    """Makes an insecure stub for an RPC service.

    Uses / depends on gRPC.

    :type stub_class: type
    :param stub_class: A gRPC stub type for a given service.

    :type host: str
    :param host: The host for the service. May also include the port
                 if ``port`` is unspecified.

    :type port: int
    :param port: (Optional) The port for the service.

    :rtype: object, instance of ``stub_class``
    :returns: The stub object used to make gRPC requests to a given API.
    """
    ...