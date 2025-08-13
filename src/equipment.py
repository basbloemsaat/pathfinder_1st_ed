"""Items.

Gear, magic items, and other equipment. Weapons, armor, and adventuring gear fall into this category.
"""

from pydantic import BaseModel
from enum import StrEnum


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
    weight: float
    value: float
    location: WearLocation | None = None


class Weapon(Item):
    damage: str
    range: str
    weapon_type: str
    masterwork: bool


class Armor(Item):
    ac_bonus: int
    max_dex_bonus: int
    armor_type: str


class MagicItem(BaseModel):
    school: str
