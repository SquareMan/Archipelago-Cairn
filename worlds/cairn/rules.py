from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule

from .items import ItemValue

if TYPE_CHECKING:
    from .world import CairnWorld


def set_all_rules(world: "CairnWorld"):
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: "CairnWorld") -> None:
    the_needle_to_the_secret = world.get_entrance("TheNeedle -> TheSecret")
    # TODO: Remove this for harder difficulties
    set_rule(the_needle_to_the_secret, lambda state: state.has(ItemValue.IceEquipment.name, world.player))


def set_all_location_rules(world: "CairnWorld") -> None:
    pass


def set_completion_condition(world: "CairnWorld") -> None:
    pass
