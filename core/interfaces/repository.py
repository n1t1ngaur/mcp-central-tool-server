from abc import ABC, abstractmethod
from typing import Any


class RepositoryInterface(ABC):

    @abstractmethod
    async def get_by_id(self, item_id: str) -> Any:
        """Fetch one record by ID."""
        pass

    @abstractmethod
    async def list(self, filters: dict | None = None) -> list[Any]:
        """Fetch multiple records."""
        pass

    @abstractmethod
    async def create(self, data: dict) -> Any:
        """Create a new record."""
        pass

    @abstractmethod
    async def update(self, item_id: str, data: dict) -> Any:
        """Update an existing record."""
        pass

    @abstractmethod
    async def delete(self, item_id: str) -> bool:
        """Delete a record."""
        pass