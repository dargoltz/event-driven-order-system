import uuid

from fastapi import APIRouter

from .models import OrderCreateRequest, OrderResponse
from ..core import ApiKeyHeader

api_router = APIRouter(prefix="/api")

orders_router = APIRouter(prefix="/orders", tags=["orders"])


@orders_router.post("/api/orders/")
async def create_order(
    request: OrderCreateRequest,
    _: ApiKeyHeader
) -> OrderResponse:  # todo быстро либо будет происходить создание? стоит ли ждать и возвращать респонс?
    ...


@orders_router.get("/api/orders/{order_id:uuid}")
async def get_order(
    order_id: uuid.UUID,
    _: ApiKeyHeader
) -> OrderResponse:
    ...


@orders_router.post("/api/orders/{order_id:uuid}/cancel")
async def cancel_order(
    order_id: uuid.UUID,
    _: ApiKeyHeader
):  # todo что стоит тут вернуть? сразу отмененный из бд? в сервисах не факт что отменится в этот момент еще
    ...


api_router.include_router(orders_router)
