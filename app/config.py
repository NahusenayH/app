from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql://user:password@localhost/db_name"
    SECRET_KEY: str = "your-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    CACHE_EXPIRATION: int = 300  # 5 minutes in seconds

    class Config:
        env_file = ".env"

settings = Settings()