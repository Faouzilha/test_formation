#!pip install pytest

from func import estTermine, calculerSomme, calculerMoyenne

def test_estTermine():
    valeur_entree = "exit"
    valeur_attendue = True
    valeur_obtenue = estTermine(valeur_entree)
    assert valeur_attendue == valeur_obtenue

def test_estNonTermine():
    valeur_entree = "pizza"
    valeur_attendue = False
    valeur_obtenue = estTermine(valeur_entree)
    assert valeur_attendue == valeur_obtenue


def test_calculerSommeTableauVide():
    tab = []
    valeur_attendue = 0
    valeur_obtenue = calculerSomme(tab)
    assert valeur_attendue == valeur_obtenue


def test_calculerSommeTableau5entiers():
    tab = [1,2,3,4,5]
    valeur_attendue = 15
    valeur_obtenue = calculerSomme(tab)
    assert valeur_attendue == valeur_obtenue

def test_calculerSommeTableau2entiers():
    tab = [10,13]
    valeur_attendue = 23
    valeur_obtenue = calculerSomme(tab)
    assert valeur_attendue == valeur_obtenue


def test_calculerMoyenneTableau10entiers():
    tab = [10,10,10,10,10,10,10,10,10,10]
    valeur_attendue = 10
    valeur_obtenue = calculerMoyenne(tab)
    assert valeur_attendue == valeur_obtenue


def test_calculerMoyenneTableau10entiers510():
    tab = [10,5,10,5,10,5,10,5,10,5]
    valeur_attendue = 7.5
    valeur_obtenue = calculerMoyenne(tab)
    assert valeur_attendue == valeur_obtenue
