import uuid

from fastapi import APIRouter, HTTPException

from .models import OrderResponse
from ..core import ApiKeyHeader
from ..grpc import order_rpc_client

api_router = APIRouter(prefix="/api")

orders_router = APIRouter(prefix="/orders", tags=["orders"])


@orders_router.post("/api/orders/")
async def create_order(
    amount: float,
    _: ApiKeyHeader
) -> OrderResponse:
    result = await order_rpc_client.create_order(amount)

    return ...


@orders_router.get("/api/orders/{order_id:uuid}")
async def get_order(
    order_id: uuid.UUID,
    _: ApiKeyHeader
) -> OrderResponse:
    result = await order_rpc_client.get_order(order_id)

    if not result:
        raise HTTPException(status_code=404, detail="Order not found")

    return ...


@orders_router.post("/api/orders/{order_id:uuid}/cancel")
async def cancel_order(
    order_id: uuid.UUID,
    _: ApiKeyHeader
):
    return await order_rpc_client.cancel_order(order_id)


api_router.include_router(orders_router)
