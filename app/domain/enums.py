from enum import Enum


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