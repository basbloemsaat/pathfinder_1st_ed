from pydantic import BaseModel, Field
from race import RaceEnum


class Character(BaseModel):
    name: str
    race: RaceEnum
