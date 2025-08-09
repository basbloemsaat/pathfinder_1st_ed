import pytest
from saving_throw import SaveProgressionSpeed, level_saving_throw


def test_save_progression_speed_enum():
    assert SaveProgressionSpeed.SLOW.value == (0, 3)
    assert SaveProgressionSpeed.FAST.value == (2, 2)


@pytest.mark.parametrize(
    "level,progression,expected",
    [
        (1, SaveProgressionSpeed.SLOW, 0),
        (3, SaveProgressionSpeed.SLOW, 1),
        (6, SaveProgressionSpeed.SLOW, 2),
        (1, SaveProgressionSpeed.FAST, 2),
        (2, SaveProgressionSpeed.FAST, 3),
        (4, SaveProgressionSpeed.FAST, 4),
        (10, SaveProgressionSpeed.FAST, 7),
    ],
)
def test_level_saving_throw(
    level: int, progression: SaveProgressionSpeed, expected: int
) -> None:
    assert level_saving_throw(level, progression) == expected
