from calculatrice import* # Import tts les fonctions du module calculatrice. 
"""Additionne, soustrait ..."""

def addition(a: float, b: float) -> float: # : Fonction addition qui prend deux paramètres a et b de type float, et renvoie la somme en tant que float.
    """Additionne"""
    return a + b

def soustraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:# Fonction division 2 paramètres (a et b) de type float. Gère également le cas de division par zéro.
    if b != 0:
        return a / b
    return "Division par zero impossible"
  
def calculatrice() -> None: #  Fonction principale calculatrice qui permet à l'utilisateur d'effectuer des opérations
    while True: # Démarre une boucle infinie pour permettre à l'utilisateur de faire plusieurs calculs jusqu'à ce qu'il choisisse de quitter.
        print("Faites votre choix")
        print("1. Addition")
        print("2. Soustraction")
        print("3. multiplication")
        print("4. division")
        print("5. Quitter")

        choix = input("Entrez votre choix (1-5)") #  Demande à l'utilisateur de choisir une opération

        if choix == '5': # Si l'utilisateur choisit '5', la boucle est interrompue, permettant de quitter le programme.
            break

        if choix in ('1', '2', '3', '4'): #  Vérifie si le choix de l'utilisateur est parmi les opérations disponibles.

            a = float(input("Entrez le premier nombre")) # Demande à l'utilisateur d'entrer deux nombres.
            b = float(input("Entrez le deuxieme nombre"))

            if choix == '1': # Appelle la fonction appropriée en fonction du choix de l'utilisateur et affiche le résultat.
                print("Resultat", addition(a, b))
            elif choix == '2':
                print("Resultat", soustraction(a, b))
            elif choix == '3':
                print("Resultat", multiplication(a, b))
            elif choix == '4':
                print("Resultat", division(a, b))
        else:
            print("Choix non valide") # Affiche un message si le choix de l'utilisateur n'est pas valide.
# En résumé,  création d'une calculatrice simple et interactive avec un menu permettant d'effectuer des opérations de base.
# Les fonctions sont bien encapsulées, ce qui rend le code modulaire et facile à comprendre.