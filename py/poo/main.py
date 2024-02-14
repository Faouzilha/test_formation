from poo.person import Person
from poo.student import Student
from poo.compteBancaire import CompteBancaire


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.display_info()
person2.display_info()

# création d'une liste d'instances Person
liste_persons = [
    Person("Alice", 25),
    Person("John", 25),
    Person("Pat", 25),
]

for person in liste_persons:
    person.display_info()
    print(person)

stu = Student("Alice", 25, "Informatique")
stu.display_info()
print(stu)


















# #! /usr/bin/env python3
# # coding: utf-8



# print("éléphant")  # print methode qui affiche en console (Terminal)

# print("-----------------------------------------------------------")

# n = "32" # Typage dynamique
# print("Le type de la variable n est ", type(n)) # retourne le type de la variable n
# print("Le type convertit de la variable n est ", type(int(n))) # int() convertira un str (chaine de caractères) en entier
# print("Le type convertit de la variable n est ", type(float(n))) # float() convertira un str (chaine de caractères) en reel

# print("-----------------------------------------------------------")

# name: str = "John"
# age: int = 32
# print("Le type de la variable name est ", type(name))
# print("Je m'appelle", name, "et j'ai", age, "ans", end='!\n')
# print(f'Je m appelle {name} et j ai {age} ans')

# print("Le type converti de la variable age est ", type(repr(age))) # repr() convertira n'importe quoi en str (chaine de caractères)

# print("-----------------------------------------------------------")

# print(5**2) # retourne la puisance de 5 par 2

# print(7//2) # retourne une division entiere

# isBool = False
# print(isBool)

# print("-----------------------------------------------------------")

# # Un tuple est immuable, non modfiable
# tuple1 = (1, 2, 3) # Groupage
# print(type(tuple1))
# print("Tuple", tuple1)
# print(tuple1[0]) # affiche 1
# print(tuple1[-1]) # affiche le dernier element du tuple

# print("-----------------------------------------------------------")

# a, b, c = tuple1 # Degroupage
# print("La valeur de a est", a)
# print("La valeur de b est", b)
# print("La valeur de c est", c)

# print("-----------------------------------------------------------")

# valeur_min = min(tuple1)
# valeur_max = max(tuple1)

# print("La valeur min est", valeur_min)
# print("La valeur max est", valeur_max)

# print("-----------------------------------------------------------")

# a, b = b, a # Permutation de valeur
# print("Apres permutation - La valeur de a est", a)
# print("Apres permutation - La valeur de b est", b)

# print("-----------------------------------------------------------")

# # Listes
# tableau = [1, 2, 4, 7, 5, 9, 5, 4]
# premier_element = tableau[0] # Accessible via leur index

# tableau[1] = 3 # Modification de la valeur dans latableau a l'index 1

# print(tableau)

# print("-----------------------------------------------------------")

# tableau.insert(1, 2)
# tableau.append(10) # insere les elements a la fin

# print(tableau)

# print("-----------------------------------------------------------")

# del tableau[2] # supprime selon l'index
# tableau.remove(10) # supprime selon l'element

# print(tableau)
# print(len(tableau))

# print("-----------------------------------------------------------")

# nouveau_tableau = list(set(tableau)) # set() enleve le doublon

# for indice, element in enumerate(nouveau_tableau):
#     print(indice, element)

# print("-----------------------------------------------------------")

# # Un dictionnaire est une structure de donnees qui permet de stocker 
# # des paires cles-valeurs
# dico = {1:"Lundi", 2:"Mardi", 3:"Mercredi", 4:"Jeudi", 5:"Vendredi"}

# print(dico[1]) # Accede aux elements du dictionnaire

# print("-----------------------------------------------------------")

# dico[6] = "Samedi" # Ajoute une nouvelle paire clé-valeur

# del dico[5] # supprime un paire clé-valeur

# # Itere sur les cles et valeur du dictionnaire
# for cle, valeur in dico.items():
#     print(f'{cle} {valeur}')

# print("-----------------------------------------------------------")

# # La fonction range()
# print(list(range(10)))

# print("-----------------------------------------------------------")

# tableau2 = list(range(5, 10, 2))
# print(tableau2)

# print("-----------------------------------------------------------")

# # input est utilise pour obtenir une chaine de caractere
# nom = input("Entrez votre nom, svp :")
# prenom = input("Entrez votre prenom, svp :")
# # Transtypage de la valeur saisie par l'utilisateur
# age = int(input("Entrez votre age, svp :"))

# print(f'{nom} {prenom} {age}')
# print("-----------------------------------------------------------")