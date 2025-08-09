import pytest
from race import Race, races, Races


def test_races_dict_keys():
    # Check that all expected races are present
    expected = {"Dwarf", "Elf", "Gnome", "Half-elf", "Halfling", "Half-orc", "Human"}
    assert expected.issubset(set(races.keys()))


def test_race_model_fields():
    # Check that a race has all required fields and correct types
    dwarf = races["Dwarf"]
    assert isinstance(dwarf, Race)
    assert dwarf.name == "Dwarf"
    assert isinstance(dwarf.ability_score_plus, list)
    assert all(isinstance(x, str) for x in dwarf.ability_score_plus)
    assert isinstance(dwarf.ability_score_minus, list)
    assert all(isinstance(x, str) for x in dwarf.ability_score_minus)
    assert isinstance(dwarf.size, str)
    assert isinstance(dwarf.type_subtype, str)
    assert isinstance(dwarf.speed, int)
    assert isinstance(dwarf.starting_languages, list)
    assert all(isinstance(x, str) for x in dwarf.starting_languages)
    assert isinstance(dwarf.race_points, int)


def test_races_enum():
    # Check that the Races enum works and returns a Race
    assert isinstance(Races.HUMAN.value, Race)
    assert Races.HUMAN.value.name == "Human"
