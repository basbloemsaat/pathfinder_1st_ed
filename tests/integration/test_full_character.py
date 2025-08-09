import pytest
from character import Character
from race import RaceEnum
from ability import AbilityScores


@pytest.fixture
def character() -> Character:
    character = Character(name="Qarsus", race=RaceEnum.HUMAN, abilities=AbilityScores())
    character.abilities.str.score = 16
    character.abilities.dex.score = 14
    character.abilities.con.score = 12
    character.abilities.int.score = 10
    character.abilities.wis.score = 8
    character.abilities.cha.score = 6

    return character


def test_character_base(character: Character):
    assert character.name == "Qarsus"
    assert character.race == RaceEnum.HUMAN


def test_character_abilities(character: Character):
    # Check that abilities are set correctly
    assert character.abilities is not None
    assert character.abilities.str.score == 16
    assert character.abilities.dex.score == 14
    assert character.abilities.con.score == 12
    assert character.abilities.int.score == 10
    assert character.abilities.wis.score == 8
    assert character.abilities.cha.score == 6

    # Check modifiers
    assert character.abilities.str.modifier == 3
    assert character.abilities.dex.modifier == 2
    assert character.abilities.con.modifier == 1
    assert character.abilities.int.modifier == 0
    assert character.abilities.wis.modifier == -1
    assert character.abilities.cha.modifier == -2
