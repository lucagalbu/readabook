"""Module to create a router with the API endpoints of the data service"""
import time
from fastapi import HTTPException, File, Form, UploadFile
from fastapi.routing import APIRouter
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_501_NOT_IMPLEMENTED,
)
from data_service.daos.base import DaoBase
from data_service.services.storage import StorageService
from data_service.typings.book_info import BookInfo


def make_router(dao: DaoBase):
    """Factory function to create a fastAPI router"""
    router: APIRouter = APIRouter()
    service = StorageService(dao=dao)

    @router.post(
        "/upload", tags=["file"], status_code=HTTP_201_CREATED, response_model=None
    )
    async def upload_file(
        title: str = Form(...), author: str = Form(...), file: UploadFile = File(...)
    ):  # pyright: reportUnusedFunction=false
        content = await file.read()
        content_type = file.content_type

        book_info = BookInfo(title=title, author=author, timestamp=time.time())

        try:
            service.upload(book_info, content_type=content_type, content=content)
        except NotImplementedError as err:
            raise HTTPException(
                status_code=HTTP_501_NOT_IMPLEMENTED, detail=str(err)
            ) from err
        except Exception as err:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                detail="The server encountered a problem while uploading the content.",
            ) from err

    return router
