"""
This type stub file was generated by pyright.
"""

from google.resumable_media.common import (
    DataCorruption,
    InvalidResponse,
    PERMANENT_REDIRECT,
    RetryStrategy,
    TOO_MANY_REQUESTS,
    UPLOAD_CHUNK_SIZE,
)

"""Utilities for Google Media Downloads and Resumable Uploads.

This package has some general purposes modules, e.g.
:mod:`~google.resumable_media.common`, but the majority of the
public interface will be contained in subpackages.

===========
Subpackages
===========

Each subpackage is tailored to a specific transport library:

* the :mod:`~google.resumable_media.requests` subpackage uses the ``requests``
  transport library.

.. _requests: http://docs.python-requests.org/

==========
Installing
==========

To install with `pip`_:

.. code-block:: console

  $ pip install --upgrade google-resumable-media

.. _pip: https://pip.pypa.io/
"""
__all__ = [
    "DataCorruption",
    "InvalidResponse",
    "PERMANENT_REDIRECT",
    "RetryStrategy",
    "TOO_MANY_REQUESTS",
    "UPLOAD_CHUNK_SIZE",
]
