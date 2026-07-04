from dataclasses import dataclass
from datetime import date
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