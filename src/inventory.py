from pydantic import BaseModel, Field

from equipment import Item


class Inventory(BaseModel):
    items: list[Item] = Field(default_factory=lambda: [])
