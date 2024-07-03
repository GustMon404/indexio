from fastapi import FastAPI
from app.routers.document.views import router
from app.config import db_lifespan

app = FastAPI(lifespan=db_lifespan)

app.include_router(router)
