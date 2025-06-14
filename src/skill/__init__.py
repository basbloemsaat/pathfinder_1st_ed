from pydantic import BaseModel, Field


class Skill(BaseModel):
    name: str = Field(..., description="The name of the skill.")
    description: str = Field(
        ..., description="A brief description of the skill and its uses."
    )
    ability_score: str = Field(
        ..., description="The primary ability score associated with the skill."
    )
    untrained: bool = Field(
        False, description="Whether the skill can only be used if trained."
    )
    armor_check_penalty: bool = Field(
        False, description="Whether the skill is affected by armor check penalties."
    )
