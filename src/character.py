from pydantic import BaseModel
from race import RaceEnum
from ability import AbilityScores


class Character(BaseModel):
    name: str
    race: RaceEnum
    abilities: AbilityScores
