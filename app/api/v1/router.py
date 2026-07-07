from fastapi import APIRouter
from app.api.v1.endpoints.handlers import obligations as obl

api_router = APIRouter(prefix="/v1")

api_router.include_router(
    obl.router,
    prefix="/obligations",
    tags=["obligations"]
)