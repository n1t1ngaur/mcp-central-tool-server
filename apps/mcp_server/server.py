from tools.aviationTool import AviationTool
from adapters.aviation_api_adapter import AviationAPIAdapter

from tools.countrylayer_tool import CountryLayerTool
from adapters.countrylayer_api_adapter import CountryLayerAPIAdapter

from core.factories.tool_factory import ToolFactory


def build_tools():

    aviation_service = AviationAPIAdapter()
    country_layer_service = CountryLayerAPIAdapter()

    ToolFactory.register(
        "Aviation",
        AviationTool
    )

    ToolFactory.register(
        "CountryLayer",
        CountryLayerTool
    )

    aviation_tool = ToolFactory.create(
        "Aviation",
        aviation_service=aviation_service
    )

    country_layer_tool = ToolFactory.create(
        "CountryLayer",
        country_layer_service=country_layer_service
    )

    return [
        aviation_tool,
        country_layer_tool
    ]