"""
This type stub file was generated by pyright.
"""

"""Firebase Cloud Messaging module."""
_MESSAGING_ATTRIBUTE = ...
__all__ = [
    "AndroidConfig",
    "AndroidFCMOptions",
    "AndroidNotification",
    "APNSConfig",
    "APNSFCMOptions",
    "APNSPayload",
    "Aps",
    "ApsAlert",
    "BatchResponse",
    "CriticalSound",
    "ErrorInfo",
    "FCMOptions",
    "LightSettings",
    "Message",
    "MulticastMessage",
    "Notification",
    "QuotaExceededError",
    "SenderIdMismatchError",
    "SendResponse",
    "ThirdPartyAuthError",
    "TopicManagementResponse",
    "UnregisteredError",
    "WebpushConfig",
    "WebpushFCMOptions",
    "WebpushNotification",
    "WebpushNotificationAction",
    "send",
    "send_all",
    "send_multicast",
    "subscribe_to_topic",
    "unsubscribe_from_topic",
]
AndroidConfig = ...
AndroidFCMOptions = ...
AndroidNotification = ...
APNSConfig = ...
APNSFCMOptions = ...
APNSPayload = ...
Aps = ...
ApsAlert = ...
CriticalSound = ...
FCMOptions = ...
LightSettings = ...
Message = ...
MulticastMessage = ...
Notification = ...
WebpushConfig = ...
WebpushFCMOptions = ...
WebpushNotification = ...
WebpushNotificationAction = ...
QuotaExceededError = ...
SenderIdMismatchError = ...
ThirdPartyAuthError = ...
UnregisteredError = ...

def send(message, dry_run=..., app=...):
    """Sends the given message via Firebase Cloud Messaging (FCM).

    If the ``dry_run`` mode is enabled, the message will not be actually delivered to the
    recipients. Instead FCM performs all the usual validations, and emulates the send operation.

    Args:
        message: An instance of ``messaging.Message``.
        dry_run: A boolean indicating whether to run the operation in dry run mode (optional).
        app: An App instance (optional).

    Returns:
        string: A message ID string that uniquely identifies the sent message.

    Raises:
        FirebaseError: If an error occurs while sending the message to the FCM service.
        ValueError: If the input arguments are invalid.
    """
    ...

def send_all(messages, dry_run=..., app=...):
    """Sends the given list of messages via Firebase Cloud Messaging as a single batch.

    If the ``dry_run`` mode is enabled, the message will not be actually delivered to the
    recipients. Instead FCM performs all the usual validations, and emulates the send operation.

    Args:
        messages: A list of ``messaging.Message`` instances.
        dry_run: A boolean indicating whether to run the operation in dry run mode (optional).
        app: An App instance (optional).

    Returns:
        BatchResponse: A ``messaging.BatchResponse`` instance.

    Raises:
        FirebaseError: If an error occurs while sending the message to the FCM service.
        ValueError: If the input arguments are invalid.
    """
    ...

def send_multicast(multicast_message, dry_run=..., app=...):
    """Sends the given mutlicast message to all tokens via Firebase Cloud Messaging (FCM).

    If the ``dry_run`` mode is enabled, the message will not be actually delivered to the
    recipients. Instead FCM performs all the usual validations, and emulates the send operation.

    Args:
        multicast_message: An instance of ``messaging.MulticastMessage``.
        dry_run: A boolean indicating whether to run the operation in dry run mode (optional).
        app: An App instance (optional).

    Returns:
        BatchResponse: A ``messaging.BatchResponse`` instance.

    Raises:
        FirebaseError: If an error occurs while sending the message to the FCM service.
        ValueError: If the input arguments are invalid.
    """
    ...

def subscribe_to_topic(tokens, topic, app=...):
    """Subscribes a list of registration tokens to an FCM topic.

    Args:
        tokens: A non-empty list of device registration tokens. List may not have more than 1000
            elements.
        topic: Name of the topic to subscribe to. May contain the ``/topics/`` prefix.
        app: An App instance (optional).

    Returns:
        TopicManagementResponse: A ``TopicManagementResponse`` instance.

    Raises:
        FirebaseError: If an error occurs while communicating with instance ID service.
        ValueError: If the input arguments are invalid.
    """
    ...

def unsubscribe_from_topic(tokens, topic, app=...):
    """Unsubscribes a list of registration tokens from an FCM topic.

    Args:
        tokens: A non-empty list of device registration tokens. List may not have more than 1000
            elements.
        topic: Name of the topic to unsubscribe from. May contain the ``/topics/`` prefix.
        app: An App instance (optional).

    Returns:
        TopicManagementResponse: A ``TopicManagementResponse`` instance.

    Raises:
        FirebaseError: If an error occurs while communicating with instance ID service.
        ValueError: If the input arguments are invalid.
    """
    ...

class ErrorInfo:
    """An error encountered when performing a topic management operation."""

    def __init__(self, index, reason) -> None: ...
    @property
    def index(self):
        """Index of the registration token to which this error is related to."""
        ...
    @property
    def reason(self):
        """String describing the nature of the error."""
        ...

class TopicManagementResponse:
    """The response received from a topic management operation."""

    def __init__(self, resp) -> None: ...
    @property
    def success_count(self):  # -> int:
        """Number of tokens that were successfully subscribed or unsubscribed."""
        ...
    @property
    def failure_count(self):  # -> int:
        """Number of tokens that could not be subscribed or unsubscribed due to errors."""
        ...
    @property
    def errors(self):  # -> list[Unknown]:
        """A list of ``messaging.ErrorInfo`` objects (possibly empty)."""
        ...

class BatchResponse:
    """The response received from a batch request to the FCM API."""

    def __init__(self, responses) -> None: ...
    @property
    def responses(self):
        """A list of ``messaging.SendResponse`` objects (possibly empty)."""
        ...
    @property
    def success_count(self): ...
    @property
    def failure_count(self): ...

class SendResponse:
    """The response received from an individual batched request to the FCM API."""

    def __init__(self, resp, exception) -> None: ...
    @property
    def message_id(self):  # -> None:
        """A message ID string that uniquely identifies the message."""
        ...
    @property
    def success(self):  # -> bool:
        """A boolean indicating if the request was successful."""
        ...
    @property
    def exception(self):
        """A ``FirebaseError`` if an error occurs while sending the message to the FCM service."""
        ...

class _MessagingService:
    """Service class that implements Firebase Cloud Messaging (FCM) functionality."""

    FCM_URL = ...
    FCM_BATCH_URL = ...
    IID_URL = ...
    IID_HEADERS = ...
    JSON_ENCODER = ...
    FCM_ERROR_TYPES = ...
    def __init__(self, app) -> None: ...
    @classmethod
    def encode_message(cls, message): ...
    def send(self, message, dry_run=...):
        """Sends the given message to FCM via the FCM v1 API."""
        ...
    def send_all(self, messages, dry_run=...):  # -> BatchResponse:
        """Sends the given messages to FCM via the batch API."""
        ...
    def make_topic_management_request(self, tokens, topic, operation):
        """Invokes the IID service for topic management functionality."""
        ...
