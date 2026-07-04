from fastapi import APIRouter, Depends

from app.schemas.obligation import ObligationsRequest, ObligationsResponse
from app.service.obligation import ObligationService
from app.api.deps import get_obligation_service

router = APIRouter()




@router.post("/obligations", response_model=ObligationsResponse, tags=["obligations"])
async def create_obligation(
    obligations_data: ObligationsRequest,
    service: ObligationService = Depends(create_service)
):
    result = await service.create_obligation(obligations_data)
    return result