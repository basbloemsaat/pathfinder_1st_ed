import pytest
from character import Character
from race import RaceEnum


def test_character_creation():
    char = Character(name="TestName", race=RaceEnum.HUMAN)
    assert char.name == "TestName"
    assert char.race == RaceEnum.HUMAN


def test_character_invalid_race():
    with pytest.raises(ValueError):
        Character(name="TestName", race="INVALID")
