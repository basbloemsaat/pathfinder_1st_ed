from pydantic import BaseModel, Field



class Race(BaseModel):
    name: str
    speed: int
    ability_bonuses: dict[str, int]
    features: list[str]