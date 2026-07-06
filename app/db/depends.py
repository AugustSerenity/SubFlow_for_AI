from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.repository.obligations import ObligationRepository
from app.service.obligation import ObligationService

def get_obligation_repository(
    session: AsyncSession = Depends(get_db),
) -> ObligationRepository:
    return ObligationRepository(session)

def get_obligation_service(
    repository: ObligationRepository = Depends(get_obligation_repository),
) -> ObligationService:
    return ObligationService(repository)