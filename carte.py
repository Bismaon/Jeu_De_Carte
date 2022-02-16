from BlackJack import *
class Carte:
    def __init__(self, couleur, valeur):
        self.Couleur = couleur
        self.Valeur = valeur

    def getNom(self):
        """Retourne le nom de la carte

        Returns:
            - String: nom de la carte
        """
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"
        
    def getCouleur(self):
        """Retourne la couleur de la carte

        Returns:
            - String: couleur de la carte
        """
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    def remplir(self):
        """Permet de remplir le paquet de carte, de manière croissante.
        """
        for v in range(1,14):
            for c in range(1,5):
                self.contenu.append(Carte(c, v))
                
    def getCarteAt(self, pos):
        """
        Args:
            pos (int): position de la carte dans le paquet

        Returns:
            class Carte(): retourne l'objet carte du paquet a la position pos
        """
        return self.contenu[pos]
            