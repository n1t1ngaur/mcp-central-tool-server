import pytest
from apps.ai_host.agent import Agent
from core.interfaces.llm import LLMProvider
from core.interfaces.mcp_client import MCPClientInterface
from core.strategies.tool_selection import ToolSelectionStrategy
from core.events.event_manager import EventManager


class FakeLLM(LLMProvider):

    async def generate(self, messages, tools=None):
        return "Final response from LLM"


class FakeMCPClient(MCPClientInterface):

    async def connect(self):
        pass

    async def list_tools(self):
        return [
            {
                "name": "github_search",
                "description": "Search GitHub"
            }
        ]

    async def call_tool(self, tool_name, arguments):
        return {
            "tool": tool_name,
            "result": "3 commits found"
        }

    async def close(self):
        pass


class FakeToolStrategy(ToolSelectionStrategy):

    async def select_tool(self, query, tools):
        return "github_search"


@pytest.mark.asyncio
async def test_agent_flow():

    llm = FakeLLM()
    mcp_client = FakeMCPClient()
    strategy = FakeToolStrategy()
    event_manager = EventManager()

    agent = Agent(
        llm=llm,
        mcp_client=mcp_client,
        tool_strategy=strategy,
        event_manager=event_manager
    )

    result = await agent.run(
        "Show latest GitHub commits"
    )

    assert result == "Final response from LLM"