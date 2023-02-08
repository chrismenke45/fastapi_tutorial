from pydantic import BaseSettings

class Settings(BaseSettings):
    fastapi_db_url: str
    fastapi_secret_key: str
    fastapi_algorithm: str
    fastapi_token_expire_minutes: str
    db_username: str
    db_password: str
    db_hostname: str
    db_port: str
    db_name: str

    class Config:
        env_file = ".env"

settings = Settings()

