from carte import Carte, PaquetDeCarte
from blackjack import BlackJack
from bataille import Bataille

def main():
    paquet_a=PaquetDeCarte()
    paquet_a=PaquetDeCarte()
    paquet_a.remplir()
    paquet_a.remplir()
    BlackJack(paquet_a, paquet_a)

if __name__=="__main__":
    main()

