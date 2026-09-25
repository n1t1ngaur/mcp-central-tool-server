import httpx
from infrastructure.config.aviation import AviationSettings

class AviationAPIAdapter:

    def __init__(self):
        self.settings = AviationSettings()

    async def get_flights(
        self,
        limit: int,
        offset: int
    ):

        params = {
            "access_key": self.settings.api_key,
            "limit": limit,
            "offset": offset
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(
                self.settings.api_url,
                params=params
            )
            response.raise_for_status()
            return response.json()