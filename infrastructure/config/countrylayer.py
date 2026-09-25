from pydantic_settings import BaseSettings, SettingsConfigDict


class CountrySettings(BaseSettings):
    api_key: str
    api_url: str
    toolName: str
    description: str
    filters: str = "name;capital;currencies"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="COUNTRY_"
    )