from enum import Enum

class MCPProtocolMode(str, Enum):
    AUTO = "auto"
    LEGACY = "legacy"
    MODERN = "2026-07-28"