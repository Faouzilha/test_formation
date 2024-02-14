#######################################################################
#
#          Functions
#
#
#######################################################################
def estTermine(text):
    if text ==  "exit":
        return True
    return False

def calculerSomme(tab):
    somme = 0
    for i in range(len(tab)):
        somme = somme + tab[i]
    return somme

def calculerMoyenne(tab):
    return calculerSomme(tab) / len(tab)

def additionner(a,b):
    return a+b

def multiplier(a,b):
    return a*b

def diviser(a,b):
    return a/b

def diviser(a, b):
    if b == 0: #Si b = none
        return 0 
    return a / b # retourne none et retourne a/b
