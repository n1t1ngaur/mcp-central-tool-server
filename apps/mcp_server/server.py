from mcp.server import MCPServer
from tools.aviationTool import AviationTool
from adapters.aviation_api_adapter import AviationAPIAdapter

from tools.countrylayer_tool import CountryLayerTool
from adapters.countrylayer_api_adapter import CountryLayerAPIAdapter

from tools.mailValidationTool import MailValidationTool
from adapters.mailBoxLayer_api_adapter import MailValidatorLayerAPIAdapter

from core.factories.tool_factory import ToolFactory
from dataclasses import asdict

mcp = MCPServer(
    "MCP Central Tool Server"
)

@mcp.tool()
async def transport_health() -> dict[str, str]:
    """
    Check whether the MCP server is reachable.
    """
    print("Lllllllllllllllllll")
    return {
        "status": "ok",
        "transport": "streamable-http"
    }



def build_tools():

    aviation_service = AviationAPIAdapter()
    country_layer_service = CountryLayerAPIAdapter()
    mailValidation_layer_service = MailValidatorLayerAPIAdapter()

    ToolFactory.register(
        "Aviation",
        AviationTool
    )

    ToolFactory.register(
        "CountryLayer",
        CountryLayerTool
    )

    ToolFactory.register(
            "MailValidatorLayer",
            MailValidationTool
    )

    aviation_tool = ToolFactory.create(
        "Aviation",
        aviation_service=aviation_service
    )

    country_layer_tool = ToolFactory.create(
        "CountryLayer",
        country_layer_service=country_layer_service
    )

    mainValidation_layer_tool= ToolFactory.create(
        "MailValidatorLayer",
        mail_validation_layer_service= mailValidation_layer_service
    )

    return [
        aviation_tool,
        country_layer_tool,
        mainValidation_layer_tool
    ]

def register_tools():

    aviation_tool, country_tool, mail_tool = build_tools()

    async def get_flights(
        limit: int = 100,
        offset: int = 0
    ) -> dict:
        result = await aviation_tool.execute({
            "limit": limit,
            "offset": offset
        })
        return asdict(result)

    async def get_countries(
        filters: str | None = None
    ) -> dict:
        result = await country_tool.execute({
            "filters": filters
        })
        return asdict(result)

    async def validate_email(
        email: str,
        smtp: bool = False,
        catch_all: bool = False
    ) -> dict:
        result = await mail_tool.execute({
            "email": email,
            "smtp": smtp,
            "catch_all": catch_all
        })
        return asdict(result)

    mcp.add_tool(
        get_flights,
        name=aviation_tool.name,
        description=aviation_tool.description
    )

    mcp.add_tool(
        get_countries,
        name=country_tool.name,
        description=country_tool.description
    )

    mcp.add_tool(
        validate_email,
        name=mail_tool.name,
        description=mail_tool.description
    )