import character_class
from saving_throw import SaveProgressionSpeed


def test_character_class__character_class():
    # Arrange
    testclass = character_class.CharacterClass(
        name="Test Class",
        description="A test class.",
        hit_die=12,
        primary_ability="Strength",
        saving_throws=character_class.ClassSavingThrow(
            fortitude=SaveProgressionSpeed.FAST,
            reflex=SaveProgressionSpeed.SLOW,
            will=SaveProgressionSpeed.SLOW,
        ),
        skills=["Athletics", "Survival", "Intimidation"],
        equipment=[
            "Greataxe or any martial melee weapon",
            "Two handaxes or any simple weapon",
            "Explorer's pack",
            "Four javelins",
        ],
    )

    # Assert
    assert testclass.name == "Test Class"
    assert testclass.description == "A test class."
    assert testclass.hit_die == 12
    assert testclass.primary_ability == "Strength"
    assert isinstance(testclass.saving_throws, character_class.ClassSavingThrow)
    assert testclass.saving_throws.fortitude == SaveProgressionSpeed.FAST
    assert testclass.saving_throws.reflex == SaveProgressionSpeed.SLOW
    assert testclass.saving_throws.will == SaveProgressionSpeed.SLOW
    assert testclass.skills == ["Athletics", "Survival", "Intimidation"]
    assert testclass.equipment == [
        "Greataxe or any martial melee weapon",
        "Two handaxes or any simple weapon",
        "Explorer's pack",
        "Four javelins",
    ]
