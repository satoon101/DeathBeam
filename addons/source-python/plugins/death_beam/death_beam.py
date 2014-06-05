# ../death_beam/death_beam.py

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python Imports
#   Config
from config.manager import ConfigManager
#   Effects
from effects import TempEntities
#   Settings
from settings.player import PlayerSettings
#   Translations
from translations.strings import LangStrings

# Script Imports
from death_beam.info import info


# =============================================================================
# >> PUBLIC VARIABLE
# =============================================================================
# Make sure the variable is set to the proper version
info.convar.set_string(info.version)

# Make the variable public
info.convar.make_public()


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Get the translations
death_beam_strings = LangStrings('death_beam')


# =============================================================================
# >> CONFIGURATION
# =============================================================================
# Create the death_beam.cfg file and execute it upon __exit__
with ConfigManager('death_beam') as config:

    pass


# =============================================================================
# >> GAME EVENTS
# =============================================================================
@Event
def player_death(game_event):
    '''Called any time a player dies'''
