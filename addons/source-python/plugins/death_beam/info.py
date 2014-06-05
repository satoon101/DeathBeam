# ../death_beam/info.py

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python Imports
#   Plugins
from plugins.info import PluginInfo


# =============================================================================
# >> PLUGIN INFO
# =============================================================================
info = PluginInfo()
info.name = 'Death Beam'
info.author = 'Satoon101'
info.version = '1.0'
info.basename = 'death_beam'
info.variable = info.basename + '_version'
info.url = ''
info.convar = ServerVar(info.variable, info.version, 0, info.name + ' Version')
