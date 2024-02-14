

class Person :
    # La méthode __init__ en Python est spéciale et est utilisée
    # comme constructeur pour initialiser les attributs
    # d'une instance de classe lors de sa création
    # Les méthodes spéciales __**** __ ont des spécifications
    # spécifiques pour l'interpréteur Pyton
    def __init__(self, name, age):  # Définition du constructeur __init__. 
                                    # Appelé automatiquement lors de la création d'1 nouvelle instance de la classe Person.
                                    # Le constructeur initialise les attributs nom et age avec les valeurs en paramètres.
        self.nom = name
        self.age = age
        
        """
        Le constructeur de la classe Person.
            
        Parameters: 
          - name (str): le nom de la personn
          - age (int): l'age de la personnee.
        """


    def __str__(self) -> str:
        return f"{self.name} {self.age} ans" # Méthode spéciale pour représenter l'objet sous forme de chaîne de caractères.
                                            #   Returns: - str: La représentation textuelle de l'objet.
        
    
    def display_info(self):
        """
        Affiche les informations de la personne.
        """   
      

    def display_info(self):
        """
        Affiche les informations de la personne
        """
        print(f"Nom: {self.name}, Age: {self.age}")
