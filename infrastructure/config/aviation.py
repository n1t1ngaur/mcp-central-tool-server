from pydantic_settings import BaseSettings, SettingsConfigDict

class AviationSettings(BaseSettings):
    api_key: str
    api_url: str
    limit: int = 100
    offset: int = 0
    toolName: str
    description: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="AVIATION_"
    )