import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo.errors import ConnectionFailure
from contextlib import asynccontextmanager
from logging import info
from fastapi import FastAPI

# load .env
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
load_dotenv(dotenv_path)

MONGODB_URL = os.environ['MONGODB_URL']
MONGODB_NAME = os.environ['DB_NAME']


class Database:
    client: AsyncIOMotorClient
    db: AsyncIOMotorDatabase

    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient(MONGODB_URL)
        cls.db = cls.client.get_database(MONGODB_NAME)

    @classmethod
    async def ping(cls):
        try:
            cls.client.admin.command("ping")
            return True
        except ConnectionFailure:
            return False

    @classmethod
    async def close(cls):
        cls.client.close()


database = Database()


@asynccontextmanager
async def db_lifespan(app: FastAPI):
    # Startup
    await Database.connect()
    ping_response = await Database.ping()
    if not ping_response:
        raise Exception("Problem connecting to database cluster.")
    else:
        info("Connected to database cluster.")

    yield

    # Shutdown
    await Database.close()
