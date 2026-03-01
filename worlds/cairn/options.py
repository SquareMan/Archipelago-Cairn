from __future__ import annotations

from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle


class KeepStartingItems(Toggle):
    """
    When disabled, all starting items (chalk bag, flask, pitons, etc.) will be disabled and added to the item pool
    """

    display_name = "Keep Starting Items"
    default = 1


@dataclass
class CairnOptions(PerGameCommonOptions):
    # TODO: Implement this on the client
    # keep_starting_items: KeepStartingItems
    pass
