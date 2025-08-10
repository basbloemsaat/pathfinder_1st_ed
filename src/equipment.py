"""Items.

Gear, magic items, and other equipment. Weapons, armor, and adventuring gear fall into this category.
"""

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    item_type: str
    weight: float
    value: float
    properties: dict


class Weapon(Item):
    damage: str
    range: str
    weapon_type: str
    masterwork: bool


class Armor(Item):
    ac_bonus: int
    max_dex_bonus: int
    armor_type: str


class MagicWeapon(Weapon):
    magic_bonus: int
