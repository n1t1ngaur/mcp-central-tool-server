from infrastructure.config.countrylayer import CountrySettings
from core.interfaces.tools import MCPTool, ToolResult



class CountryLayerTool(MCPTool):
    def __init__(self,CountryLayerService):
        self.CountryLayerService = CountryLayerService
        self.settings = CountrySettings()

    @property
    def name(self):
        return self.settings.toolName

    @property
    def description(self):
        return self.settings.description

    @property
    def input_schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "filters": {
                    "type": "string",
                    "description": "Fields to return from country API",
                    "default": self.settings.filters
                }
            }
        }

    async def execute(self, arguments: dict) -> ToolResult:

        filters = arguments.get(
            "filters",
            self.settings.filters
        )

        data = await self.country_layer_service.get_countries(
            filters=filters
        )

        return ToolResult(
            success=True,
            data=data
        )