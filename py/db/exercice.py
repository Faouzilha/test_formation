# Creer un module python a partir de script dans lequel on retrouvera 
# 5 methodes :
# select_specific_cols()
# insert_cinema()
# update_cinema()
# select_by_id()
# delete_cinema()


import mysql.connector

# Fonction pour se connecter à la base de données
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3308,
        database="cinemas"
    )

# Fonction pour effectuer une requête SELECT spécifique
def select_specific_cols():
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = "SELECT NumCinema, NomCinema, RueCinema FROM cinema;"
            cursor.execute(query)
            return cursor.fetchall()

# Fonction pour effectuer une opération d'insertion
def insert_cinema(nom_cinema, rue_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"INSERT INTO cinema (NomCinema, RueCinema) VALUES ('{nom_cinema}', '{rue_cinema}');"
            cursor.execute(query)
            mydb.commit()

# Fonction pour effectuer une opération de mise à jour
def update_cinema(num_cinema, nom_cinema, rue_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"UPDATE cinema SET NomCinema = '{nom_cinema}', RueCinema = '{rue_cinema}' WHERE NumCinema = {num_cinema};"
            cursor.execute(query)
            mydb.commit()

# Fonction pour effectuer une requête SELECT par ID
def select_by_id(num_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"SELECT NumCinema, NomCinema, RueCinema FROM cinema WHERE NumCinema = {num_cinema};"
            cursor.execute(query)
            return cursor.fetchone()

# Fonction pour effectuer une opération de suppression
def delete_cinema(num_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"DELETE FROM cinema WHERE NumCinema = {num_cinema};"
            cursor.execute(query)
            mydb.commit()



import mysql.connector

# Fonction pour se connecter à la base de données
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3308,
        database="cinemas"
    )

# Fonction pour effectuer une requête SELECT spécifique
def select_specific_cols():
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = "SELECT NumCinema, NomCinema, RueCinema FROM cinema;"
            cursor.execute(query)
            return cursor.fetchall()

# Fonction pour effectuer une opération d'insertion
def insert_cinema(nom_cinema, rue_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"INSERT INTO cinema (NomCinema, RueCinema) VALUES ('{nom_cinema}', '{rue_cinema}');"
            cursor.execute(query)
            mydb.commit()

# Fonction pour effectuer une opération de mise à jour
def update_cinema(num_cinema, nom_cinema, rue_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"UPDATE cinema SET NomCinema = '{nom_cinema}', RueCinema = '{rue_cinema}' WHERE NumCinema = {num_cinema};"
            cursor.execute(query)
            mydb.commit()

# Fonction pour effectuer une requête SELECT par ID
def select_by_id(num_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"SELECT NumCinema, NomCinema, RueCinema FROM cinema WHERE NumCinema = {num_cinema};"
            cursor.execute(query)
            return cursor.fetchone()

# Fonction pour effectuer une opération de suppression
def delete_cinema(num_cinema):
    with connect_to_database() as mydb:
        with mydb.cursor() as cursor:
            query = f"DELETE FROM cinema WHERE NumCinema = {num_cinema};"
            cursor.execute(query)
            mydb.commit()

