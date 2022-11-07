from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = "Production"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite+aiosqlite:///./shorter-url.db"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
