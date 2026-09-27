from infrastructure.config.mailBoxLayer import MailboxSettings
from core.interfaces.tools import MCPTool, ToolResult



class MailValidationTool(MCPTool):
    def __init__(self, MailValidationService):
        self.mailbox_layer_service = MailValidationService
        self.settings = MailboxSettings()

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
                "email": {
                    "type": "string",
                    "description": "Email address to validate."
                },
                "smtp": {
                    "type": "boolean",
                    "description": "Enable SMTP verification.",
                    "default": False
                },
                "catch_all": {
                    "type": "boolean",
                    "description": "Enable catch-all email detection.",
                    "default": False
                },
                "format": {
                    "type": "boolean",
                    "description": "Return formatted JSON response.",
                    "default": False
                },
                "callback": {
                    "type": ["string", "null"],
                    "description": "Optional JSONP callback function.",
                    "default": None
                }
            },
            "required": ["email"]
        }


    async def execute(self, arguments: dict) -> ToolResult:

        email = arguments.get("email")
        smtp = arguments.get("smtp", False)
        catch_all = arguments.get("catch_all", False)
        format = arguments.get("format", False)
        callback = arguments.get("callback", None)

        data = await self.mailbox_layer_service.validate_email(
            email=email,
            smtp=smtp,
            catch_all=catch_all,
            format=format,
            callback=callback
        )

        return ToolResult(
            success=True,
            data=data
        )