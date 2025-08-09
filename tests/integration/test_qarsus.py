import pytest
from character import Character
from race import RaceEnum
from ability import AbilityScores


@pytest.fixture
def character() -> Character:
    return Character(name="Qarsus", race=RaceEnum.HUMAN, abilities=AbilityScores())


def test_character_creation(character: Character):
    assert character.race == RaceEnum.HUMAN
    assert character.abilities is not None
    assert character.abilities.str.score == 0
    assert character.abilities.dex.score == 0
    assert character.abilities.con.score == 0
    assert character.abilities.int.score == 0
    assert character.abilities.wis.score == 0
    assert character.abilities.cha.score == 0
    assert character.name == "Qarsus"


def test_character_abilities(character: Character):
    character.abilities.str.score = 16
    character.abilities.dex.score = 14

    # Check that the abilities are set correctly
    assert character.abilities.str.score == 16
    assert character.abilities.dex.score == 14
    # Check modifiers
    assert character.abilities.str.modifier == 3
    assert character.abilities.dex.modifier == 2
