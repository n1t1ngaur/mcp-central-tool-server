from abc import ABC, abstractmethod
from typing import Any


class LLMProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None
    ) -> Any:
        """
        Generate a response from the LLM.

        messages:
            Conversation messages.

        tools:
            Optional MCP tool definitions available to the model.
        """
        pass
    