import json
from pydantic import BaseModel
from typing import Optional

from enum import Enum


class School(BaseModel):
    name: str
    description: Optional[str] = None
    spells: list[str] = []


_schools: dict[str, School] = {}
with open("data/tables/Magic Schools.json") as f:
    data = json.load(f)
    for item in data:
        school = School(
            name=item.get("Name"),
            description=item.get("Description"),
        )
        _schools[school.name] = school


class School_(Enum):
    ABJURATION = _schools["Abjuration"]
    CONJURATION = _schools["Conjuration"]
    DIVINATION = _schools["Divination"]
    ENCHANTMENT = _schools["Enchantment"]
    EVOCATION = _schools["Evocation"]
    ILLUSION = _schools["Illusion"]
    NECROMANCY = _schools["Necromancy"]
    TRANSMUTATION = _schools["Transmutation"]
