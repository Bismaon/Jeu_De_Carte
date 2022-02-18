from carte import *
from BlackJack import *
from Bataille import *
"""
Exemple d'instance de Bataille:
- deux paquets de cartes:
    - nom_du_paquet=PaquetDeCarte()
    - nom_du_deuxieme_paquet=PaquetDeCarte()
- il faut les remplir:
    - nom_du_paquet.remplir()
    - nom_du_deuxieme_paquet.remplir()
- ensuite on met en route la bataille:
    - Bataille(nom_du_paquet, nom_du_deuxieme_paquet).bataille()
    - faite tourner le programme et c'est bon
"""    

def main():    
    paquetA=PaquetDeCarte()
    paquetB=PaquetDeCarte()
    paquetA.remplir()
    paquetB.remplir()
    btlle=Bataille(paquetA, paquetB)
    BlackJack(paquetA, paquetB, "Bismaon")
if __name__=="__main__":
    main()

