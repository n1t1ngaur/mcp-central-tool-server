from abc import ABC, abstractmethod
from typing import Any


class MCPClientInterface(ABC):

    @abstractmethod
    async def connect(self) -> None:
        """Connect to the MCP server."""
        pass

    @abstractmethod
    async def list_tools(self) -> list[dict[str, Any]]:
        """Return tools exposed by the MCP server."""
        pass

    @abstractmethod
    async def call_tool(
        self,
        tool_name: str,
        arguments: dict[str, Any]
    ) -> Any:
        """Call a tool on the MCP server."""
        pass

    @abstractmethod
    async def close(self) -> None:
        """Close the MCP connection."""
        pass