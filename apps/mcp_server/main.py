from apps.mcp_server.server import mcp, register_tools
from infrastructure.config.mcp import MCPSettings


def main():

    settings = MCPSettings()
    register_tools()
    mcp.run(
        transport="streamable-http",
        host=settings.server_host,
        port=settings.server_port,
        streamable_http_path=settings.server_path
    )


if __name__ == "__main__":
    main()