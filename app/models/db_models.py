from datetime import date, datetime
from decimal import Decimal
from uuid import UUID, uuid4

from sqlalchemy import Date, DateTime, Enum, Numeric, String
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.domain.enums import (
    CategoryType,
    RecurrenceType,
    StatusType,
)


class ObligationORM(Base):
    __tablename__ = "obligations"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
    )

    category: Mapped[CategoryType] = mapped_column(
        Enum(CategoryType),
        nullable=False,
    )

    recurrence: Mapped[RecurrenceType | None] = mapped_column(
        Enum(RecurrenceType),
        nullable=True,
    )

    next_payment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[StatusType] = mapped_column(
        Enum(StatusType),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )