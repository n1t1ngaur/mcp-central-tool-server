from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class ToolResult:
    success: bool
    data: Any = None
    error: str | None = None


class MCPTool(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique tool name."""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Description used by the AI/LLM to understand the tool."""
        pass

    @property
    @abstractmethod
    def input_schema(self) -> dict:
        """Schema describing the arguments accepted by the tool."""
        pass

    @abstractmethod
    async def execute(self, arguments: dict) -> ToolResult:
        """Execute the tool."""
        pass