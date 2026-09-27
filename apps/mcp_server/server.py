from tools.aviationTool import AviationTool
from adapters.aviation_api_adapter import AviationAPIAdapter

from tools.countrylayer_tool import CountryLayerTool
from adapters.countrylayer_api_adapter import CountryLayerAPIAdapter

from tools.mailValidationTool import MailValidationTool
from adapters.mailBoxLayer_api_adapter import MailValidatorLayerAPIAdapter

from core.factories.tool_factory import ToolFactory


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