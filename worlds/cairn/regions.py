from __future__ import annotations

from enum import Enum, auto
from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import CairnWorld


class RegionValue(Enum):
    Tenzen = auto()
    TheTwistedRidge = auto()
    TheEscarpment = auto()
    TheArch = auto()
    TheShortcut = auto()
    TheSplitRock = auto()
    TheWaterfall = auto()
    TheVillage = auto()
    TheStandingStones = auto()
    TheChild = auto()
    TheVault = auto()
    TheTerraces = auto()
    TheMirror = auto()
    TheTwoHundredSteps = auto()
    ThePalaceofWind = auto()
    ThePeril = auto()
    TheDome = auto()
    TheNeedle = auto()
    TheSecret = auto()
    TheBlades = auto()
    TheSeaOfSeracs = auto()
    TheImmaculate = auto()
    Kami = auto()


def create_and_connect_regions(world: CairnWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: CairnWorld) -> None:
    world.multiworld.regions += [Region(region.name, world.player, world.multiworld) for region in RegionValue]


def connect_regions(world: CairnWorld) -> None:
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

    tenzen.connect(the_twisted_ridge)
    the_twisted_ridge.connect(the_escarpment)
    the_escarpment.connect(the_arch)

    the_arch.connect(the_shortcut)
    the_arch.connect(the_split_rock)
    the_shortcut.connect(the_waterfall)
    the_split_rock.connect(the_waterfall)

    the_waterfall.connect(the_village)
    the_village.connect(the_standing_stones)

    the_standing_stones.connect(the_vault)
    the_standing_stones.connect(the_terraces)
    the_standing_stones.connect(the_child)
    the_vault.connect(the_terraces)
    the_child.connect(the_terraces)

    the_terraces.connect(the_mirror)
    the_mirror.connect(the_two_hundred_steps)
    the_two_hundred_steps.connect(the_palace_of_wind)
    the_palace_of_wind.connect(the_dome)
    the_dome.connect(the_needle)
    the_needle.connect(the_secret)
    the_secret.connect(the_blades)
    the_blades.connect(the_sea_of_seracs)
    the_sea_of_seracs.connect(the_immaculate)
    the_immaculate.connect(kami)
