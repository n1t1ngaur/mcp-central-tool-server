from typing import Type

from core.interfaces.tools import MCPTool


class ToolFactory:

    _registry: dict[str, Type[MCPTool]] = {}

    @classmethod
    def register(
        cls,
        name: str,
        tool_class: Type[MCPTool]
    ) -> None:
        cls._registry[name] = tool_class

    @classmethod
    def create(
        cls,
        name: str,
        **kwargs
    ) -> MCPTool:

        tool_class = cls._registry.get(name)

        if not tool_class:
            raise ValueError(
                f"Tool '{name}' is not registered."
            )

        return tool_class(**kwargs)

    @classmethod
    def available_tools(cls) -> list[str]:
        return list(cls._registry.keys())