from typing import Annotated
from pydantic import BaseModel, Field


class Skill(BaseModel):
    name: Annotated[str, Field(description="The name of the skill.")]
    description: Annotated[
        str, Field(description="A brief description of the skill and its uses.")
    ]
    ability_score: Annotated[
        str, Field(description="The primary ability score associated with the skill.")
    ]
    untrained: Annotated[
        bool, Field(description="Whether the skill can only be used if trained.")
    ]
    armor_check_penalty: Annotated[
        bool,
        Field(description="Whether the skill is affected by armor check penalties."),
    ]


skill_list: dict[str, Skill] = {}
