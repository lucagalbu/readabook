"""Business logic of the data service"""
from data_service.daos.base import DaoBase


class StorageService:
    """Class that implements the business logic"""

    dao: DaoBase

    def __init__(self, dao: DaoBase):
        self.dao = dao
