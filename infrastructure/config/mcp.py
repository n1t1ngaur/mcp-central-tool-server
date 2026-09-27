from pydantic_settings import BaseSettings, SettingsConfigDict

from core.protocol.versioning import MCPProtocolMode


class MCPSettings(BaseSettings):

    protocol_mode: MCPProtocolMode = MCPProtocolMode.AUTO

    client_name: str = "mcp-ai-host"
    client_version: str = "1.0.0"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="MCP_"
    )