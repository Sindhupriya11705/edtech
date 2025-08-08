from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    MONGODB_URI:    str = Field(..., env="MONGODB_URI")
    DATABASE_NAME:  str = Field("edtech", env="DATABASE_NAME")
    SECRET_KEY:     str = Field(..., env="SECRET_KEY")
    HF_API_KEY:     str = Field(..., env="HF_API_KEY")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()