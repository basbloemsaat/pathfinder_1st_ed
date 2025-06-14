from enum import Enum


class SaveProgressionSpeed(Enum):
    SLOW = (0, 3)
    FAST = (2, 2)


def level_saving_throw(level: int, progression: SaveProgressionSpeed) -> int:
    """
    Calculate the saving throw for a given level.
    """

    save = progression.value[0] + level // progression.value[1]

    return save
