from dataclasses import dataclass
from enum import Enum, auto
from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items
from .regions import RegionValue

if TYPE_CHECKING:
    from .world import CairnWorld


class LocationValue(Enum):
    VillageBagSlot1 = 1
    VillageBagSlot2 = 2

    IceEquipment = 10000
    Summit = auto()


@dataclass
class Container:
    name: str
    slots: int


IDS_PER_CONTAINER = 16
IDS_PER_REGION = 1000


def loot_locations_for_container(container: Container, base_id: int):
    assert container.slots <= IDS_PER_CONTAINER, f"container.slots = {container.slots}"
    if container.slots == 1:
        return {container.name: base_id}
    return {f"{container.name} Slot {(i + 1)!s}": base_id + i for i in range(0, container.slots)}


def loot_locations_for_region(region: RegionValue):
    containers = REGION_TO_CONTAINERS[region]
    base_id = region.value * IDS_PER_REGION

    # assert len(containers) <= IDS_PER_REGION / IDS_PER_CONTAINER
    return {
        f"{region.name} {name}": id
        for idx, container in enumerate(containers)
        for name, id in loot_locations_for_container(container, base_id + (idx * IDS_PER_CONTAINER)).items()
    }


REGION_TO_CONTAINERS: dict[RegionValue, list[Container]] = {
    RegionValue.Tenzen: [
        Container("Cairn_Coins (3)", 1),
        Container("LootVolume", 1),
        Container("PitonLootable", 1),
        Container("ClimbingGym_Loots", 4),
        Container("Bottle", 1),
        Container("Cairn_Coins (1)", 1),
        Container("Cairn_Coins (4)", 1),
        Container("Cairn_Coins", 1),
        Container("Cairn_Coins (2)", 1),
        Container("PitonLootable (1)", 1),
        Container("Rubbish_PlasticBottle", 1),
        Container("Raspberry_1", 1),
        Container("Rubbish_PlasticBag", 1),
        Container("Thistle_1", 1),
        Container("Gentian_1", 1),
        Container("Thistle_1 (1)", 1),
        Container("Dandelion_1", 1),
        Container("Object_04", 1),
        Container("Raspberry_1 (2)", 1),
        Container("Gentian_1 (1)", 1),
        Container("Thistle_1 (2)", 1),
        Container("Nettle_1", 1),
        Container("BirdNest_1_Egg", 1),
        Container("Honey_1", 1),
        Container("Raspberry_1 (3)", 1),
        Container("BirdNest_1_Egg (2)", 1),
    ],
    RegionValue.TheTwistedRidge: [
        Container("Rubbish_PlasticBottle", 1),
        Container("Raspberry_1 (1)", 1),
        Container("Rubbish_PlasticBottle (2)", 1),
        Container("BirdNest_1_Egg", 1),
        Container("Thistle_1", 1),
        Container("Bag_Bells", 3),
        Container("Rubbish_PlasticBag (1)", 1),
        Container("Rubbish_Can (2)", 1),
        Container("Rubbish_GlassBottle (1)", 1),
        Container("Thistle_1 (1)", 1),
        Container("Rubbish_PlasticBag", 1),
        Container("Object_01", 1),
        Container("Rubbish_PlasticBottle (1)", 1),
        Container("Rubbish_Can (1)", 1),
        Container("Rubbish_PlasticBag (2)", 1),
        Container("Honey_1 (1)", 1),
        Container("LootVolume_BrokenVendingMachine", 5),
        Container("Gentian_1", 1),
        Container("Dandelion_1", 1),
        Container("Rubbish_GlassBottle (2)", 1),
        Container("HoneyPot (1)", 1),
        Container("Mushroom_1", 1),
        Container("Rubbish_GlassBottle", 1),
        Container("Rubbish_Can", 1),
        Container("Honey_1 (2)", 1),
        Container("Rubbish_PlasticBottle (2)", 1),
    ],
    RegionValue.TheEscarpment: [
        Container("Object_02", 1),
        Container("Raspberry_1", 1),
        Container("Thistle_Wall_1", 1),
        Container("Honey_1", 1),
        Container("BearBox", 10),
        Container("Can_SparklingWater ", 1),
        Container("Nettle_1", 1),
        Container("Object_01", 1),
        Container("Chimney_Loots", 5),
        Container("Gentian_1", 1),
        Container("Mushroom_1", 1),
        Container("Object_03", 1),
        Container("BirdNest_1_Egg", 1),
    ],
    RegionValue.TheArch: [
        Container("Thistle_1 (1)", 1),
        Container("Pot_02", 5),
        Container("Thistle_Wall_1", 1),
        Container("BrokenPitonLoot", 1),
        Container("BearBox", 10),
        Container("Can_Milk", 1),
        Container("Mushroom_1", 1),
        Container("LootVolume", 1),
        Container("Rubbish_PlasticBag", 1),
        Container("Bottle", 1),
        Container("Bag_TentBag", 3),
        Container("Nettle_Wall_1", 1),
        Container("Rubbish_PlasticBag (2)", 1),
        Container("Rubbish_PlasticBottle", 1),
        Container("Dandelion_Wall_1", 1),
        Container("Rubbish_PlasticBottle (1)", 1),
        Container("Rubbish_GlassBottle (1)", 1),
        Container("Rubbish_Can", 1),
        Container("Rubbish_PlasticBag (3)", 1),
        Container("Bag", 3),
        Container("Rubbish_PlasticBottle (2)", 1),
        Container("BirdNest_1_Egg", 1),
        Container("Outside", 9),
        Container("Nettle_1", 1),
        Container("Gentian_1", 1),
        Container("Mushroom_1 (2)", 1),
        Container("Rubbish_GlassBottle", 1),
        Container("BirdNest_2_Eggs", 1),
        Container("Outside (2)", 3),
        Container("Rubbish_GlassBottle (2)", 1),
        Container("Rubbish_Can (1)", 1),
        Container("LootVolume (2)", 1),
        Container("BearBox (2)", 11),
        Container("Can_YellowYak", 1),
        Container("Rubbish_PlasticBag (4)", 1),
        Container("Rubbish_PlasticBag (1)", 1),
        Container("LootVolume (3)", 1),
        Container("LootVolume (4)", 1),
        Container("Outside (3)", 4),
        Container("Can_Moonshine", 1),
        Container("Rubbish_PlasticBottle (1) (2)", 1),
        Container("Rubbish_PlasticBottle (2)", 1),
        Container("Object_06", 1),
        Container("LootVolume (5)", 1),
    ],
    RegionValue.TheShortcut: [],
    RegionValue.TheSplitRock: [
        Container("Gentian_1 (1)", 1),
        Container("Pot_01", 2),
        Container("Mushroom_1", 1),
        Container("Nettle_Wall_1", 1),
        Container("Gentian_1", 1),
        Container("Pot_02", 5),
        Container("Raspberry_1", 1),
        Container("BirdNest_1_Egg", 1),
        Container("Thistle_1", 1),
    ],
    RegionValue.TheWaterfall: [
        Container("Raspberry_1 (2)", 1),
        Container("Thistle_1", 1),
        Container("WildGarlic_Wall_1", 1),
        Container("Raspberry_1 (3)", 1),
        Container("Raspberry_Wall_1", 1),
        Container("Nettle_1", 1),
        Container("Gentian_1", 1),
        Container("Dandelion_1", 1),
        Container("BirdNest_1_Egg (1)", 1),
        Container("BirdNest_1_Egg", 1),
        Container("Thistle_Wall_1", 1),
        Container("Rubbish_Can (1)", 1),
        Container("Bag (2)", 2),
        Container("Gentian_1 (2)", 1),
        Container("LootVolume", 1),
        Container("Bag", 4),
        Container("Mushroom_1", 1),
        Container("Pot_01", 4),
        Container("Rubbish_Can", 1),
        Container("LootVolume (2)", 1),
        Container("Bag (1)", 4),
        Container("Pot_02 (1)", 2),
        Container("Thistle_Wall_1 (2)", 1),
        Container("Dandelion_Wall_1", 1),
        Container("LootVolume (3)", 1),
        Container("LootVolume (4)", 1),
        Container("Rubbish_Can (2)", 1),
        Container("BirdNest_1_Egg (2)", 1),
        Container("BirdNest_1_Egg (1) (2)", 1),
    ],
    RegionValue.TheVillage: [
        Container("Thistle_Wall_1", 1),
        Container("Honey_1", 1),
        Container("Raspberry_1 (1)", 1),
        Container("Nettle_1", 1),
        Container("Plantain_1", 1),
        Container("Nettle_Wall_1", 1),
        Container("Mushroom_1", 1),
        Container("LootVolume", 1),
        Container("Well_Loots", 5),
        Container("Well_Loots (2)", 4),
        Container("Raspberry_1", 1),
        Container("BirdNest_1_Egg", 1),
        Container("BirdNest_1_Egg (2)", 1),
        Container("Dandelion_1", 1),
    ],
    RegionValue.TheStandingStones: [
        Container("Bag", 5),
        Container("WildGarlic_Wall_1", 1),
        Container("Mushroom_1", 1),
        Container("Can_SparklingWater ", 1),
        Container("Juniper_Wall_1", 1),
        Container("Nettle_1", 1),
        Container("WildGarlic_1", 1),
        Container("LootVolume", 1),
        Container("BearBox", 11),
        Container("Juniper_1 (3)", 1),
        Container("Raspberry_1", 1),
        Container("12_FirstGuardian_BabyStatuetteLoot", 1),
        Container("LootVolume (2)", 1),
        Container("Bag (1)", 4),
        Container("LootVolume (3)", 1),
        Container("LootVolume (4)", 1),
        Container("BearBox (2)", 11),
        Container("Mushroom_Wall_1", 1),
        Container("Dandelion_1", 1),
        Container("Bag (2)", 3),
        Container("Honey_1 (1)", 1),
        Container("WildGarlic_1 (2)", 1),
        Container("Gentian_1", 1),
        Container("PitonLootableCrystal", 1),
        Container("Honey_1", 1),
        Container("Plantain_Wall_1", 1),
        Container("Pot_01", 1),
        Container("Gentian_1 (2)", 1),
        Container("DeadBody_LootVolume", 3),
        Container("LootVolume (5)", 1),
        Container("LootVolume (6)", 1),
        Container("Plantain_Wall_1 (2)", 1),
        Container("Rubbish_PlasticBag", 1),
        Container("Rubbish_PlasticBottle", 1),
        Container("Bag (2)", 5),
        Container("BearBox (3)", 11),
        Container("Bottle", 1),
        Container("Bag (3)", 4),
        Container("Thistle_1", 1),
        Container("LootVolume (7)", 1),
    ],
    RegionValue.TheChild: [],
    RegionValue.TheVault: [
        Container("Mushroom_1 (1)", 1),
        Container("11_ShepherdIndoor_NPCExchange_Shepherdess", 1),
        Container("LootVolume", 1),
        Container("Tomato_Crate", 1),
        Container("Pot_02", 6),
        Container("Tomato_Crate (1)", 1),
        Container("Gentian_1", 1),
    ],
    RegionValue.TheTerraces: [
        Container("Gentian_1", 1),
        Container("Nettle_1", 1),
        Container("Thistle_1 (1)", 1),
        Container("Thistle_1", 1),
        Container("WildGarlic_1", 1),
        Container("Object_02", 2),
        Container("Plantain_1 (1)", 1),
    ],
    RegionValue.TheMirror: [
        Container("Rubbish_PlasticBag", 1),
        Container("WildGarlic_1 (1)", 1),
        Container("Rubbish_PlasticBottle", 1),
        Container("WildGarlic_1", 1),
        Container("BrokenClimbot_02", 5),
        Container("Bag_Top", 5),
        Container("Rubbish_PlasticBag (2)", 1),
        Container("Dandelion_Wall_1", 1),
        Container("Nettle_1", 1),
        Container("Juniper_1 (2)", 1),
        Container("Bag", 1),
        Container("Juniper_1", 1),
        Container("LootVolume", 1),
        Container("Bag_BearEntrance", 5),
        Container("LootVolume (2)", 1),
        Container("BearBox", 11),
        Container("Can_SparklingWater ", 1),
        Container("Raspberry_1 (1)", 1),
        Container("Thistle_Wall_1", 1),
        Container("Rubbish_PlasticBag (1)", 1),
        Container("BirdNest_1_Egg", 1),
        Container("BirdNest_1_Egg (1)", 1),
        Container("Dandelion_1 (1)", 1),
    ],
    RegionValue.TheTwoHundredSteps: [
        Container("Thistle_1", 1),
        Container("Thistle_Wall_1 (1)", 1),
        Container("Plantain_1", 1),
        Container("Nettle_1", 1),
        Container("WildGarlic_1", 1),
        Container("Juniper_Wall_1", 1),
        Container("BirdNest_1_Egg", 1),
        Container("BirdNest_1_Egg (1)", 1),
    ],
    RegionValue.ThePalaceofWind: [
        Container("Floor3_Lift_Bag", 3),
        Container("LootVolume", 1),
        Container("Floor2_Pot_02", 3),
        Container("Floor2_Rubbish_GlassBottle", 1),
        Container("Floor4_Right_Pot_02", 5),
        Container("PitonLootable", 1),
        Container("Floor3_Interior_Bag (1)", 3),
        Container("LootVolume (2)", 1),
        Container("BrokenPitonLoot", 1),
        Container("Mushroom_1", 1),
        Container("NPC_CHunter_Gameplay", 1),
        Container("LootVolume (3)", 1),
        Container("Floor2_Rubbish_Can", 1),
        Container("LootVolume (4)", 1),
        Container("LootVolume (5)", 1),
        Container("LootVolume (6)", 1),
        Container("LootVolume (7)", 1),
        Container("LootVolume (8)", 1),
        Container("Floor1_Left_Pot_01", 4),
        Container("Pit_Bag", 2),
        Container("PitonLootableCrystal", 1),
        Container("Bag", 3),
        Container("Juniper_1", 1),
        Container("Thistle_1", 1),
        Container("LootVolume (9)", 1),
        Container("Mushroom_1 (2)", 1),
        Container("Plantain_Wall_1", 1),
        Container("Bag (2)", 4),
        Container("Gentian_1", 1),
        Container("Pot_02", 2),
        Container("Pot_01 (1)", 2),
        Container("LootVolume (10)", 1),
        Container("BirdNest_3_Eggs", 1),
        Container("WildGarlic_Wall_1", 1),
        Container("Pot_02 (2)", 4),
        Container("LootVolume (11)", 1),
        Container("Mushroom_1 (3)", 1),
        Container("BrokenClimbot_01", 5),
        Container("Dandelion_Wall_1", 1),
        Container("PitonLootable (2)", 1),
        Container("PitonLootable (1)", 1),
    ],
    RegionValue.ThePeril: [
        Container("Bag (2)", 2),
        Container("Mushroom_1 (1)", 1),
        Container("Thistle_1", 1),
        Container("LootVolume", 1),
        Container("Bag (3)", 5),
        Container("Mushroom_1", 1),
        Container("Pot_01", 2),
        Container("Plantain_1", 1),
        Container("DeadBody_LootVolume", 3),
        Container("BirdNest_1_Egg", 1),
    ],
    RegionValue.TheDome: [
        Container("BrokenClimbot_01", 5),
        Container("Bag", 4),
        Container("DeadBody_LootVolume_Ridge", 5),
        Container("Dandelion_Wall_1", 1),
        Container("Juniper_Wall_1", 1),
        Container("Edelweiss", 1),
        Container("DeadBody_LootVolume (2)", 5),
        Container("FocusInteractionElement", 1),
        Container("Nettle_1", 1),
        Container("DeadBody_LootVolume", 2),
        Container("BirdNest_1_Egg (1)", 1),
        Container("BirdNest_1_Egg", 1),
        Container("DeadBody_LootVolume (1)", 3),
    ],
    RegionValue.TheNeedle: [
        Container("Plantain_1 (1)", 1),
        Container("Pot_01 (1)", 2),
        Container("Thistle_1 (2)", 1),
        Container("BrokenPitonLoot", 1),
        Container("Pot_01", 3),
        Container("Bag", 4),
        Container("WildGarlic_Wall_1", 1),
        Container("WildGarlic_1", 1),
        Container("Plantain_1", 1),
        Container("Pot_02", 3),
        Container("Juniper_1", 1),
        Container("Gentian_1", 1),
    ],
    RegionValue.TheSecret: [
        Container("Mushroom_1 (2)", 1),
        Container("Object_02", 1),
        Container("Pot_02", 2),
        Container("Juniper_1", 1),
        Container("NPC_Salamander_Oink", 1),
        Container("LootVolume", 1),
        Container("Object_01", 1),
        Container("Pot_01", 1),
        Container("PitonLootableCrystal", 1),
        Container("Pot_02 (1)", 3),
        Container("Mushroom_1 (3)", 1),
        Container("Mushroom_1", 1),
        Container("Pot_02 (2)", 3),
        Container("Pot_01 (2)", 2),
        Container("Rubbish_PlasticBag", 1),
        Container("Thistle_1 (2)", 1),
        Container("Pot_02 (1) (2)", 2),
        Container("DeadBody_LootVolume", 4),
        Container("Mushroom_1 (1)", 1),
        Container("LootVolume (2)", 1),
        Container("BrokenPitonLoot (1)", 1),
        Container("BrokenPitonLoot", 1),
        Container("LootVolume (3)", 1),
        Container("Bag", 5),
        Container("Pot_02 (3)", 1),
        Container("LootVolume (4)", 1),
        Container("LootVolume (5)", 1),
        Container("Bag (1)", 5),
        Container("Pot_01 (3)", 1),
        Container("BrokenPitonLoot (2)", 1),
        Container("HoneyPot", 1),
        Container("Bag (4)", 4),
        Container("Bag (3)", 2),
        Container("Tomato_Crate", 1),
        Container("BrokenPitonLoot (3)", 1),
    ],
    RegionValue.TheBlades: [],
    RegionValue.TheSeaOfSeracs: [],
    RegionValue.TheImmaculate: [],
    RegionValue.Kami: [],
}

TENZEN_LOOT = loot_locations_for_region(RegionValue.Tenzen)
THETWISTEDRIDGE_LOOT = loot_locations_for_region(RegionValue.TheTwistedRidge)
THEESCARPMENT_LOOT = loot_locations_for_region(RegionValue.TheEscarpment)
THEARCH_LOOT = loot_locations_for_region(RegionValue.TheArch)
THESHORTCUT_LOOT = loot_locations_for_region(RegionValue.TheShortcut)
THESPLITROCK_LOOT = loot_locations_for_region(RegionValue.TheSplitRock)
THEWATERFALL_LOOT = loot_locations_for_region(RegionValue.TheWaterfall)
THEVILLAGE_LOOT = loot_locations_for_region(RegionValue.TheVillage)
THESTANDINGSTONES_LOOT = loot_locations_for_region(RegionValue.TheStandingStones)
THECHILD_LOOT = loot_locations_for_region(RegionValue.TheChild)
THEVAULT_LOOT = loot_locations_for_region(RegionValue.TheVault)
THETERRACES_LOOT = loot_locations_for_region(RegionValue.TheTerraces)
THEMIRROR_LOOT = loot_locations_for_region(RegionValue.TheMirror)
THETWOHUNDREDSTEPS_LOOT = loot_locations_for_region(RegionValue.TheTwoHundredSteps)
THEPALACEOFWIND_LOOT = loot_locations_for_region(RegionValue.ThePalaceofWind)
THEPERIL_LOOT = loot_locations_for_region(RegionValue.ThePeril)
THEDOME_LOOT = loot_locations_for_region(RegionValue.TheDome)
THENEEDLE_LOOT = loot_locations_for_region(RegionValue.TheNeedle)
THESECRET_LOOT = loot_locations_for_region(RegionValue.TheSecret)
THEBLADES_LOOT = loot_locations_for_region(RegionValue.TheBlades)
THESEAOFSERACS_LOOT = loot_locations_for_region(RegionValue.TheSeaOfSeracs)
THEIMMACULATE_LOOT = loot_locations_for_region(RegionValue.TheImmaculate)
KAMI_LOOT = loot_locations_for_region(RegionValue.Kami)

LOCATION_NAME_TO_ID = {
    **TENZEN_LOOT,
    **THETWISTEDRIDGE_LOOT,
    **THEESCARPMENT_LOOT,
    **THEARCH_LOOT,
    **THESHORTCUT_LOOT,
    **THESPLITROCK_LOOT,
    **THEWATERFALL_LOOT,
    **THEVILLAGE_LOOT,
    **THESTANDINGSTONES_LOOT,
    **THECHILD_LOOT,
    **THEVAULT_LOOT,
    **THETERRACES_LOOT,
    **THEMIRROR_LOOT,
    **THETWOHUNDREDSTEPS_LOOT,
    **THEPALACEOFWIND_LOOT,
    **THEPERIL_LOOT,
    **THEDOME_LOOT,
    **THENEEDLE_LOOT,
    **THESECRET_LOOT,
    **THEBLADES_LOOT,
    **THESEAOFSERACS_LOOT,
    **THEIMMACULATE_LOOT,
    **KAMI_LOOT,
    "Summit": 1000000,
}


class CairnLocation(Location):
    game: str = "Cairn"


def create_all_locations(world: "CairnWorld"):
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: "CairnWorld"):
    tenzen = world.get_region(RegionValue.Tenzen.name)
    the_twisted_ridge = world.get_region(RegionValue.TheTwistedRidge.name)
    the_escarpment = world.get_region(RegionValue.TheEscarpment.name)
    the_arch = world.get_region(RegionValue.TheArch.name)
    the_shortcut = world.get_region(RegionValue.TheShortcut.name)
    the_split_rock = world.get_region(RegionValue.TheSplitRock.name)
    the_waterfall = world.get_region(RegionValue.TheWaterfall.name)
    the_village = world.get_region(RegionValue.TheVillage.name)
    the_standing_stones = world.get_region(RegionValue.TheStandingStones.name)
    the_child = world.get_region(RegionValue.TheChild.name)
    the_vault = world.get_region(RegionValue.TheVault.name)
    the_terraces = world.get_region(RegionValue.TheTerraces.name)
    the_mirror = world.get_region(RegionValue.TheMirror.name)
    the_two_hundred_steps = world.get_region(RegionValue.TheTwoHundredSteps.name)
    the_palace_of_wind = world.get_region(RegionValue.ThePalaceofWind.name)
    the_dome = world.get_region(RegionValue.TheDome.name)
    the_needle = world.get_region(RegionValue.TheNeedle.name)
    the_secret = world.get_region(RegionValue.TheSecret.name)
    the_blades = world.get_region(RegionValue.TheBlades.name)
    the_sea_of_seracs = world.get_region(RegionValue.TheSeaOfSeracs.name)
    the_immaculate = world.get_region(RegionValue.TheImmaculate.name)
    kami = world.get_region(RegionValue.Kami.name)

    tenzen.add_locations(TENZEN_LOOT, CairnLocation)
    the_twisted_ridge.add_locations(THETWISTEDRIDGE_LOOT)
    the_escarpment.add_locations(THEESCARPMENT_LOOT)
    the_arch.add_locations(THEARCH_LOOT)
    the_shortcut.add_locations(THESHORTCUT_LOOT)
    the_split_rock.add_locations(THESPLITROCK_LOOT)
    the_waterfall.add_locations(THEWATERFALL_LOOT)
    the_village.add_locations(THEVILLAGE_LOOT)
    the_standing_stones.add_locations(THESTANDINGSTONES_LOOT)
    the_child.add_locations(THECHILD_LOOT)
    the_vault.add_locations(THEVAULT_LOOT)
    the_terraces.add_locations(THETERRACES_LOOT)
    the_mirror.add_locations(THEMIRROR_LOOT)
    the_two_hundred_steps.add_locations(THETWOHUNDREDSTEPS_LOOT)
    the_palace_of_wind.add_locations(THEPALACEOFWIND_LOOT)
    the_dome.add_locations(THEDOME_LOOT)
    the_needle.add_locations(THENEEDLE_LOOT)
    the_secret.add_locations(THESECRET_LOOT)
    the_blades.add_locations(THEBLADES_LOOT)
    the_sea_of_seracs.add_locations(THESEAOFSERACS_LOOT)
    the_immaculate.add_locations(THEIMMACULATE_LOOT)
    kami.add_locations(KAMI_LOOT)


def create_events(world: "CairnWorld"):
    pass
