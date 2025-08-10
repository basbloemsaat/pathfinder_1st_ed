from character_class import CharacterClass, Class_, character_classes


def test_character_class_fields():
    # Test that at least one class exists
    assert "Wizard" in character_classes
    wizard = character_classes["Wizard"]
    assert isinstance(wizard, CharacterClass)
    assert wizard.name == "Wizard"
    assert isinstance(wizard.description, str)
    assert isinstance(wizard.hit_die, str)
    assert isinstance(wizard.allowed_alignments, set)
    assert isinstance(wizard.class_skills, list)
    assert isinstance(wizard.skill_ranks_per_level, int)
    assert isinstance(wizard.starting_wealth, str)
    assert isinstance(wizard.average_starting_wealth, str)


def test_character_classes_dict():
    # Test that all entries in character_classes are CharacterClass instances
    for cls in character_classes.values():
        assert isinstance(cls, CharacterClass)


def test_class_enum_members():
    # Ensure all ClassEnum members are present in character_classes and are CharacterClass instances

    for member in Class_:
        # The value of each member should be a CharacterClass instance
        assert isinstance(member.value, CharacterClass)
        # The name of the class should be in character_classes
        assert member.value.name in character_classes
        # The object in character_classes should be the same as the enum value
        assert character_classes[member.value.name] is member.value


def test_class_skills_are_lists():
    for cls in character_classes.values():
        assert isinstance(cls.class_skills, list)
        for skill in cls.class_skills:
            assert isinstance(skill, str)


def test_skill_ranks_per_level_is_int():
    for cls in character_classes.values():
        assert isinstance(cls.skill_ranks_per_level, int)


def test_starting_wealth_and_average_are_strings():
    for cls in character_classes.values():
        assert isinstance(cls.starting_wealth, str)
        assert isinstance(cls.average_starting_wealth, str)
