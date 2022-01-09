"""Module to create a router with the API endpoints of the data service"""
from fastapi.routing import APIRouter
from data_service.daos.base import DaoBase

# pylint: disable=unused-argument
def make_router(dao: DaoBase):
    """Factory function to create a fastAPI router"""
    router: APIRouter = APIRouter()

    return router
