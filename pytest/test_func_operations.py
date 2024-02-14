#!pip install pytest

from func import additionner
from func import multiplier
from func import diviser

def test_additionnerPositifs():
    valeur_a = 10
    valeur_b = 15    
    valeur_attendue = 25
    valeur_obtenue = additionner(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue


def test_additionnerPositifEtNegatif():
    valeur_a = -10
    valeur_b = 15    
    valeur_attendue = 5
    valeur_obtenue = additionner(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue


def test_additionnerNegatifs():
    valeur_a = -10
    valeur_b = -15 
    valeur_attendue = -25
    valeur_obtenue = additionner(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue

def test_multiplierPositifs():
    valeur_a = 10
    valeur_b = 5
    valeur_attendue = 50
    valeur_obtenue = multiplier(valeur_a, valeur_b)
    assert valeur_attendue == valeur_obtenue

def test_multiplierNegatifs():     
    valeur_a = -10     
    valeur_b = -15      
    valeur_attendue = 150     
    valeur_obtenue = multiplier (valeur_a, valeur_b)     
    assert valeur_attendue == valeur_obtenue

    
def test_diviserPositifs():
    valeur_a = 20
    valeur_b = 5
    valeur_attendue = 4 
    valeur_obtenue = diviser(valeur_a, valeur_b) 
    assert valeur_attendue == valeur_obtenue

def test_diviserNegatifs():
    valeur_a = -10
    valeur_b = -15
    valeur_attendue = 0.6666666666666666  
    valeur_obtenue = diviser(valeur_a, valeur_b) 
    assert valeur_attendue == valeur_obtenue