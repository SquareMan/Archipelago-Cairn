from BaseClasses import ItemClassification
from worlds.AutoWorld import World

from . import items, locations, regions, rules
from .options import CairnOptions


class CairnWorld(World):
    game = "Cairn"
    origin_region_name = "Tenzen"

    options_dataclass = CairnOptions
    options: CairnOptions

    item_name_to_id = items.ITEM_NAME_TO_ID
    location_name_to_id = locations.LOCATION_NAME_TO_ID

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.CairnItem:
        return items.CairnItem(name, ItemClassification.filler, items.ITEM_NAME_TO_ID[name], self.player)

    item_name_groups = {
        "food": {item.name for item in items.FOOD},
        "drugs": {item.name for item in items.DRUGS},
        "gear": {item.name for item in items.GEAR},
        "maps": {item.name for item in items.MAPS},
        "reading material": {item.name for item in items.READING_MATERIAL},
        "trash": {item.name for item in items.TRASH},
    }
