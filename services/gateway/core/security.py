from typing import Annotated

from fastapi import HTTPException, Header, Depends

from services.gateway.core.config import config


def check_api_key(api_key: str = Header(...)):
    if api_key != config.api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")


ApiKeyHeader = Annotated[str, Depends(check_api_key)]
