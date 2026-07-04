from datetime import date

from app.domain.enums import StatusType
from app.domain.model import Obligation


class ObligationService:
    def __init__(self, repository):
        self.repository = repository

    async def create(self, data):
        today = date.today()

        status_check = await self.repository.get_active_by_title(data.title)

        warning = None
        if status_check:
            warning = "Активное обязательство с таким названием уже существует"

        if data.next_payment_date < today:
            status = StatusType.EXPIRED
        else:
            status = StatusType.ACTIVE

        obligation = Obligation(
            id=None,
            title=data.title,
            amount=data.amount,
            currency=data.currency,
            category=data.category,
            recurrence=data.recurrence,
            next_payment_date=data.next_payment_date,
            status=status,
        )

        result_obl = await self.repository.create_obligation(obligation)

        return {"obligation":result_obl,
                "warning":warning
                }

