from fastapi import FastAPI
from app.routers.document.views import router

app = FastAPI()

app.include_router(router)
