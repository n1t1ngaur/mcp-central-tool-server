from core.interfaces.llm import LLMProvider
from core.interfaces.mcp_client import MCPClientInterface
from core.strategies.tool_selection import ToolSelectionStrategy
from core.events.event_manager import EventManager


class Agent:

    def __init__(
        self,
        llm: LLMProvider,
        mcp_client: MCPClientInterface,
        tool_strategy: ToolSelectionStrategy,
        event_manager: EventManager
    ):
        self.llm = llm
        self.mcp_client = mcp_client
        self.tool_strategy = tool_strategy
        self.event_manager = event_manager

    async def run(self, query: str):

        await self.event_manager.notify(
            "query_received",
            {"query": query}
        )

        tools = await self.mcp_client.list_tools()

        selected_tool = await self.tool_strategy.select_tool(
            query=query,
            tools=tools
        )

        if selected_tool:

            await self.event_manager.notify(
                "tool_selected",
                {
                    "tool": selected_tool,
                    "query": query
                }
            )

            tool_result = await self.mcp_client.call_tool(
                tool_name=selected_tool,
                arguments={
                    "query": query
                }
            )

            response = await self.llm.generate(
                messages=[
                    {
                        "role": "user",
                        "content": query
                    },
                    {
                        "role": "tool",
                        "content": str(tool_result)
                    }
                ]
            )

            return response

        return await self.llm.generate(
            messages=[
                {
                    "role": "user",
                    "content": query
                }
            ]
        )