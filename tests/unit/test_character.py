import pytest

from character import Character
from race import Races
from ability import AbilityScores
from character_class import Classes

from categories import Alignments
from level import Level


def test_character_creation():
    abilities = AbilityScores()
    char = Character(
        name="TestName",
        race=Races.HUMAN,
        abilities=abilities,
        levels=[Level(class_=Classes.FIGHTER.value)],
        alignment=Alignments.TRUE_NEUTRAL,
    )
    assert char.name == "TestName"
    assert char.race == Races.HUMAN
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
            race=Races("INVALID"),
            abilities=abilities,
            levels=[Level(class_=Classes.FIGHTER.value)],
            alignment=Alignments.TRUE_NEUTRAL,
        )


def test_character_invalid_class():
    abilities = AbilityScores()
    with pytest.raises(ValueError):
        Character(
            name="TestName",
            race=Races.HUMAN,
            abilities=abilities,
            levels=[Level(class_="INVALID")],
            alignment=Alignments.TRUE_NEUTRAL,
        )
