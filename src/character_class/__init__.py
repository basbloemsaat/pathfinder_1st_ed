from pydantic import BaseModel, Field
from saving_throw import SaveProgressionSpeed


class ClassSavingThrow(BaseModel):
    fortitude: SaveProgressionSpeed = Field(
        ...,
        description="The progression speed for the Fortitude saving throw.",
    )
    reflex: SaveProgressionSpeed = Field(
        ...,
        description="The progression speed for the Reflex saving throw.",
    )
    will: SaveProgressionSpeed = Field(
        ...,
        description="The progression speed for the Will saving throw.",
    )


class CharacterClass(BaseModel):
    name: str = Field(..., description="The name of the character class.")
    description: str = Field(
        ..., description="A brief description of the character class."
    )
    hit_die: int = Field(
        ...,
        description="The hit die for the character class, used for calculating hit points.",
    )
    primary_ability: str = Field(
        ..., description="The primary ability score that defines the character class."
    )

    saving_throws: ClassSavingThrow = Field(
        ...,
        description="The saving throw progressions for the character class.",
    )

    skills: list[str] = Field(
        ..., description="List of skills available to the character class."
    )
    equipment: list[str] = Field(
        ..., description="Starting equipment for the character class."
    )
