"""Module to create a router with the API endpoints of the data service"""
from __future__ import annotations
from typing import TYPE_CHECKING
from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_501_NOT_IMPLEMENTED,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from google.api_core.exceptions import NotFound
from data_service.services.storage import StorageService

if TYPE_CHECKING:
    from data_service.daos.base import DaoBase


def make_router(dao: DaoBase):
    """Factory to create a router"""
    router: APIRouter = APIRouter()
    service = StorageService(dao=dao)

    @router.post("/upload", tags=["file"], status_code=HTTP_201_CREATED)
    async def upload_file(file: UploadFile = File(...)):  # type: ignore
        content = await file.read()
        content_type = file.content_type
        filename = file.filename

        try:
            service.upload(content, filename, content_type)
        except NotImplementedError as err:
            raise HTTPException(
                status_code=HTTP_501_NOT_IMPLEMENTED, detail=str(err)
            ) from err
        except NotFound as err:
            raise HTTPException(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                detail="The server encountered a problem in uploading the content.",
            ) from err

    @router.delete("/delete", tags=["file"], status_code=HTTP_204_NO_CONTENT)
    def delete_file(filename: str):  # type: ignore
        service.delete_file(filename)

    return router
