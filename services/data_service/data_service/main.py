"""Main entrypoint of the FastApi application"""
from fastapi import FastAPI
from dotenv import load_dotenv

from data_service.routers import storage
from data_service.daos.firebase import FirebaseDao

# Load evironment variables
load_dotenv("../.env", override=True)

# Set up FastAPI
app = FastAPI()

storage_dao = FirebaseDao()
storage_router = storage.make_router(storage_dao)
app.include_router(storage_router)
