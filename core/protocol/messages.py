from dataclasses import dataclass
from typing import Any


@dataclass
class JSONRPCRequest:
    method: str
    params: dict[str, Any]
    id: int | str

    def to_dict(self) -> dict:
        return {
            "jsonrpc": "2.0",
            "id": self.id,
            "method": self.method,
            "params": self.params,
        }


@dataclass
class JSONRPCResponse:
    id: int | str
    result: Any

    def to_dict(self) -> dict:
        return {
            "jsonrpc": "2.0",
            "id": self.id,
            "result": self.result,
        }


@dataclass
class JSONRPCError:
    id: int | str
    code: int
    message: str

    def to_dict(self) -> dict:
        return {
            "jsonrpc": "2.0",
            "id": self.id,
            "error": {
                "code": self.code,
                "message": self.message,
            },
        }


@dataclass
class JSONRPCNotification:
    method: str
    params: dict[str, Any]

    def to_dict(self) -> dict:
        return {
            "jsonrpc": "2.0",
            "method": self.method,
            "params": self.params,
        }