from pydantic import BaseModel, model_validator
from race import RaceEnum
from ability import AbilityScores
from typing_extensions import Self
from alignment import AlignmentEnum
from level import Level
from exceptions import AlignmentError


class Character(BaseModel, validate_assignment=True):
    name: str
    race: RaceEnum
    abilities: AbilityScores
    levels: list[Level] = []
    alignment: AlignmentEnum

    @model_validator(mode="after")
    def validate_alignment(self) -> Self:
        """Validate the character's alignment."""

        allowed_alignments = set(AlignmentEnum)

        for level in self.levels:
            if level.class_.allowed_alignments == set():
                # if the class allows any alignment, we don't filter
                continue

            # remove any alignments not allowed by the character's class
            allowed_alignments.intersection_update(level.class_.allowed_alignments)

        if self.alignment not in allowed_alignments:
            raise AlignmentError(
                f"Alignment {self.alignment} is not allowed for this character."
            )

        return self
