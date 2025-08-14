"""Items.

Gear, magic items, and other equipment. Weapons, armor, and adventuring gear fall into this category.
"""

import json
from enum import StrEnum, Enum

from pydantic import BaseModel


class WearLocation(StrEnum):
    HEAD = "head"
    HEADBAND = "headband"
    EYES = "eyes"
    SHOULDERS = "shoulders"
    NECK = "neck"
    CHEST = "chest"
    BODY = "body"
    ARMOR = "armor"
    BELT = "belt"
    WRIST = "wrist"
    HANDS = "hands"
    FINGER = "finger"
    FEET = "feet"


class Item(BaseModel):
    name: str
    description: str
    item_type: str
    weight: str | float
    cost: str | int | float
    location: WearLocation | None = None


class Weapon(Item):
    damage: str
    range: str
    use_category: str
    weapon_type: str
    masterwork: bool = False


class Armor(Item):
    ac_bonus: int
    max_dex_bonus: int
    armor_type: str


class MagicItem(BaseModel):
    school: str


weapons: dict[str, Weapon] = {}
with open("data/tables/Weapons.json") as f:
    weapons_data = json.load(f)

for weapon_data in weapons_data:
    weapons[weapon_data["Weapon"]] = Weapon(
        name=weapon_data["Weapon"],
        description=weapon_data.get("Description", ""),
        item_type="weapon",
        weight=weapon_data.get("Weight"),
        cost=weapon_data.get("Cost", ""),
        location=(
            WearLocation[weapon_data.get("Location")]
            if weapon_data.get("Location")
            else None
        ),
        damage=weapon_data.get("Dmg (M)"),
        range=weapon_data.get("Range"),
        use_category=weapon_data.get("Use Category"),
        weapon_type=weapon_data.get("Type"),
    )

weapons_ = Enum("Weapons", {w.name: w for w in weapons.values()})
