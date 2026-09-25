import httpx
from infrastructure.config.countrylayer import CountrySettings
class CountryLayerAPIAdapter:

    def __init__(self):
        self.settings = CountrySettings()

    async def get_countries(
        self,
        filters: str | None = None
    ):
        params = {
            "access_key": self.settings.api_key,
            "filters": filters or self.settings.filters
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.settings.api_url,
                params=params
            )
            response.raise_for_status()
            return response.json()