from pydantic import BaseModel, model_validator
from race import RaceEnum
from ability import AbilityScores
from character_class import ClassEnum
from typing_extensions import Self
from exceptions import AlignmentError


class Character(BaseModel):
    name: str
    race: RaceEnum
    abilities: AbilityScores
    character_class: ClassEnum

    @model_validator(mode="after")
    def validate_alignment(self) -> Self:
        """Validate the character's alignment."""

        return self
