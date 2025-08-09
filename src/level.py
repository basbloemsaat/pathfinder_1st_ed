"""A level is a collection of attributes that encapsulate the
character's experience and abilities at a certain stage in their journey.
"""

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from character_class import CharacterClass


class Level(BaseModel):
    """A class representing a character's level increase."""

    class_: Annotated[CharacterClass, Field(description="The class of the level.")]
