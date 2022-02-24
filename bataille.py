from random import shuffle
from carte import Carte, PaquetDeCarte
###To do list:
#    - make it visual
#    - have interaction with the user
#    - be able to choose which game one wnats to play, black, or bataille
class Bataille:
    """La class Batialle permet de:
        -   jouer à la bataille contre "l'ordinateur"
        -   de tirer des cartes
        -   de savoir combien de carte reste dans chaque paquet
        -   finir au bout de 100 retour de carte, et de voir qui a gagné!
    """

    def __init__(self, paquet1:list, paquet2:list):
        self.jeu1=paquet1
        self.jeu2=paquet2

    def bataille(self):
        """Tapez ENTER pour tirer une carte et commencer la bataille.\n
        RAPPEL:\n
            - Les cartes sont tirer en meme temps
            - trefles < carreau < coeur < pique"""
        v_couleur={'trefle':1, 'carreau':2, 'coeur':3, 'pique':4}
        indice_j1=0
        indice_j2=0
        tour=0
        shuffle(self.jeu1.contenu)
        shuffle(self.jeu2.contenu)
        while len(self.jeu1.contenu)!=0 and len(self.jeu2.contenu)!=0:
            tour+=1
            if indice_j1>=len(self.jeu1.contenu):
                indice_j1=0
            if indice_j2>=len(self.jeu2.contenu):
                indice_j2=0
            carte1=self.jeu1.get_carte_at(indice_j1)
            carte2=self.jeu2.get_carte_at(indice_j2)
            input('{}: {} de {} contre {} de {}'.format(tour,
                                                        carte1.get_nom(),
                                                        carte1.get_couleur(),
                                                        carte2.get_nom(),
                                                        carte2.get_couleur()))
            if carte1.valeur>carte2.valeur:
                input(f"J1: {carte1.get_nom()} de {carte1.get_couleur()} l'emporte!")
                self.jeu2.contenu.append(carte1)
                self.jeu1.contenu.pop(indice_j1)
                indice_j2+=1
            elif carte1.valeur == carte2.valeur:
                if v_couleur[carte1.get_couleur()]>v_couleur[carte2.get_couleur()]:
                    input(f"J1: {carte1.get_nom()} de {carte1.get_couleur()} l'emporte!")
                    self.jeu2.contenu.append(carte1)
                    self.jeu1.contenu.pop(indice_j1)
                    indice_j2+=1
                elif v_couleur[carte1.get_couleur()]==v_couleur[carte2.get_couleur()]:
                    input("Egalité!")
                    indice_j1+=1
                    indice_j2+=1
                else:
                    input(f"J2: {carte2.get_nom()} de {carte2.get_couleur()} l'emporte!")
                    self.jeu1.contenu.append(carte2)
                    self.jeu2.contenu.pop(indice_j2)
                    indice_j1+=1
            else:
                input(f"J2: {carte2.get_nom()} de {carte2.get_couleur()} l'emporte!")
                self.jeu1.contenu.append(carte2)
                self.jeu2.contenu.pop(indice_j2)
                indice_j1+=1
            if tour>100:
                if len(self.jeu2.contenu)>len(self.jeu1.contenu):
                    print(f"""Joueur Numero 2 a gagné! avec {len(self.jeu2.contenu)} cartes restantes!\n
                              Le joueur numero 1 avait {len(self.jeu1.contenu)} cartes restantes!""")
                    return
                if len(self.jeu1.contenu)==len(self.jeu2.contenu):
                    print("Egalité!")
                    return
                else:
                    print(f"""Joueur Numero 1 a gagné! avec {len(self.jeu1.contenu)} cartes restantes!\n
                              Le joueur numero 2 avait {len(self.jeu2.contenu)} cartes restantes!""")
                    return
        if len(self.jeu2.contenu)==0:
            print("Joueur Numero 1 a gagné!", tour)
        else:
            print("Joueur Numero 2 a gagné!", tour)
paquet_a=PaquetDeCarte()
paquet_b=PaquetDeCarte()
paquet_a.remplir()
paquet_b.remplir()
bt=Bataille(paquet_a, paquet_b)
bt.bataille()