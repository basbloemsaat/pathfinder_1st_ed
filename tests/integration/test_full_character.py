import pytest
from character import Character
from race import RaceEnum
from ability import AbilityScores

from character_class import ClassEnum
import exceptions
from alignment import AlignmentEnum
from level import Level


@pytest.fixture
def character() -> Character:

    character = Character(
        name="Qarsus",
        race=RaceEnum.HUMAN,
        abilities=AbilityScores(),
        levels=[Level(class_=ClassEnum.DRUID.value)],
        alignment=AlignmentEnum.TRUE_NEUTRAL,
    )
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


def test_character_class(character: Character):
    # Check that the character class is set correctly (first level)
    assert character.levels[0].class_.name == "Druid"

    druid = character.levels[0].class_
    assert druid.name == "Druid"
    assert druid.description.startswith(
        "The druid is a worshiper of all things natural"
    )
    assert druid.hit_die == "d8"
    from alignment import AlignmentEnum

    assert druid.allowed_alignments == {
        AlignmentEnum.NEUTRAL_GOOD,
        AlignmentEnum.TRUE_NEUTRAL,
        AlignmentEnum.NEUTRAL_EVIL,
    }
    assert "Handle Animal" in druid.class_skills
    assert "Spellcraft" in druid.class_skills
    assert druid.skill_ranks_per_level == 4
    assert druid.starting_wealth == "2d6 x 10 gp"
    assert druid.average_starting_wealth == "70 gp"


def test_character_invalid_alignment(character: Character):

    with pytest.raises(exceptions.AlignmentError):
        character.alignment = AlignmentEnum.LAWFUL_GOOD
