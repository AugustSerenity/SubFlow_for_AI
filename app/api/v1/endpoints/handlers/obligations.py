from fastapi import APIRouter, Depends

from app.schemas.obligation import ObligationsRequest, ObligationsResponse
from app.service.obligation import ObligationService
from app.db.depends import get_obligation_service

router = APIRouter()

@router.post("/obligations", response_model=ObligationsResponse, tags=["obligations"])
async def create_obligation(
    obligations_data: ObligationsRequest,
    service: ObligationService = Depends(get_obligation_service)
):
    return await service.create(obligations_data)