import pytest

from character import Character
from race import RaceEnum
from ability import AbilityScores
from character_class import ClassEnum


def test_character_creation():
    from alignment import AlignmentEnum
    from level import Level

    abilities = AbilityScores()
    char = Character(
        name="TestName",
        race=RaceEnum.HUMAN,
        abilities=abilities,
        levels=[Level(class_=ClassEnum.FIGHTER.value)],
        alignment=AlignmentEnum.TRUE_NEUTRAL,
    )
    assert char.name == "TestName"
    assert char.race == RaceEnum.HUMAN
    assert char.levels[0].class_.name == "Fighter"
    # Test abilities default
    assert hasattr(char, "abilities")
    # Check that all abilities are present and default to 0
    assert char.abilities.str.score == 0
    assert char.abilities.dex.score == 0
    assert char.abilities.con.score == 0
    assert char.abilities.int.score == 0
    assert char.abilities.wis.score == 0
    assert char.abilities.cha.score == 0


def test_character_invalid_race():
    from alignment import AlignmentEnum
    from level import Level

    abilities = AbilityScores()
    with pytest.raises(ValueError):
        Character(
            name="TestName",
            race=RaceEnum("INVALID"),
            abilities=abilities,
            levels=[Level(class_=ClassEnum.FIGHTER.value)],
            alignment=AlignmentEnum.TRUE_NEUTRAL,
        )


def test_character_invalid_class():
    from alignment import AlignmentEnum
    from level import Level

    abilities = AbilityScores()
    with pytest.raises(ValueError):
        Character(
            name="TestName",
            race=RaceEnum.HUMAN,
            abilities=abilities,
            levels=[Level(class_="INVALID")],
            alignment=AlignmentEnum.TRUE_NEUTRAL,
        )
