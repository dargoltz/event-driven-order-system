import uuid
from enum import Enum

from pydantic import BaseModel, Field


class Status(str, Enum):
    CREATED = "created"
    AWAITING_PAYMENT = "awaiting payment"
    PAID = "paid"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class OrderCreateRequest(BaseModel):
    amount: float = Field(gt=0)


class OrderResponse(BaseModel):
    id: uuid.UUID
    status: Status
    amount: float = Field(gt=0)
