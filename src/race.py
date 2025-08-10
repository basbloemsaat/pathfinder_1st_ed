import json
from pydantic import BaseModel
from typing import Optional

from enum import Enum


class Race(BaseModel):
    name: str
    ability_score_plus: list[str]
    ability_score_minus: list[str]
    size: str
    race_type: str
    subtype: list[str]
    speed: int
    starting_languages: list[str]
    senses: Optional[str]
    defensive_traits: Optional[list[str]]
    offensive_traits: Optional[list[str]]
    weapon_familiarity_proficiency: Optional[list[str]]
    skill_bonuses: Optional[list[str]]
    bonus_feats: list[str]
    spell_like_or_supernatural_abilities: Optional[list[str]]
    race_points: int


races: dict[str, Race] = {}
with open("data/tables/Core Races.json") as f:
    race_data = json.load(f)
    for race in race_data:
        races[race["Race"]] = Race(
            name=race["Race"],
            ability_score_plus=race["Ability Score Plus"],
            ability_score_minus=race["Ability Score Minus"],
            size=race["Size"],
            race_type=race["Type"],
            subtype=race["Subtype"],
            speed=int(race["Speed"].split()[0]),
            starting_languages=race["Starting Languages"],
            senses=race.get("Senses"),
            defensive_traits=race.get("Defensive Traits"),
            offensive_traits=race.get("Offensive Traits"),
            weapon_familiarity_proficiency=race.get("Weapon Familiarity Proficiency"),
            skill_bonuses=race.get("Skill Bonuses"),
            bonus_feats=race.get("Bonus Feats", []),
            spell_like_or_supernatural_abilities=race.get(
                "Spell-Like (Sp) or Supernatural (Su) Abilities"
            ),
            race_points=int(race["Race Points"]),
        )


class Race_(Enum):
    DWARF = races["Dwarf"]
    ELF = races["Elf"]
    GNOME = races["Gnome"]
    HALFELF = races["Half-elf"]
    HALFLING = races["Halfling"]
    HALFORC = races["Half-orc"]
    HUMAN = races["Human"]
