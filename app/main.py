from fastapi import FastAPI, APIRouter
from app.api import user_router
from .log_config import setup_logging

app = FastAPI(
    title="UpTimeRebotClone",
    version="1.0.0"
)

setup_logging()

router = APIRouter()
@router.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(user_router)
app.include_router(router)