from ability import Ability, AbilityScore, AbilityScores


def test_ability_enum():
    assert Ability.STR.value == "Strength"
    assert Ability.DEX.value == "Dexterity"
    assert Ability.CON.value == "Constitution"
    assert Ability.INT.value == "Intelligence"
    assert Ability.WIS.value == "Wisdom"
    assert Ability.CHA.value == "Charisma"


def test_ability_score_modifier():
    assert AbilityScore(ability=Ability.STR, score=10).modifier == 0
    assert AbilityScore(ability=Ability.STR, score=12).modifier == 1
    assert AbilityScore(ability=Ability.STR, score=8).modifier == -1
    assert AbilityScore(ability=Ability.STR, score=1).modifier == -5
    assert AbilityScore(ability=Ability.STR, score=20).modifier == 5


def test_ability_scores_defaults():
    scores = AbilityScores()
    assert scores.str.ability == Ability.STR
    assert scores.dex.ability == Ability.DEX
    assert scores.con.ability == Ability.CON
    assert scores.int.ability == Ability.INT
    assert scores.wis.ability == Ability.WIS
    assert scores.cha.ability == Ability.CHA
    assert scores.str.score == 0
    assert scores.cha.score == 0
