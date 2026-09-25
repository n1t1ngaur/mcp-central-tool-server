from core.interfaces.tools import MCPTool,ToolResult
from infrastructure.config.aviation import AviationSettings
from dotenv import load_dotenv
import os



class AviationTool(MCPTool):

    def __init__(self, aviation_service):
        self.aviation_service = aviation_service
        self.settings = AviationSettings()

    @property
    def name(self)->str:
        "ToolName"
        return self.settings.toolName

    @property
    def description(self) -> str:
        return self.settings.description

    @property
    def input_schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of flights to return",
                    "default": self.settings.limit
                },
                "offset": {
                    "type": "integer",
                    "description": "Number of records to skip",
                    "default": self.settings.offset
                }
            }
        }

    async def execute(self, arguments: dict) -> ToolResult:

        limit = arguments.get(
            "limit",
            self.settings.limit
        )

        offset = arguments.get(
            "offset",
            self.settings.offset
        )

        data = await self.aviation_service.get_flights(
            limit=limit,
            offset=offset
        )

        return ToolResult(
            success=True,
            data=data
        )