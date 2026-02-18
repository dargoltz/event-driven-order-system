from pydantic_settings import BaseSettings

class Config(BaseSettings):
    api_key: str = "_"

config = Config()