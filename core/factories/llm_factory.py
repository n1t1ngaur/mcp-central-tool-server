from typing import Type

from core.interfaces.llm import LLMProvider


class LLMFactory:

    _registry: dict[str, Type[LLMProvider]] = {}

    @classmethod
    def register(
        cls,
        name: str,
        provider_class: Type[LLMProvider]
    ) -> None:
        cls._registry[name] = provider_class

    @classmethod
    def create(
        cls,
        name: str,
        **kwargs
    ) -> LLMProvider:

        provider_class = cls._registry.get(name)

        if not provider_class:
            raise ValueError(
                f"LLM provider '{name}' is not registered."
            )

        return provider_class(**kwargs)

    @classmethod
    def available_providers(cls) -> list[str]:
        return list(cls._registry.keys())