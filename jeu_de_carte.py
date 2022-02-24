from carte import Carte, PaquetDeCarte
from BlackJack import BlackJack
from Bataille import Bataille

def main():    
    paquet_a=PaquetDeCarte()
    paquet_a=PaquetDeCarte()
    paquet_a.remplir()
    paquet_a.remplir()
    BlackJack(paquet_a, paquet_a)
    
if __name__=="__main__":
    main()

