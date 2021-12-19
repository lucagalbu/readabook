import typing

class UploadFile:
    """
    An uploaded file included as part of the request data.
    """

    spool_max_size: int = ...
    filename: str
    content_type: str
    async def read(self, size: int = ...) -> typing.Union[bytes, str]: ...
