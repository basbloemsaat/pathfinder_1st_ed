from pydantic import BaseModel, Field
from race import RaceEnum


class Character(BaseModel):
    name: str
    character_class: str
    level: int = 0
    hit_points: int = 0
    # race:
