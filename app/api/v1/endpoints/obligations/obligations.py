from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator
from fastapi import FastAPI, APIRouter

router = APIRouter()

class StatusType(str, Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    EXPIRED = "expired"

class RecurrenceType(str, Enum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    YEARLY = "yearly"

class CategoryType(str, Enum):
    SUBSCRIPTION = "subscription"
    WARRANTY = "warranty"
    BILL = "bill"
    INSURANCE = "insurance"

class ObligationsRequestDTO(BaseModel):
    title: str = Field(min_length=1)
    amount: Decimal
    currency: str
    category: CategoryType
    recurrence: RecurrenceType | None = Field(
        default=None,
        description="Периодичность повторения. null — для разовых обязательств."
    )
    next_payment_date: date
    status: StatusType

    @field_validator("currency")
    @classmethod
    def currency_validator(cls, value: str) -> str:
        upper_val = value.upper()
        allowed = ["RUB", "USD", "EUR"]

        if upper_val not in allowed:
            raise ValueError(f"Валюта должна быть одной из: {','.join(allowed)}")

        return upper_val

class ObligationsResponse(BaseModel):
    obligation: str
    warning: str | None = Field(
        default=None,
        description="Активное обязательство с таким названием уже существует"
    )

@router.post("/obligations", response_model=ObligationsResponse, tags=["obligations"])
def create_obligation(obligation: ObligationsRequestDTO):