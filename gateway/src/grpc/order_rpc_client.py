import grpc

import order_pb2
import order_pb2_grpc
from ..core import config


class OrderRPCClient:
    def __init__(self):
        self.channel = None
        self.stub = None

    async def start(self):
        self.channel = grpc.aio.insecure_channel(config.ORDER_RPC_HOST)
        self.stub = order_pb2_grpc.OrderServiceStub(self.channel)

    async def close(self):
        if self.channel:
            await self.channel.close()

    async def create_order(self, amount: float):
        req = order_pb2.OrderCreateRequest(amount=amount)
        return await self.stub.CreateOrder(req)

    async def get_order(self, order_id: str):
        req = order_pb2.OrderId(id=order_id)
        return await self.stub.GetOrder(req)

    async def cancel_order(self, order_id: str):
        req = order_pb2.OrderId(id=order_id)
        await self.stub.CancelOrder(req)


order_rpc_client = OrderRPCClient()
