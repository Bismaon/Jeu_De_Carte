from carte import Carte, PaquetDeCarte
from blackjack import BlackJack
from bataille import Bataille

def main():
    paquet_a=PaquetDeCarte()
    paquet_b=PaquetDeCarte()
    paquet_a.remplir()
    paquet_b.remplir()
    BlackJack(paquet_a, paquet_b)

if __name__=="__main__":
    main()