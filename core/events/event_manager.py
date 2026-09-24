from typing import Any
from core.interfaces.observer import ObserverInterface

class EventManager:

    def __init__(self):
        self._observers: list[ObserverInterface] = []

    def subscribe(
        self,
        observer: ObserverInterface
    ) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(
        self,
        observer: ObserverInterface
    ) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    async def notify(
        self,
        event_type: str,
        payload: dict[str, Any]
    ) -> None:

        for observer in self._observers:
            await observer.update(
                event_type,
                payload
            )