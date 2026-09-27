from core.protocol.versioning import MCPProtocolMode
from infrastructure.config.mcp import MCPSettings


def test_default_protocol_mode_is_auto():

    settings = MCPSettings()

    assert settings.protocol_mode == MCPProtocolMode.AUTO


def test_supported_protocol_modes():

    assert MCPProtocolMode.AUTO.value == "auto"
    assert MCPProtocolMode.LEGACY.value == "legacy"
    assert MCPProtocolMode.MODERN.value == "2026-07-28"
    