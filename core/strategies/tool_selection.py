from abc import ABC, abstractmethod
from typing import Any


class ToolSelectionStrategy(ABC):

    @abstractmethod
    async def select_tool(
        self,
        query: str,
        tools: list[dict[str, Any]]
    ) -> str | None:
        """
        Select the most appropriate tool for the given query.

        Returns:
            Tool name if a tool is selected,
            otherwise None.
        """
        pass