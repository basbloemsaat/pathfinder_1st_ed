from enum import Enum
from pydantic import BaseModel


class Ability(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"


class AbilityScore(BaseModel):
    ability: Ability
    score: int = 0

    @property
    def modifier(self) -> int:
        """Calculate the ability modifier based on the score."""
        return (self.score - 10) // 2


class AbilityScores(BaseModel):
    str: AbilityScore = AbilityScore(ability=Ability.STR)
    dex: AbilityScore = AbilityScore(ability=Ability.DEX)
    con: AbilityScore = AbilityScore(ability=Ability.CON)
    int: AbilityScore = AbilityScore(ability=Ability.INT)
    wis: AbilityScore = AbilityScore(ability=Ability.WIS)
    cha: AbilityScore = AbilityScore(ability=Ability.CHA)
