# ../death_beam/config.py

"""Provides configuration based functionality for the plugin."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from config.manager import ConfigManager
from core import GAME_NAME

# Plugin
from .info import info
from .strings import CONFIG_STRINGS


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = (
    'beam_model',
    'beam_time',
    'beam_width',
)


# =============================================================================
# >> CONFIGURATION
# =============================================================================
with ConfigManager(info.name, 'db_') as _config:
    beam_width = _config.cvar(
        name='beam_width',
        default=10,
        description=CONFIG_STRINGS['beam_width'],
    )

    beam_time = _config.cvar(
        name='beam_time',
        default=4,
        description=CONFIG_STRINGS['beam_time'],
    )

    beam_model = _config.cvar(
        name='beam_model',
        default=f'sprites/laser{"beam" if GAME_NAME == "csgo" else ""}.vmt',
        description=CONFIG_STRINGS['beam_model'],
    )
