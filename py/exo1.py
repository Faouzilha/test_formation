# Un enseignant attribue des notes en fonction de la moyenne des examens de ses étudiants. Les critères sont les suivants :

# Si la moyenne est inférieure à 10, l'étudiant est recalé.
# Si la moyenne est entre 10 et 12 inclus, l'étudiant obtient la mention "Passable".
# Si la moyenne est entre 12 (non inclus) et 14 inclus, l'étudiant obtient la mention "Assez bien".
# Si la moyenne est entre 14 (non inclus) et 16 inclus, l'étudiant obtient la mention "Bien".
# Si la moyenne est supérieure ou égale à 16, l'étudiant obtient la mention "Très bien".
# Écrire un algorithme en pseudo-code qui demande à l'utilisateur ses trois notes d'examens, qui calcule la moyenne, puis qui attribue une mention en fonction de la moyenne.

# Pseudo-code

# Algorithme CalculNoteFinale
# Variables note1, note2, note3, moyenne : reels
#          mention : Chaîne de caractères
# Début
#    Écrire("Entrez la première note : ")
#    Lire(note1)

#    Écrire("Entrez la deuxième note : ")
#    Lire(note2)

#    Écrire("Entrez la troisième note : ")
#    Lire(note3)

#    moyenne ← (note1 + note2 + note3) / 3

#    Selon (moyenne) Faire
#        Cas < 10 :
#            mention ← "Recalé"
#        Cas <= 12 :
#            mention ← "Passable"
#        Cas <= 14 :
#            mention ← "Assez bien"
#        Cas <= 16 :
#            mention ← "Bien"
#        Sinon
#            mention ← "Très bien"
#    FinSelon

#    Écrire("Votre moyenne est de ", moyenne, " et vous avez la mention : ", mention)
# Fin

# python - Solution avec if-elif-else

note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))

moyenne = (note1 + note2 + note3) / 3

if moyenne < 10:
    mention = "Recalé"
elif moyenne <= 12:
    mention = "Passable"
elif moyenne <= 14:
    mention = "Assez bien"
elif moyenne <= 16:
    mention = "Bien"
else:
    mention = "Très bien"

print("Votre moyenne est de", moyenne, "et vous avez la mention :", mention)

# Ecrire un algorithme qui détermine le premier nombre entier N tel que la somme
# de 1 à N dépasse strictement 100

# Pseudo-code

# Variables som, i : entier
# Debut
#   i ← 0
#   som ← 0
#   TantQue (som <= 100)
#       i ← i + 1
#       som ← som+i
#   FinTantQue
#   Ecrire (" La valeur cherchée est N= ", i)
# Fin

# python

som = 0
i = 0

# Première itération (i = 1, som = 1)
# Deuxieme itération (i = 2, som = 3)
# Troisieme itération (i = 3, som = 6)
# Quatrieme itération (i = 4, som = 10)
while som <= 100:
    i += 1
    som += i

print("La valeur cherchée est N =", i)
print("La somme est N =", som)

# Ecrire un algorithme qui demande un nombre de départ, et qui ensuite affiche les dix nombres suivants. 
# Par exemple, si l'utilisateur entre le nombre 17, le programme affichera les nombres de 18 à 27. 

# Pseudo-code

# Variables N, i en Entier 
# Debut 
#   Ecrire()"Entrez un nombre : ") 
#   Lire(N) 
#   i ← 0 
#   Ecrire ("Les 10 nombres suivants sont : ") 
#   TantQue i < 10    
#       i ← i + 1    
#       Ecrire(N + i) 
#   FinTantQue 
# Fin 

# python

N = 0
i = 0

N = int(input("Entrez un nombre : "))

print("Les 10 nombres suivants sont : ")
while i < 10:
    i = i + 1
    print(N + i)

# Réécrire l'algorithme précédent, en utilisant cette fois l'instruction Pour

# pseudo-code

# Variables N, i : entier 
# Debut 
#   Ecrire ("Entrez un nombre :")
#   Lire (N) 
#   Ecrire ("Les 10 nombres suivants sont : ") 
#   Pour i ← 1 à 10   
#       Ecrire (N + i)
#   FinPour
# Fin

# python

N, i = 0, 0

# Demander à l'utilisateur d'entrer un nombre
N = int(input("Entrez un nombre : "))

# Afficher les 10 nombres suivants
print("Les 10 nombres suivants sont : ")
for i in range(1, 11):
    print(N + i)

# Écrire un algorithme qui demande à l'utilisateur d'entrer un nombre entier positif 
# L'algorithme doit afficher tous les nombres pairs de 0 à N à l'aide d'une 
# boucle "tant que".

# Pseudo-code

# Variables N, i en Entier 
# Debut 
#   Ecrire()"Entrez un nombre entier positif : ") 
#   Lire(N) 
#   i ← 0 
#   Ecrire ("Les 10 nombres suivants sont : ") 
#   TantQue i <= N       
#       Ecrire(i)
#   i ← i + 2  
#   FinTantQue 
# Fin 

# python - Solution 1

N = int(input("Entrez un nombre entier positif : "))
i = 0

print("Les 10 nombres suivants sont : ")
while i <= N:
    print(i)
    i += 2

# python - Solution 2

N = int(input("Entrez un nombre entier positif : "))
i = 0

print("Tous les nombres pairs suivants sont : ")
while i <= N:
    if i % 2 == 0:  
        print(i)
    i = i + 1

# Ecrire un algorithme qui demande un nombre compris entre 10 et 20, 
# jusqu’à ce que la réponse convienne. 
# En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! »,
# et inversement, « Plus grand ! » si le nombre est inférieur à 10.

# Variable N : entier
# Debut 
#   N ← 0 
#   Ecrire ("Entrez un nombre entre 10 et 20")
#   Lire (N)   
#   TantQue N < 10 ou N > 20     
#       Si N < 10 Alors     
#           Ecrire("Plus grand !")   
#       SinonSi N > 20 Alors     
#           Ecrire ("Plus petit !") 
#       FinSi 
#   FinTantQue 
# Fin

while True:
    nombre = int(input("Entrez un nombre entre 10 et 20 : "))
    if nombre < 10:
        print("Plus grand !")
    elif nombre > 20:
        print("Plus petit !")
    else:
        break
    
print("Vous avez saisi un nombre valide entre 10 et 20. Merci !")

# Calcul de x à la puissance n où x est un réel non nul et n un entier positif ou null

# Pseudo-code

# Variables x, puiss : réel
# n, i : entier
# Debut
#   Ecrire (" Entrez la valeur de x ")
#   Lire (x)
#   Ecrire (" Entrez la valeur de n ")
#   Lire (n)
# La variable puiss est initialement definit a 1 , car elle est mulitpliee par la valeur de x "
# cela permet d'accumuler le resultat de x par lui-meme n fois, simulant la pussance de x^n
#   puiss ← 1
#   Pour i allant de 1 à n
#       puiss ← puiss * x
#   FinPour
#   Ecrire (x, " à la puissance ", n, " est égal à ", puiss)
# Fin

# python
x, puiss = 1.0, 1.0  # Initialisation de x et puiss à 1.0 pour les traiter comme des réels
n, i = 0, 0  # Initialisation de n et i à 0

# Demander à l'utilisateur la valeur de x
x = float(input("Entrez la valeur de x : "))

# Demander à l'utilisateur la valeur de n
n = int(input("Entrez la valeur de n : "))

# Calculer x à la puissance n
for i in range(1, n + 1):
    puiss *= x

# Afficher le résultat
print(x, " à la puissance ", n, " est égal à ", puiss)

# Autres solutions
# Methode pow(...) qui retourne la puissance de x par n
puiss2 = pow(x, n);
print(x, " à la puissance ", n, " est égal à ", puiss2)
# Operateur ** pour la puissance
puiss3 = x ** n;
print(x, " à la puissance ", n, " est égal à ", puiss3)

# Ecrire un algorithme qui demande un nombre de départ, et qui ensuite écrit la table de multiplication de ce nombre, 
# présentée comme suit (cas où l'utilisateur entre le nombre 7)

# Variables N, i : entier
# Debut 
#   Ecrire ("Entrez un nombre : ") 
#   Lire (N) 
#   Ecrire ("La table de multiplication de ce nombre est : ") 
#   Pour i ← 1 à 10   
#       Ecrire (N, " x ", i, " = ", n * i)
#   FinPour
# Fin 

N, i = 0, 0

N = int(input("Entrez un nombre : "))

print("La table de multiplication de", N, "est :")
for i in range(1, 11):
    print(N, "x", i, "=", N * i)

# Écrire un algorithme qui génère un nombre aléatoire entre 1 et 100 (inclus). 
# Ensuite, demandez à l'utilisateur de deviner ce nombre. 
# L'algorithme doit donner des indications (trop grand, trop petit) 
# jusqu'à ce que l'utilisateur devine le nombre. 
# Enfin, affichez le nombre de tentatives nécessaires pour deviner le nombre.

import random

tentative = 0
choix = 0
random = random.randint(1, 100)
print("Random :", random)

print("Bienvenue dans le jeu Zee Magic Number !!!")

while True:
    choix = int(input("Devinez un nombre entre 1 et 100"))
    tentative += 1

    if choix < random:
        print("Plus grand !")
    elif choix > random:
        print("Plus petit !")
    else:
        break
    
print("Bravo !!! Vous avez trouvé le nombre magique ", random, " en ", tentative)

# Ecrire un algorithme qui demande successivement 20 nombres à l’utilisateur, 
# et qui lui dise ensuite quel était le plus grand parmi ces 20 nombres : 
# Entrez le nombre numéro 1 : 12 
# Entrez le nombre numéro 2 : 14 etc. 
# Entrez le nombre numéro 20 : 6 
# Le plus grand de ces nombres est  : 14 

# Variables N, i, PG : Entier 
# Debut 
#   PG ← 0 
#   Pour i ← 1 à 20   
#       Ecrire ("Entrez un nombre : ")   
#       Lire (N)   
#       Si N > PG Alors    
#           PG ← N   
#       FinSi 
#   FinPour
#   Ecrire ("Le nombre le plus grand était : ", PG) 
# Fin

PG = 0

for i in range(1, 21):
    N = int(input("Entrez un nombre : "))
    if N > PG:
        PG = N

print("Le nombre le plus grand était :", PG)

# Écrire un algorithme qui demande à l'utilisateur d'entrer un nombre entier positif n. 
# L'algorithme doit calculer et afficher la somme des carrés des nombres de 1 à n.

# Par exemple, si l'utilisateur entre n = 4 , l'algorithme doit calculer 
# 1^2 + 2^2 + 3^3 + 4^4 
# et afficher le resultat

# Algorithme SommeCarres
# Variables
#     n, somme, i, carre : entiers
# Début
#     Ecrire("Entrez un nombre entier positif : ")
#     Lire(n)
#     somme ← 0
#     Pour i de 1 à n
#         carre ← i * i
#         somme ← somme + carre
#     FinPour
#     Ecrire("La somme des carrés de 1 à ", n, " est : ", somme)
# Fin

n = int(input("Entrez un nombre entier positif : ")) # Demande à l'utilisateur d'entrer un nombre entier positif et le convertit en entier avec la fonction int.

somme = 0 # Initialise la variable somme à zéro. Cette variable sera utilisée pour accumuler la somme des carrés.

for i in range(1, n + 1): # Débute une boucle for qui itère sur les nombres de 1 à n inclus.
    carre = pow(i, 2) # Calcule le carré de chaque nombre dans la boucle à l'aide de la fonction pow().
    somme = somme + carre #  Ajoute le carré du nombre actuel à la variable somme.

print("La somme des carrés de 1 à ", n, "est :", somme) # Affiche la somme totale des carrés des nombres de 1 à n à la fin de la boucle for. 
#Utilise print() avec des virgules pour concaténer les éléments à afficher.




    
    




