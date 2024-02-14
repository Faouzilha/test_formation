import statistics
# exo1
# Définissez une fonction maximum(n1,n2,n3) qui renvoie le plus grand des 3 nombres n1, n2, n3 fournis en arguments. 
# Par exemple, l'exécution de l'instruction : print(maximum(2,5,4)) doit donner le résultat : 5.

def maximum(n1, n2, n3):# Fonction maximum qui prend 3 paramètres (n1,n2,n3)
    return max(n1, n2, n3)# Renvoie le maximum des 3 (max)


resultat = maximum(2, 5, 4) #  Appel de la fonction maximum avec les valeurs 2, 5 et 4, et le résultat est stocké dans la variable resultat
print(resultat) # Affiche le résultat

    
# exo2
# Définissez une fonction surfCercle(R). Cette fonction doit renvoyer la surface (l'aire) d'un cercle dont on lui a fourni le rayon R en argument. 
#Par exemple, l'exécution de l'instruction :
# print(surfCercle(2.5)) doit donner le résultat 19.635
    
import math # Importe le module math, qui fournit des fonctions mathématiques 

def surfCercle(R):
    # Aire d'un cercle : Aire = Pi * R puissance 2 (en multipliant Pi par le carré du rayon)
    aire = math.pi * R**2
    return (aire, 3) # l'aire du cercle et le nombre 3, le nombre 3 est renvoyé à chaque appel de la fonction, indépendamment du rayon fourni en argument.


print(surfCercle(2.5)) # Appel de la fonction surfCercle avec un rayon de 2.5. Le résultat est un tuple contenant l'aire du cercle calculée et le nombre 3.



# exo3 : Réecrire avec une fonction
# Un gardien de phare va aux toilettes cinq fois par jour or lesWCsont au rez-de-chaussée. . .
# Écrire une procédure (donc sans retour) hauteurparcourue qui reçoit deux paramètres
# le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :
# Pour x marches de y cm, il parcourt z.zz m par semaine.
# On n’oubliera pas :
# – qu’une semaine comporte 7 jours ;
# – qu’une fois en bas, le gardien doit remonter ;

import math
math.pi # Accède à la constante π (pi) du module math

nombres_marche = 50 # initialisation des variables avec des valeurs spécifiques
hauteur_marche = 15

def distance_parcourue(nb, h) :# fonction définie par distance parcourue(nb, h) paramètre
    nombre_total_marche = nb *2 # Calcul du nombre total de marches (en montant et descendant)
    hauteur_total_marche = h /100 # Conversion de la hauteur d'une marche de centimètres en mètres
    print(f'Pour {nb} marches de {h} cm, il parcourt { hauteur_total_marche:.2f} m par semaine !')
    #Affichage d'une chaîne formatée indiquant le nombre de marches, la hauteur d'une marche,
    #et la distance totale parcourue en mètres (avec une précision de deux chiffres après la virgule).
     

nbMarches = int(input("Combien de marches ?"))# Demande à l'utilisateur d'entrer le nombre de marches 
hauteurMarche = int(input("Hauteur d'une marche (cm) ?"))# et la hauteur d'une marche, convertissant les entrées en entiers

distance_parcourue(nombres_marche, hauteur_marche) # Appel de la fonction distance_parcourue avec les valeurs initiales définies 


# Ecrivez une fonction renvoyant plusieurs valeurs sous forme d’un tuple.
# Écrire une fonction minMaxMoy qui reçoit une liste d’entiers en arguments et qui renvoie le minimum,
# le maximum et la moyenne de cette liste. 
# Le programme principal appellera cette fonction avec la liste : [10, 18, 14, 20, 12, 16].

def minMaxMoy(liste):# fonction minMaxMoy qui prend une liste en paramètre
    min = liste[0]# Initialisation des variables min, max et sum avec la première valeur de la liste.
    max = liste[0]
    sum = float(liste[0])

    for i in liste[1:]: # Début d'une boucle qui itère à travers les éléments de la liste, à partir du 2ème élément
        if i < min:# Elément i est < à la valeur actuelle de min, met à jour min avec i
            min = i 
        if i> max:
            max = i
        sum += i # Ajoute la valeur de i à la somme totale.
    moyenne = sum / len(liste) # Moyenne calculée en divisant la somme totale par la longueur de la liste
    return(min, max, moyenne) #  La fonction renvoie un tuple contenant le minimum, le maximum et la moyenne

listEntier = [10, 18, 14, 20, 12, 16 ] # Déclaration d'une liste d'entiers appelée listEntier
        
print("liste =", listEntier)
listes = minMaxMoy(listEntier) # Appel de la fonction minMaxMoy avec la liste listEntier et stocke le résultat dans la variable listes.
print(f"min : {listes[0]}, max : {listes[1]}, moy : {listes[2]}") # Affiche le min, le max et la moy calculés à partir de la liste d'entiers. Utilise une chaîne formatée pour afficher les résultats


# exo5:                                                                             
# Ecrivez une fonction qui compte le nombre de mots d’une phrase
# Ecrire une fonction compteMots(phrase) qui renvoie le nombre de mots contenus 
#dans la phrase "phrase".
# On considère comme mots les ensembles de caractères inclus entre des espaces.
# Aide :
# Utilisez la methode split() pour diviser la phrase en mots en utilisant l'espace 
#comme séparateur
# puis len() pour compter le nombre d'éléments
                                                        
def compteMots(phrase):
    mots = phrase.split() # éthode split() pour diviser la phrase en mots en utilisant l'espace comme séparateur par défaut, créant ainsi une liste de mots.
    nbMots = len(mots) # Utilisation de la fonction len pour obtenir la longueur de la liste de mots, ce qui donne le nombre total de mots dans la phrase.
    return nbMots
               
phrase1 = "j'apprends la programmation python."
total = compteMots(phrase1) # Appel de la fonction compteMots avec la phrase phrase1 et stockage du résultat dans la variable total.
print(f"La phrase '{phrase1}' contient {total} mots.")



# L'ordinateur tire un nombre entier au hasard entre 0 et 100.
# L'utilisateur doit le trouver et pour cela propose des valeurs.
# L'ordinateur indique pour chaque valeur proposée si la valeur est trop petite, 
#trop grande ou s'il a trouvé.
# 1) Écrire un programme en Python pour jouer à ce jeu.

import random # Import module random qui est utilisé pour générer des nombres aléatoires

def jeuDeviner():
    nombre_secret = random.randint(0, 100) # Génère un nombre aléatoire entre 0 et 100 et le stocke dans la variable nombre_secret.
    print(nombre_secret) 

    while True: # Débute une boucle infinie pour permettre à l'utilisateur de faire plusieurs tentatives jusqu'à ce qu'il devine correctement le nombre secret.
        proposition = int(input("Proposez un nombre entre 0 et 100 : ")) # Demande à l'utilisateur de saisir un nombre en le convertissant en entier.
        if proposition < nombre_secret:
            print("Trop petit ! Essayez à nouveau.")# Vérifie si la proposition de l'utilisateur est trop petite, affiche un message et continue la boucle.
            continue
        if proposition > nombre_secret:
            print("Trop grand ! Essayez à nouveau.")
            continue
        if proposition == nombre_secret:# Vérifie si la proposition de l'utilisateur est correcte. Si ok, affiche "bravoo" et utilise break pour sortir de la boucle
          print("bravoo")
          break          
        
jeuDeviner() # Appel de la fonction jeuDeviner pour commencer le jeu.




