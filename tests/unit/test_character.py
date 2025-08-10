import pytest

from character import Character
from race import Race_
from ability import AbilityScores
from character_class import Class_

from categories import Alignment
from level import Level


def test_character_creation():
    abilities = AbilityScores()
    char = Character(
        name="TestName",
        race=Race_.HUMAN,
        abilities=abilities,
        levels=[Level(class_=Class_.FIGHTER.value)],
        alignment=Alignment.TRUE_NEUTRAL,
    )
    assert char.name == "TestName"
    assert char.race == Race_.HUMAN
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
    abilities = AbilityScores()
    with pytest.raises(ValueError):
        Character(
            name="TestName",
            race=Race_("INVALID"),
            abilities=abilities,
            levels=[Level(class_=Class_.FIGHTER.value)],
            alignment=Alignment.TRUE_NEUTRAL,
        )


def test_character_invalid_class():
    abilities = AbilityScores()
    with pytest.raises(ValueError):
        Character(
            name="TestName",
            race=Race_.HUMAN,
            abilities=abilities,
            levels=[Level(class_="INVALID")],
            alignment=Alignment.TRUE_NEUTRAL,
        )
