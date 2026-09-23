from abc import ABC, abstractmethod
from typing import Any


class ObserverInterface(ABC):

    @abstractmethod
    async def update(
        self,
        event_type: str,
        payload: dict[str, Any]
    ) -> None:
        """Receive event notifications."""
        pass