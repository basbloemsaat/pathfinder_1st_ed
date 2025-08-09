from race import Race, races, RaceEnum


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
    assert isinstance(dwarf.race_type, str)
    assert isinstance(dwarf.subtype, list)
    assert all(isinstance(x, str) for x in dwarf.subtype)
    assert isinstance(dwarf.speed, int)
    assert isinstance(dwarf.starting_languages, list)
    assert all(isinstance(x, str) for x in dwarf.starting_languages)
    assert isinstance(dwarf.weapon_familiarity_proficiency, (list, type(None)))
    if dwarf.weapon_familiarity_proficiency:
        assert all(isinstance(x, str) for x in dwarf.weapon_familiarity_proficiency)
    assert isinstance(dwarf.race_points, int)


def test_races_enum():
    # Check that the Races enum works and returns a Race for all core races
    expected = {
        "DWARF": "Dwarf",
        "ELF": "Elf",
        "GNOME": "Gnome",
        "HALFELF": "Half-elf",
        "HALFLING": "Halfling",
        "HALFORC": "Half-orc",
        "HUMAN": "Human",
    }
    for enum_member, race_name in expected.items():
        race = getattr(RaceEnum, enum_member).value
        assert isinstance(race, Race)
        assert race.name == race_name
