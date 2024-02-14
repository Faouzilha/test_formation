# Module Calculatrice

"""Additionne, soustrait ..."""

def addition(a: float, b: float) -> float:
    """Additionne"""
    return a + b

def soustraction(a: float, b: float) -> float:
    return a - b

def multiplication(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division par zéro impossible"

def calculatrice() -> None:
    while True:
        print("Faites votre choix")
        print("1. Addition")
        print("2. Soustraction")
        print("3. multiplication")
        print("4. division")
        print("5. Quitter")

        choix = input("Entrez votre choix (1-5)")

        if choix == '5':
            break

        if choix in ('1', '2', '3', '4'):
            a = float(input("Entrez le premier nombre"))
            b = float(input("Entrez le deuxieme nombre"))
            if choix == '1':
                print("Resultat", addition(a, b))
            elif choix == '2':
                print("Resultat", soustraction(a, b))
            elif choix == '3':
                print("Resultat", multiplication(a, b))
            elif choix == '4':
                print("Resultat", division(a, b))
        else:
            print("Choix non valide")