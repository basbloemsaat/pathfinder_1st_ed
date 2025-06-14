from character_class import CharacterClass, ClassSavingThrow
from saving_throw import SaveProgressionSpeed

barbarian = CharacterClass(
    name="Barbarian",
    description="A fierce warrior of primitive background who can enter a battle rage.",
    hit_die=12,
    primary_ability="Strength",
    saving_throws=ClassSavingThrow(
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
