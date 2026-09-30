import httpx
from infrastructure.config.mailBoxLayer import MailboxSettings


class MailValidatorLayerAPIAdapter:

    def __init__(self):
        self.settings = MailboxSettings()

    async def validate_email(
        self,
        email: str,
        smtp: bool = True,
        catch_all: bool = False,
        format: bool = False,
        callback: str | None = None,
    ):
        params = {
            "access_key": self.settings.api_key,
            "email": email,
            "smtp": smtp or self.settings.smtp,
            "catch_all": catch_all or self.settings.catch_all,
            "format": format or self.settings.format,
            "callback": callback or self.settings.callback
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.settings.api_url,
                params=params
            )
            response.raise_for_status()
            return response.json()