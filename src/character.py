from pydantic import BaseModel, model_validator
from race import Race_
from ability import AbilityScores
from typing_extensions import Self
from categories import Alignment
from level import Level
from exceptions import AlignmentError


class Character(BaseModel, validate_assignment=True):
    name: str
    race: Race_
    abilities: AbilityScores
    levels: list[Level] = []
    alignment: Alignment

    # todo: inventory
    # todo: equipment / loadouts / weapons

    @model_validator(mode="after")
    def validate_alignment(self) -> Self:
        """Validate the character's alignment."""

        allowed_alignments = set(Alignment)

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
