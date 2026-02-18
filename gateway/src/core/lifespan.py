from contextlib import asynccontextmanager
from fastapi import FastAPI

from ..grpc import order_rpc_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    await order_rpc_client.start()
    yield
    await order_rpc_client.close()