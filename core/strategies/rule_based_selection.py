from typing import Any

from core.strategies.tool_selection import ToolSelectionStrategy


class RuleBasedToolSelectionStrategy(ToolSelectionStrategy):

    async def select_tool(
        self,
        query: str,
        tools: list[dict[str, Any]]
    ) -> str | None:

        query = query.lower()

        rules = {
            "github": "github_search",
            "repository": "github_search",
            "commit": "github_search",

            "database": "query_database",
            "sql": "query_database",

            "document": "search_documents",
            "pdf": "search_documents",
            "rag": "search_documents",

            "project": "get_project_status",
            "task": "get_project_status",
        }

        for keyword, tool_name in rules.items():
            if keyword in query:
                return tool_name

        return None