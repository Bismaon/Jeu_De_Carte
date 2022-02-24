class Carte:
    """La class carte est une classe permettant:
        - d'instancier une carte
        - de renvoyer son nom/couleur de carte
        - de renvoyer sa valeur de carte"""

    def __init__(self, couleur, valeur):
        """Counstructeur de la classe Carte qui permet de\n
        donner une couleur et une valeur a une carte
        Args:
            couleur (str): 1 ou 2 ou 3 ou 4
            valeur (int): de 1 a 13"""
        self.couleur = couleur
        self.valeur = valeur

    def get_nom(self):
        """Renvoie le nom de la carte
        Returns:
            - String: nom de la carte"""
        if ( self.valeur > 1 and self.valeur < 11):
            return str( self.valeur)
        elif self.valeur == 11:
            return "Valet"
        elif self.valeur == 12:
            return "Dame"
        elif self.valeur == 13:
            return "Roi"
        else:
            return "As"

    def get_couleur(self):
        """Renvoie la couleur de la carte
        Returns:
            - String: couleur de la carte"""
        return ['pique', 'coeur', 'carreau', 'trefle'][self.couleur - 1]

class PaquetDeCarte:
    """La class PaquetDeCarte est une classe qui permet:
        - d'initialiser un paquet de carte
        - de remplir un paquet de carte 
        - de trouver une carte a une positon I dans le paquet de carte"""

    def __init__(self):
        """Constructeur de la classe PaquetDeCarte, qui initialise un paquet vide."""
        self.contenu = []

    def remplir(self):
        """Permet de remplir le paquet de carte, de manière croissante."""
        for couleur in range(1,5):
            for valeur in range(1,14):
                self.contenu.append(Carte(couleur, valeur))

    def get_carte_at(self, pos):
        """Args:
                pos (int): position de la carte dans le paquet
        Returns:
            class Carte(): retourne l'objet carte du paquet à la position pos"""
        return self.contenu[pos]