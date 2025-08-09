from pydantic import BaseModel, Field
from saving_throw import SaveProgressionSpeed
from typing import Annotated


class ClassSavingThrow(BaseModel):
    fortitude: Annotated[
        SaveProgressionSpeed,
        Field(
            description="The progression speed for the Fortitude saving throw.",
        ),
    ]
    reflex: Annotated[
        SaveProgressionSpeed,
        Field(
            description="The progression speed for the Reflex saving throw.",
        ),
    ]
    will: Annotated[
        SaveProgressionSpeed,
        Field(
            description="The progression speed for the Will saving throw.",
        ),
    ]


class CharacterClass(BaseModel):
    name: Annotated[
        str,
        Field(description="The name of the character class."),
    ]
    description: Annotated[
        str,
        Field(description="A brief description of the character class."),
    ]
    hit_die: Annotated[
        int,
        Field(
            description="The hit die for the character class, used for calculating hit points.",
        ),
    ]
    primary_ability: Annotated[
        str,
        Field(
            description="The primary ability score that defines the character class.",
        ),
    ]
    saving_throws: Annotated[
        ClassSavingThrow,
        Field(
            description="The saving throw progressions for the character class.",
        ),
    ]
    skills: Annotated[
        list[str],
        Field(description="List of skills available to the character class."),
    ]
    equipment: Annotated[
        list[str],
        Field(description="Starting equipment for the character class."),
    ]
