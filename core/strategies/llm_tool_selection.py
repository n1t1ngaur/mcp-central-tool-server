from typing import Any

from core.interfaces.llm import LLMProvider
from core.strategies.tool_selection import ToolSelectionStrategy


class LLMToolSelectionStrategy(ToolSelectionStrategy):

    def __init__(self, llm: LLMProvider):
        self.llm = llm

    async def select_tool(
        self,
        query: str,
        tools: list[dict[str, Any]]
    ) -> str | None:

        if not tools:
            return None

        prompt =    f"""
                        You are a tool selection system.

                        User query:
                        {query}

                        Available tools:
                        {tools}

                        Return only the exact tool name that should be used.
                        If no tool is required, return NONE.
                    """

        response = await self.llm.generate(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        if response is None:
            return None

        selected_tool = str(response).strip()

        if selected_tool.upper() == "NONE":
            return None

        available_tool_names = {
            tool.get("name")
            for tool in tools
        }

        if selected_tool not in available_tool_names:
            return None

        return selected_tool