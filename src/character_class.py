import json
from enum import Enum
from typing import Annotated

from pydantic import BaseModel, Field

from saving_throw import SaveProgressionSpeed
from alignment import AlignmentEnum


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
        str,
        Field(
            description="The hit die for the character class, used for calculating hit points."
        ),
    ]
    allowed_alignments: Annotated[
        set[AlignmentEnum],
        Field(
            description="Allowed alignments for the class. Empty list means any alignment is allowed."
        ),
    ]
    class_skills: Annotated[
        list[str],
        Field(description="List of skills available to the character class."),
    ]
    skill_ranks_per_level: Annotated[
        int,
        Field(description="Number of skill ranks gained per level."),
    ]
    starting_wealth: Annotated[
        str,
        Field(description="Starting equipment for the character class."),
    ]
    average_starting_wealth: Annotated[
        str,
        Field(description="Average starting wealth for the character class."),
    ]


character_classes: dict[str, CharacterClass] = {}
with open("data/tables/Character Classes.json") as f:
    class_data = json.load(f)
    for cls in class_data:
        character_classes[cls["Class"]] = CharacterClass(
            name=cls["Class"],
            description=cls["Description"],
            hit_die=cls["Hit die"],
            allowed_alignments=set(AlignmentEnum(a) for a in cls.get("Alignment", [])),
            class_skills=cls.get("Class Skills", []),
            skill_ranks_per_level=int(cls.get("Skill Ranks per Level", 0)),
            starting_wealth=cls.get("Starting Wealth", ""),
            average_starting_wealth=cls.get("Average Starting Wealth", ""),
        )


class ClassEnum(Enum):
    BARBARIAN = character_classes["Barbarian"]
    BARD = character_classes["Bard"]
    CLERIC = character_classes["Cleric"]
    DRUID = character_classes["Druid"]
    FIGHTER = character_classes["Fighter"]
    MONK = character_classes["Monk"]
    PALADIN = character_classes["Paladin"]
    RANGER = character_classes["Ranger"]
    ROGUE = character_classes["Rogue"]
    SORCERER = character_classes["Sorcerer"]
    WIZARD = character_classes["Wizard"]
