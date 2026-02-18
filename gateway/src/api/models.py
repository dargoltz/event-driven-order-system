import uuid
from enum import Enum

from pydantic import BaseModel, Field


class Status(str, Enum):
    CREATED = "CREATED"
    AWAITING_PAYMENT = "AWAITING_PAYMENT"
    PAID = "PAID"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class OrderResponse(BaseModel):
    id: uuid.UUID
    status: Status
    amount: float = Field(gt=0)
