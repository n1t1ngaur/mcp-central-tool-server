from pydantic_settings import BaseSettings, SettingsConfigDict


class MailboxSettings(BaseSettings):
    api_key: str
    api_url: str
    toolName: str
    description: str

    smtp: bool = True
    catch_all: bool = False
    format: bool = False
    callback: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env.mailbox",
        env_prefix="MAILBOX_"
    )
