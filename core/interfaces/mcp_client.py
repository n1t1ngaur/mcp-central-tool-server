from abc import ABC, abstractmethod
from typing import Any


class MCPClientInterface(ABC):

    @property
    @abstractmethod
    def protocol_version(self) -> str | None:
        """Protocol version negotiated with the MCP server."""
        pass

    @abstractmethod
    async def connect(self) -> None:
        pass

    @abstractmethod
    async def list_tools(self) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    async def call_tool(
        self,
        tool_name: str,
        arguments: dict[str, Any]
    ) -> Any:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass