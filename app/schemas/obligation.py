from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator

from app.domain.enums import CategoryType, RecurrenceType


class ObligationsRequest(BaseModel):
    title: str = Field(min_length=1)
    amount: Decimal
    currency: str
    category: CategoryType
    recurrence: RecurrenceType | None = Field(
        default=None,
        description="Периодичность повторения. null — для разовых обязательств."
    )
    next_payment_date: date

    @field_validator("currency")
    @classmethod
    def currency_validator(cls, value: str) -> str:
        value = value.upper()
        allowed = {"RUB", "USD", "EUR"}
        if value not in allowed:
            raise ValueError(f"Валюта должна быть одной из: {', '.join(allowed)}")
        return value


class ObligationsResponse(BaseModel):
    obligation: str
    warning: str | None = Field(
        default=None,
        description="Активное обязательство с таким названием уже существует"
    )