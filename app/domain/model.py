from dataclasses import dataclass
from datetime import date
from datetime import datetime
from decimal import Decimal
from uuid import UUID

@dataclass
class Obligation:
    id: UUID | None
    title: str
    amount: Decimal
    currency: str
    category: str
    recurrence: str | None
    next_payment_date: date
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None