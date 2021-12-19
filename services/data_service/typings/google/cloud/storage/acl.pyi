"""
This type stub file was generated by pyright.
"""

"""Manipulate access control lists that Cloud Storage provides.

:class:`google.cloud.storage.bucket.Bucket` has a getting method that creates
an ACL object under the hood, and you can interact with that using
:func:`google.cloud.storage.bucket.Bucket.acl`:

.. literalinclude:: snippets.py
    :start-after: [START client_bucket_acl]
    :end-before: [END client_bucket_acl]
    :dedent: 4


Adding and removing permissions can be done with the following methods
(in increasing order of granularity):

- :func:`ACL.all`
  corresponds to access for all users.
- :func:`ACL.all_authenticated` corresponds
  to access for all users that are signed into a Google account.
- :func:`ACL.domain` corresponds to access on a
  per Google Apps domain (ie, ``example.com``).
- :func:`ACL.group` corresponds to access on a
  per group basis (either by ID or e-mail address).
- :func:`ACL.user` corresponds to access on a
  per user basis (either by ID or e-mail address).

And you are able to ``grant`` and ``revoke`` the following roles:

- **Reading**:
  :func:`_ACLEntity.grant_read` and :func:`_ACLEntity.revoke_read`
- **Writing**:
  :func:`_ACLEntity.grant_write` and :func:`_ACLEntity.revoke_write`
- **Owning**:
  :func:`_ACLEntity.grant_owner` and :func:`_ACLEntity.revoke_owner`

You can use any of these like any other factory method (these happen to
be :class:`_ACLEntity` factories):

.. literalinclude:: snippets.py
   :start-after: [START acl_user_settings]
   :end-before: [END acl_user_settings]
   :dedent: 4

After that, you can save any changes you make with the
:func:`google.cloud.storage.acl.ACL.save` method:

.. literalinclude:: snippets.py
   :start-after: [START acl_save]
   :end-before: [END acl_save]
   :dedent: 4

You can alternatively save any existing :class:`google.cloud.storage.acl.ACL`
object (whether it was created by a factory method or not) from a
:class:`google.cloud.storage.bucket.Bucket`:

.. literalinclude:: snippets.py
   :start-after: [START acl_save_bucket]
   :end-before: [END acl_save_bucket]
   :dedent: 4

To get the list of ``entity`` and ``role`` for each unique pair, the
:class:`ACL` class is iterable:

.. literalinclude:: snippets.py
   :start-after: [START acl_print]
   :end-before: [END acl_print]
   :dedent: 4

This list of tuples can be used as the ``entity`` and ``role`` fields
when sending metadata for ACLs to the API.
"""

class _ACLEntity:
    """Class representing a set of roles for an entity.

    This is a helper class that you likely won't ever construct
    outside of using the factor methods on the :class:`ACL` object.

    :type entity_type: str
    :param entity_type: The type of entity (ie, 'group' or 'user').

    :type identifier: str
    :param identifier: (Optional) The ID or e-mail of the entity. For the special
                       entity types (like 'allUsers').
    """

    READER_ROLE = ...
    WRITER_ROLE = ...
    OWNER_ROLE = ...
    def __init__(self, entity_type, identifier=...) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self): ...
    def get_roles(self):  # -> set[Any]:
        """Get the list of roles permitted by this entity.

        :rtype: list of strings
        :returns: The list of roles associated with this entity.
        """
        ...
    def grant(self, role):  # -> None:
        """Add a role to the entity.

        :type role: str
        :param role: The role to add to the entity.
        """
        ...
    def revoke(self, role):  # -> None:
        """Remove a role from the entity.

        :type role: str
        :param role: The role to remove from the entity.
        """
        ...
    def grant_read(self):  # -> None:
        """Grant read access to the current entity."""
        ...
    def grant_write(self):  # -> None:
        """Grant write access to the current entity."""
        ...
    def grant_owner(self):  # -> None:
        """Grant owner access to the current entity."""
        ...
    def revoke_read(self):  # -> None:
        """Revoke read access from the current entity."""
        ...
    def revoke_write(self):  # -> None:
        """Revoke write access from the current entity."""
        ...
    def revoke_owner(self):  # -> None:
        """Revoke owner access from the current entity."""
        ...

class ACL:
    """Container class representing a list of access controls."""

    _URL_PATH_ELEM = ...
    _PREDEFINED_QUERY_PARAM = ...
    PREDEFINED_XML_ACLS = ...
    PREDEFINED_JSON_ACLS = ...
    loaded = ...
    client = ...
    reload_path = ...
    save_path = ...
    user_project = ...
    def __init__(self) -> None: ...
    @classmethod
    def validate_predefined(cls, predefined):  # -> str:
        """Ensures predefined is in list of predefined json values

        :type predefined: str
        :param predefined: name of a predefined acl

        :type predefined: str
        :param predefined: validated JSON name of predefined acl

        :raises: :exc: `ValueError`: If predefined is not a valid acl
        """
        ...
    def reset(self):  # -> None:
        """Remove all entities from the ACL, and clear the ``loaded`` flag."""
        ...
    def __iter__(self): ...
    def entity_from_dict(self, entity_dict):  # -> _ACLEntity:
        """Build an _ACLEntity object from a dictionary of data.

        An entity is a mutable object that represents a list of roles
        belonging to either a user or group or the special types for all
        users and all authenticated users.

        :type entity_dict: dict
        :param entity_dict: Dictionary full of data from an ACL lookup.

        :rtype: :class:`_ACLEntity`
        :returns: An Entity constructed from the dictionary.
        """
        ...
    def has_entity(self, entity):  # -> bool:
        """Returns whether or not this ACL has any entries for an entity.

        :type entity: :class:`_ACLEntity`
        :param entity: The entity to check for existence in this ACL.

        :rtype: bool
        :returns: True of the entity exists in the ACL.
        """
        ...
    def get_entity(self, entity, default=...):
        """Gets an entity object from the ACL.

        :type entity: :class:`_ACLEntity` or string
        :param entity: The entity to get lookup in the ACL.

        :type default: anything
        :param default: This value will be returned if the entity
                        doesn't exist.

        :rtype: :class:`_ACLEntity`
        :returns: The corresponding entity or the value provided
                  to ``default``.
        """
        ...
    def add_entity(self, entity):  # -> None:
        """Add an entity to the ACL.

        :type entity: :class:`_ACLEntity`
        :param entity: The entity to add to this ACL.
        """
        ...
    def entity(self, entity_type, identifier=...):  # -> _ACLEntity:
        """Factory method for creating an Entity.

        If an entity with the same type and identifier already exists,
        this will return a reference to that entity.  If not, it will
        create a new one and add it to the list of known entities for
        this ACL.

        :type entity_type: str
        :param entity_type: The type of entity to create
                            (ie, ``user``, ``group``, etc)

        :type identifier: str
        :param identifier: The ID of the entity (if applicable).
                           This can be either an ID or an e-mail address.

        :rtype: :class:`_ACLEntity`
        :returns: A new Entity or a reference to an existing identical entity.
        """
        ...
    def user(self, identifier):  # -> _ACLEntity:
        """Factory method for a user Entity.

        :type identifier: str
        :param identifier: An id or e-mail for this particular user.

        :rtype: :class:`_ACLEntity`
        :returns: An Entity corresponding to this user.
        """
        ...
    def group(self, identifier):  # -> _ACLEntity:
        """Factory method for a group Entity.

        :type identifier: str
        :param identifier: An id or e-mail for this particular group.

        :rtype: :class:`_ACLEntity`
        :returns: An Entity corresponding to this group.
        """
        ...
    def domain(self, domain):  # -> _ACLEntity:
        """Factory method for a domain Entity.

        :type domain: str
        :param domain: The domain for this entity.

        :rtype: :class:`_ACLEntity`
        :returns: An entity corresponding to this domain.
        """
        ...
    def all(self):  # -> _ACLEntity:
        """Factory method for an Entity representing all users.

        :rtype: :class:`_ACLEntity`
        :returns: An entity representing all users.
        """
        ...
    def all_authenticated(self):  # -> _ACLEntity:
        """Factory method for an Entity representing all authenticated users.

        :rtype: :class:`_ACLEntity`
        :returns: An entity representing all authenticated users.
        """
        ...
    def get_entities(self):  # -> list[Unknown]:
        """Get a list of all Entity objects.

        :rtype: list of :class:`_ACLEntity` objects
        :returns: A list of all Entity objects.
        """
        ...
    @property
    def client(self):
        """Abstract getter for the object client."""
        ...
    def reload(self, client=..., timeout=..., retry=...):  # -> None:
        """Reload the ACL data from Cloud Storage.

        If :attr:`user_project` is set, bills the API request to that project.

        :type client: :class:`~google.cloud.storage.client.Client` or
                      ``NoneType``
        :param client: (Optional) The client to use.  If not passed, falls back
                       to the ``client`` stored on the ACL's parent.
        :type timeout: float or tuple
        :param timeout:
            (Optional) The amount of time, in seconds, to wait
            for the server response.  See: :ref:`configuring_timeouts`

        :type retry: :class:`~google.api_core.retry.Retry`
        :param retry:
            (Optional) How to retry the RPC. See: :ref:`configuring_retries`
        """
        ...
    def save(
        self,
        acl=...,
        client=...,
        if_generation_match=...,
        if_generation_not_match=...,
        if_metageneration_match=...,
        if_metageneration_not_match=...,
        timeout=...,
        retry=...,
    ):  # -> None:
        """Save this ACL for the current bucket.

        If :attr:`user_project` is set, bills the API request to that project.

        :type acl: :class:`google.cloud.storage.acl.ACL`, or a compatible list.
        :param acl: The ACL object to save.  If left blank, this will save
                    current entries.

        :type client: :class:`~google.cloud.storage.client.Client` or
                      ``NoneType``
        :param client: (Optional) The client to use.  If not passed, falls back
                       to the ``client`` stored on the ACL's parent.

        :type if_generation_match: long
        :param if_generation_match:
            (Optional) See :ref:`using-if-generation-match`

        :type if_generation_not_match: long
        :param if_generation_not_match:
            (Optional) See :ref:`using-if-generation-not-match`

        :type if_metageneration_match: long
        :param if_metageneration_match:
            (Optional) See :ref:`using-if-metageneration-match`

        :type if_metageneration_not_match: long
        :param if_metageneration_not_match:
            (Optional) See :ref:`using-if-metageneration-not-match`

        :type timeout: float or tuple
        :param timeout:
            (Optional) The amount of time, in seconds, to wait
            for the server response.  See: :ref:`configuring_timeouts`

        :type retry: google.api_core.retry.Retry or google.cloud.storage.retry.ConditionalRetryPolicy
        :param retry:
            (Optional) How to retry the RPC. See: :ref:`configuring_retries`
        """
        ...
    def save_predefined(
        self,
        predefined,
        client=...,
        if_generation_match=...,
        if_generation_not_match=...,
        if_metageneration_match=...,
        if_metageneration_not_match=...,
        timeout=...,
        retry=...,
    ):  # -> None:
        """Save this ACL for the current bucket using a predefined ACL.

        If :attr:`user_project` is set, bills the API request to that project.

        :type predefined: str
        :param predefined: An identifier for a predefined ACL.  Must be one
                           of the keys in :attr:`PREDEFINED_JSON_ACLS`
                           or :attr:`PREDEFINED_XML_ACLS` (which will be
                           aliased to the corresponding JSON name).
                           If passed, `acl` must be None.

        :type client: :class:`~google.cloud.storage.client.Client` or
                      ``NoneType``
        :param client: (Optional) The client to use.  If not passed, falls back
                       to the ``client`` stored on the ACL's parent.

        :type if_generation_match: long
        :param if_generation_match:
            (Optional) See :ref:`using-if-generation-match`

        :type if_generation_not_match: long
        :param if_generation_not_match:
            (Optional) See :ref:`using-if-generation-not-match`

        :type if_metageneration_match: long
        :param if_metageneration_match:
            (Optional) See :ref:`using-if-metageneration-match`

        :type if_metageneration_not_match: long
        :param if_metageneration_not_match:
            (Optional) See :ref:`using-if-metageneration-not-match`

        :type timeout: float or tuple
        :param timeout:
            (Optional) The amount of time, in seconds, to wait
            for the server response.  See: :ref:`configuring_timeouts`

        :type retry: google.api_core.retry.Retry or google.cloud.storage.retry.ConditionalRetryPolicy
        :param retry:
            (Optional) How to retry the RPC. See: :ref:`configuring_retries`
        """
        ...
    def clear(
        self,
        client=...,
        if_generation_match=...,
        if_generation_not_match=...,
        if_metageneration_match=...,
        if_metageneration_not_match=...,
        timeout=...,
        retry=...,
    ):  # -> None:
        """Remove all ACL entries.

        If :attr:`user_project` is set, bills the API request to that project.

        Note that this won't actually remove *ALL* the rules, but it
        will remove all the non-default rules.  In short, you'll still
        have access to a bucket that you created even after you clear
        ACL rules with this method.

        :type client: :class:`~google.cloud.storage.client.Client` or
                      ``NoneType``
        :param client: (Optional) The client to use.  If not passed, falls back
                       to the ``client`` stored on the ACL's parent.

        :type if_generation_match: long
        :param if_generation_match:
            (Optional) See :ref:`using-if-generation-match`

        :type if_generation_not_match: long
        :param if_generation_not_match:
            (Optional) See :ref:`using-if-generation-not-match`

        :type if_metageneration_match: long
        :param if_metageneration_match:
            (Optional) See :ref:`using-if-metageneration-match`

        :type if_metageneration_not_match: long
        :param if_metageneration_not_match:
            (Optional) See :ref:`using-if-metageneration-not-match`

        :type timeout: float or tuple
        :param timeout:
            (Optional) The amount of time, in seconds, to wait
            for the server response.  See: :ref:`configuring_timeouts`

        :type retry: google.api_core.retry.Retry or google.cloud.storage.retry.ConditionalRetryPolicy
        :param retry:
            (Optional) How to retry the RPC. See: :ref:`configuring_retries`
        """
        ...

class BucketACL(ACL):
    """An ACL specifically for a bucket.

    :type bucket: :class:`google.cloud.storage.bucket.Bucket`
    :param bucket: The bucket to which this ACL relates.
    """

    def __init__(self, bucket) -> None: ...
    @property
    def client(self):
        """The client bound to this ACL's bucket."""
        ...
    @property
    def reload_path(self):  # -> str:
        """Compute the path for GET API requests for this ACL."""
        ...
    @property
    def save_path(self):
        """Compute the path for PATCH API requests for this ACL."""
        ...
    @property
    def user_project(self):
        """Compute the user project charged for API requests for this ACL."""
        ...

class DefaultObjectACL(BucketACL):
    """A class representing the default object ACL for a bucket."""

    _URL_PATH_ELEM = ...
    _PREDEFINED_QUERY_PARAM = ...

class ObjectACL(ACL):
    """An ACL specifically for a Cloud Storage object / blob.

    :type blob: :class:`google.cloud.storage.blob.Blob`
    :param blob: The blob that this ACL corresponds to.
    """

    def __init__(self, blob) -> None: ...
    @property
    def client(self):
        """The client bound to this ACL's blob."""
        ...
    @property
    def reload_path(self):
        """Compute the path for GET API requests for this ACL."""
        ...
    @property
    def save_path(self):
        """Compute the path for PATCH API requests for this ACL."""
        ...
    @property
    def user_project(self):
        """Compute the user project charged for API requests for this ACL."""
        ...