# Module exercices

# exo1 :
# définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
# – triez et affichez la liste ; (sort())
# – ajoutez l’élément 12 à la liste et affichez la liste ;
# – renversez et affichez la liste ;
# – affichez l’indice de l’élément 17 ;
# – enlevez l’élément 38 et affichez la liste ;

liste =[17, 38, 10, 25, 72]
liste.sort()
print(liste)

liste.append(12)

print(liste)

liste.reverse()
print(liste)

print(liste[0])

del liste[1]
print(liste)

print("----------------------------------------------------------")

# exo2 :
# – affichez le dernier élément en utilisant un indiçage négatif.
# Bien remarquer que certaines méthodes de liste ne retournent rien.
# 2. Initialisez truc comme une liste vide, et machin comme une liste de cinq flottants nuls.
# Affichez ces listes.
# Utilisez la fonction range() pour afficher :
# – les entiers de 0 à 3 ;
# – les entiers de 4 à 7 ;
# – les entiers de 2 à 8 par pas de 2.
# Définir chose comme une liste des entiers de 0 à 5 et testez l’appartenance des éléments 3 et 6 à chose.

print(liste[-1])

truc = []
machin = [1.1, 2.2, 3.3, 4.4, 5.5]

print(truc)
print(machin)

print(list(range(3)))
print(list(range(4, 7)))
print(list(range(2, 8, 2)))

chose = list(range(5))
print(3 in chose)
print(6 in chose)

print("----------------------------------------------------------")

# exo3 :
# Écrire un programme en Python pour calculer:
# a) 1+2+3+....+100
# b) 1+3+5+....+99

res_sum1 = sum(range(1, 101))
print(res_sum1)

# res_sum1 = 0
# for i in range(1, 101):
#     res_sum1 += i

res_sum2 = sum(range(1, 100, 2))
print(res_sum2)

# res_sum2 = 0
# for i in range(1, 100, 2):
#     res_sum2 += i

print("----------------------------------------------------------")

# exo4 :
# Un gardien de phare va aux toilettes cinq fois par jour or les WC sont au rez-de-chaussée. . .
# Écrire un programme qui compte le nombre de marches du phare et la hauteur de chaque marche (en cm), et qui affiche :
# Pour x marches de y cm, il parcourt z.zz m par semaine.
# On n’oubliera pas :
# – qu’une semaine comporte 7 jours ;
# – qu’une fois en bas, le gardien doit remonter ;
# – que le résultat est à exprimer en m.  

nombres_marche = 50
hauteur_marche = 15

nombre_total_marche = nombres_marche * 2
hauteur_total_marche = nombre_total_marche * hauteur_marche / 100

distance_parcourue = hauteur_total_marche * 7 * 5

print(f'Pour {nombres_marche} marches de {hauteur_marche} cm,  il parcourt {distance_parcourue:.2f} m par semaine.')

print("----------------------------------------------------------")

# exo5 :
# Je suis ligoté sur les rails en gare d’Arras. Écrire un programme qui affiche un tableau
# me permettant de connaître l’heure à laquelle je serai déchiqueté par le train parti de
# la gare du Nord à 9h (il y a 170 km entre la gare du Nord et Arras).
# Le tableau prédira les différentes heures possibles pour toutes les vitesses de 100 km/h
# à 300 km/h, par pas de 10 km/h, les résultats étant arrondis à la minute inférieure.

#pip install prettytable
from prettytable import PrettyTable

distance = 170
depart_gare_du_nord = 9

table = PrettyTable(["Vitesse (km/h)", "Heure d'arrivée"])

for vitesse in range(100, 310, 10):
    # calcule le temps nécessaire pour le voyage entre la gare du Nord et 
    # Arras en fonction de la vitesse du train
    temps_voyage = distance / vitesse
    # extrait les minutes d'arrivée en prenant la partie décimale de 
    # temps_voyage (correspondant aux minutes)  et en la multipliant par 60
    min_arrivee = int((temps_voyage % 1) * 60)
    # extrait les secondes d'arrivée. Elle prend la partie décimale 
    # de la partie décimale de temps_voyage, la multiplie par 60 (pour convertir 
    # en secondes)
    sec_arrivee = int(((temps_voyage % 1) * 60 % 1) * 60)
    # calcule l'heure d'arrivée en ajoutant le temps de voyage à 
    # l'heure de départ de la gare du Nord.
    heure_arrivee = depart_gare_du_nord + int(temps_voyage)
    
    table.add_row([vitesse, f'{heure_arrivee:02}H{min_arrivee:02}M{sec_arrivee:02}'])

# Afficher la table
print(table)

print("----------------------------------------------------------")

# exo6 :
# Un permis de chasse à points remplace désormais le permis de chasse traditionnel.
# Chaque chasseur possède au départ un capital de 100 points. S’il tue une poule il perd
# 1 point, 3 points pour 1 chien, 5 points pour une vache et 10 points pour un ami. Le
# permis coûte 200 euros.
# Écrire une programme qui selon le nombre de victimes du chasseur retourne la somme due.

nombres_poules = int(input("Poules tuees ?"))
nombres_chiens = int(input("Chiens tuees ?"))
nombres_vaches = int(input("Vaches tuees ?"))
nombres_amis = int(input("Amis tuees ?"))

pts_perdus = nombres_poules + 3 * nombres_chiens + 5 * nombres_vaches + 10 * nombres_amis
pts_restants = max(0, 100 - pts_perdus)  # Mise à jour des points restants
somme_due = max(0, pts_perdus) * 2 - 200

if somme_due < 0:
    print(f"Il lui reste {pts_restants} points.")
else:
    print(f"Le chasseur doit débourser {somme_due} euros en amende.")
    print(f"Il lui reste {pts_restants} points.")

print("----------------------------------------------------------")


# exo7 :
# Écrire un programme qui calcule la somme de trois valeurs, et qui renvoie leur somme.
# Dans le programme principal, définir un tuple de trois nombres, puis utilisez la syn-
# taxe d’appel à la fonction qui décompresse le tuple. Affichez le résultat.

tuple_ex = (1, 2, 3)
a, b, c = tuple_ex
res_somme = a + b + c
print("Somme des valeurs du tuple", res_somme)
