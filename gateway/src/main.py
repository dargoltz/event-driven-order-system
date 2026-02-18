from fastapi import FastAPI

from .api import api_router
from .core import lifespan

app = FastAPI(lifespan=lifespan())
app.include_router(api_router)


@app.get("/health")
async def health():
    return {"status": "ok"}