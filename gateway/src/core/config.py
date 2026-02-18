from pydantic_settings import BaseSettings

class Config(BaseSettings):
    API_KEY: str = "_"
    ORDER_RPC_HOST: str = "localhost:50051"

config = Config()