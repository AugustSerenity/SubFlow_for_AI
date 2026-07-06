from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.model import Obligation
from app.domain.enums import StatusType
from sqlalchemy import select, func
from app.models.db_models import ObligationORM


class ObligationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_active_by_title(
            self,
            title: str,
    ) -> Obligation | None:
        stmt = (
            select(ObligationORM)
            .where(
                func.lower(ObligationORM.title) == title.lower(),
                ObligationORM.status == StatusType.ACTIVE,
            )
        )

        result = await self.session.execute(stmt)

        orm = result.scalar_one_or_none()

        if orm is None:
            return None

        return self._to_domain(orm)

    async def create_obligation(
            self,
            obligation: Obligation,
        ) -> Obligation:
        orm = self._to_orm(obligation)

        self.session.add(orm)

        await self.session.commit()
        await self.session.refresh(orm)

        return self._to_domain(orm)

    def _to_domain(
            self,
            orm: ObligationORM,
    ) -> Obligation:

        return Obligation(
            id=orm.id,
            title=orm.title,
            amount=orm.amount,
            currency=orm.currency,
            category=orm.category,
            recurrence=orm.recurrence,
            next_payment_date=orm.next_payment_date,
            status=orm.status,
        )

    def _to_orm(
            self,
            domain: Obligation,
    ) -> ObligationORM:

        return ObligationORM(
            title=domain.title,
            amount=domain.amount,
            currency=domain.currency,
            category=domain.category,
            recurrence=domain.recurrence,
            next_payment_date=domain.next_payment_date,
            status=domain.status,
        )