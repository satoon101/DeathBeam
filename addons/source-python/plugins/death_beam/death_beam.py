# ../death_beam/death_beam.py

"""Show a beam from the killer to their victim."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Source.Python
from colors import BLUE, RED
from effects.base import TempEntity
from engines.precache import Model
from entities import TakeDamageInfo
from entities.constants import EntityEffects, SolidType
from entities.entity import Entity
from entities.hooks import EntityCondition, EntityPreHook
from events import Event
from listeners import OnLevelInit
from mathlib import Matrix3x4, Vector
from memory import Convention, DataType, make_object
from players.entity import Player
from players.helpers import userid_from_index
from stringtables import string_tables
from studio.cache import model_cache

# Plugin
from .config import beam_model, beam_time, beam_width
from .strings import TRANSLATION_STRINGS


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
_model = Model(str(beam_model))
KILLER_DICTIONARY = {}
_team_colors = {
    2: RED,
    3: BLUE,
}


# =============================================================================
# >> FUNCTION HOOKS
# =============================================================================
@EntityPreHook(EntityCondition.is_bot_player, 'on_take_damage')
@EntityPreHook(EntityCondition.is_human_player, 'on_take_damage')
def _pre_take_damage(stack_data):
    """Store the information for later use."""
    take_damage_info = make_object(TakeDamageInfo, stack_data[1])
    attacker = Entity(take_damage_info.attacker)
    if attacker.classname != 'player':
        return

    victim = make_object(Player, stack_data[0])
    if victim.health > take_damage_info.damage:
        return

    KILLER_DICTIONARY[victim.userid] = {
        'attacker': userid_from_index(attacker.index),
        'end': Vector(*take_damage_info.position),
        'projectile': attacker.index != take_damage_info.inflictor,
        'color': _team_colors[victim.team],
    }


# =============================================================================
# >> GAME EVENTS
# =============================================================================
@Event('player_death')
def _player_death(game_event):
    """Determine if the death should spawn a beam."""
    userid = game_event['userid']
    kill_info = KILLER_DICTIONARY.pop(userid, None)
    if kill_info is None:
        return

    attacker = game_event['attacker']
    if attacker != kill_info['attacker']:
        return

    killer = Player.from_userid(attacker)
    if kill_info['projectile']:
        start = _get_start_from_player(killer)
    else:
        start = _get_start_from_weapon(killer)

    _create_beam(start, kill_info['end'], kill_info['color'])


@OnLevelInit
@Event('round_start')
def _reset_dictionary(*args, **kwargs):
    """Reset the kill info dictionary."""
    KILLER_DICTIONARY.clear()


# =============================================================================
# >> HELPER FUNCTIONS
# =============================================================================
def _get_start_from_player(player):
    """Return the player's position."""
    location = player.origin
    location.z += 20
    return location


def _get_start_from_weapon(player):
    """Return the weapon's position."""
    weapon = player.active_weapon
    if weapon is None:
        return

    world_model = string_tables[Model.precache_table][weapon.world_model_index]
    header = model_cache.get_model_header(model_cache.find_model(world_model))

    has_muzzle = False
    for index in range(header.attachments_count):
        if header.get_attachment(index).name != 'muzzle_flash':
            continue
        has_muzzle = True

    if not has_muzzle:
        return

    bone = _find_bone(player.model_header, 'ValveBiped.Bip01_R_Hand')
    if bone == -1:
        return

    GetBoneTransform = player.make_virtual_function(
        199,
        Convention.THISCALL,
        [DataType.POINTER, DataType.INT, DataType.POINTER],
        DataType.VOID,
    )

    matrix = Matrix3x4()
    GetBoneTransform(player, bone, matrix)

    angles = matrix.angles
    angles.z += 180

    prop = Entity.create('prop_dynamic_override')
    prop.model_name = world_model
    prop.effects = EntityEffects.NODRAW
    prop.solid_type = SolidType.NONE
    prop.origin = matrix.position
    prop.angle = Vector(*angles)
    prop.spawn()

    null = Entity.create('info_null')
    null.set_parent(prop)
    null.call_input('SetParentAttachment', 'muzzle_flash')

    origin = null.get_property_vector('m_vecAbsOrigin')

    null.spawn()
    prop.remove()

    return origin


def _find_bone(header, name):
    """Return the index of the bone."""
    for index in range(header.bones_count):
        bone = header.get_bone(index)
        if bone.name == name:
            return index

    return -1


def _create_beam(start, end, color):
    """Create the beam from the player/weapon's origin to the victim's."""
    width = int(beam_width)
    entity = TempEntity('BeamPoints')
    entity.start_point = start
    entity.start_width = width
    entity.end_point = end
    entity.end_width = width
    entity.color = color
    entity.life_time = int(beam_time)
    entity.model = _model
    entity.halo = _model
    entity.create()
