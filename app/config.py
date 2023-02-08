from pydantic import BaseSettings

class Settings(BaseSettings):
    fastapi_db_url: str
    fastapi_secret_key: str
    fastapi_algorithm: str
    fastapi_token_expire_minutes: str

    class Config:
        env_file = ".env"

settings = Settings()

