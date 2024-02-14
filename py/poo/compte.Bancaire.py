# Exercice : Compte bancaire

# 1) Créer une classe Python nommée CompteBancaire qui représente un compte bancaire, ayant pour attributs : numeroCompte (type numérique ) , nom (nom du propriétaire du compte du type chaine), solde.
# 2) Créer un constructeur ayant comme paramètres : numeroCompte, nom, solde.
# 3) Créer une méthode Versement() qui gère les versements.
# 4) Créer une méthode Retrait() qui gère les retraits.
# 5) Créer une méthode Agios() permettant d'appliquer les agios à un pourcentage de 5 % du solde
# 6) Créer une méthode afficher() permettant d’afficher les détails sur le compte
# 7) Concevoir la classe CompteBancaire et appeler ses methodes dans main.py.

class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def versement(self, argent):
        self.solde += argent

    def retrait(self, argent):
        if(self.solde <= 0):
            print("Retrait impossible, solde insuffisant !")
        else:
            self.solde -= argent

    def agios(self):
        agios = self.solde * 0.05
        self.solde -= agios

    def afficher(self):
        print("Compte numéro : ", self.numeroCompte)
        print("Nom : ", self.nom)
        print("Solde  : ", self.solde)
        
        
        
compte1 = CompteBancaire(1, "NOM1", 2000)
compte1.afficher()

compte1.retrait(100)

compte1.afficher()

compte1.versement(1000)

compte1.afficher()

compte1.agios()

compte1.afficher()