from func import multiplier, diviser

def test_multiplierPositifs():
    valeur_a = 10
    valeur_b = 15    
    valeur_attendue = 150
    valeur_obtenue = multiplier(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue


def test_multiplierZero():
    valeur_a = 10
    valeur_b = 0    
    valeur_attendue = 0
    valeur_obtenue = multiplier(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue



def test_diviserZero():
    valeur_a = 10
    valeur_b = 0    
    valeur_attendue = None
    valeur_obtenue = diviser(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue
