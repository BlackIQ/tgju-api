# Libs
from pydantic_settings import BaseSettings, SettingsConfigDict


# Settings class
class Settings(BaseSettings):
    # Database
    postgresql_url: str = ""

    model_config = SettingsConfigDict(env_file=".env")


# Settings
settings = Settings()
