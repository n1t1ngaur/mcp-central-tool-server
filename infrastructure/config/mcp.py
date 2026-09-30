from pydantic_settings import BaseSettings, SettingsConfigDict

from core.protocol.versioning import MCPProtocolMode


class MCPSettings(BaseSettings):

    protocol_mode: MCPProtocolMode = MCPProtocolMode.AUTO

    client_name: str = "mcp-ai-host"
    client_version: str = "1.0.0"

    server_host: str = "127.0.0.1"
    server_port: int = 8001
    server_path: str = "/mcp"

    model_config = SettingsConfigDict(
        env_file=".env.mcp",
        env_prefix="MCP_"
    )

    @property
    def server_url(self) -> str:
        return (
            f"http://{self.server_host}:"
            f"{self.server_port}"
            f"{self.server_path}"
        )
