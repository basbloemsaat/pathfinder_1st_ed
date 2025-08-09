import pytest

from character import Character
from race import RaceEnum
from ability import AbilityScores
from character_class import ClassEnum



def test_character_creation():
    abilities = AbilityScores()
    char = Character(
        name="TestName",
        race=RaceEnum.HUMAN,
        abilities=abilities,
        character_class=ClassEnum.FIGHTER
    )
    assert char.name == "TestName"
    assert char.race == RaceEnum.HUMAN
    assert char.character_class == ClassEnum.FIGHTER
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
        Character(name="TestName", race="INVALID", abilities=abilities, character_class=ClassEnum.FIGHTER)


def test_character_invalid_class():
    abilities = AbilityScores()
    with pytest.raises(ValueError):
        Character(name="TestName", race=RaceEnum.HUMAN, abilities=abilities, character_class="INVALID")
