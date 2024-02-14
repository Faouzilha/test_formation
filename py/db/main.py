
# Ce module est importé pour utiliser 
# le connecteur MySQL pour Python.
import mysql.connector
import exercice


# représente la connexion à la bLase de données MySQl
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port=3306,
  database = "mydb"
)

print(mydb)

# Créé pour exécuter des requêtes SQL sur la base de données.
cursor = mydb.cursor()

# Requête SQL pour sélectionner la colonne nomCinema de la table cinéma.
select_specific_cols = "SELECT * FROM cinema;"

# Exécutez la requête SQL à l'aide du curseur.
cursor.execute(select_specific_cols)

# Récupère tous les résultats de la requête exécutée.
results = cursor.fetchall()

# Afficher les résultats
for res in results:
    print(res)

# ferme le curseur pour libérer les ressources.
cursor.close()
# ferme la connexion à la base de données.
mydb.close()


with mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database="mydb"
) as mydb:
    with mydb.cursor() as cursor:
        # Requête SELECT
        select_specific_cols = "SELECT NumCinema, NomCinema, RueCinema FROM cinema;"
        cursor.execute(select_specific_cols)

        # Récupérer les résultats
        results = cursor.fetchall()

        # Afficher les résultats
        for res in results:
            print(res)

        # Requête INSERT
        nom_cinema = "NouveauCinema"
        rue_cinema = "NouvelleRue"
        insert_cinema = f"INSERT INTO cinema (NomCinema, RueCinema) VALUES ('{nom_cinema}', '{rue_cinema}');"
        cursor.execute(insert_cinema)

        # Valider l'opération d'insertion
        mydb.commit()

        # Requête UPDATE (modifier le nom du premier cinéma)
        num_cinema_a_modifier = 1
        nom_cinema_modifie = "PullMan"
        rue_cinema_modifie = "CountryClub"

        update_query = f"UPDATE cinema SET NomCinema = '{nom_cinema_modifie}', RueCinema = '{rue_cinema_modifie}'  WHERE NumCinema = {num_cinema_a_modifier};"
        cursor.execute(update_query)

        # Valider l'opération d'update
        mydb.commit()

        print(f"\nCinéma avec ID {num_cinema_a_modifier} mis à jour avec le nouveau nom '{nom_cinema_modifie}'.")

        # Requête SELECT par ID
        num_cinema = 3
        select_by_id_query = f"SELECT NumCinema, NomCinema, RueCinema FROM cinema WHERE NumCinema = {num_cinema};"
        cursor.execute(select_by_id_query)
        selected_cinema = cursor.fetchone()

        print(f"\nSélection du cinéma avec ID {num_cinema} : {selected_cinema}")

        # Requête DELETE (supprimer le cinéma avec ID 1)
        num_cinema_a_supprimer = 3
        delete_query = f"DELETE FROM cinema WHERE NumCinema = {num_cinema_a_supprimer};"
        cursor.execute(delete_query)

        # Valider l'opération de suppression
        mydb.commit()

        print(f"\nCinéma avec ID {num_cinema_a_supprimer} supprimé avec succès.")

        #essaie delete
        