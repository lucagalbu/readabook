"""Main entrypoint of the FastApi application"""
from fastapi import FastAPI
from dotenv import load_dotenv

from data_service.routers import storage
from data_service.daos.firebase import FirebaseDao, FirebaseClient

# Load evironment variables
load_dotenv("../.env", override=True)

# Set up FastAPI
app = FastAPI()

firebase_client = FirebaseClient()
storage_dao = FirebaseDao(firebase_client=firebase_client)
storage_router = storage.make_router(storage_dao)
app.include_router(storage_router)
