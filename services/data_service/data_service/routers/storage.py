"""Module to create a router with the API endpoints of the data service"""
from __future__ import annotations
from typing import TYPE_CHECKING
from fastapi import APIRouter
from data_service.services.storage import StorageService

if TYPE_CHECKING:
    from data_service.daos.base import DaoBase


def make_router(dao: DaoBase):
    """Factory to create a router"""
    router: APIRouter = APIRouter()
    service = StorageService(dao=dao)

    return router
