import json
from pydantic import BaseModel
from typing import Optional

from enum import Enum


class Race(BaseModel):
    name: str
    ability_score_plus: list[str]
    ability_score_minus: list[str]
    size: str
    type_subtype: str
    speed: int
    starting_languages: list[str]
    senses: Optional[str]
    defensive_traits: Optional[list[str]]
    offensive_traits: Optional[list[str]]
    skill_bonuses: Optional[list[str]]
    bonus_feats: Optional[str]
    spell_like_or_supernatural_abilities: Optional[list[str]]
    race_points: int


races = {}
with open("data/tables/Core Races.json") as f:
    race_data = json.load(f)

    for race in race_data:
        races[race["Race"]] = Race(
            name=race["Race"],
            speed=int(race["Speed"].split()[0]),
            ability_score_plus=race["Ability Score Plus"],
            ability_score_minus=race["Ability Score Minus"],
            size=race["Size"],
            type_subtype=race["Type (subtype)"],
            starting_languages=race["Starting Languages"],
            senses=race["Senses"],
            defensive_traits=race["Defensive Traits"],
            offensive_traits=race["Offensive Traits"],
            skill_bonuses=race["Skill Bonuses"],
            bonus_feats=race["Bonus Feats"],
            spell_like_or_supernatural_abilities=race[
                "Spell-Like (Sp) or Supernatural (Su) Abilities"
            ],
            race_points=int(race["Race Points"]),
        )


class Races(Enum):
    HUMAN = races["Human"]
