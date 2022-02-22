from carte import *
from BlackJack import *
from Bataille import *

def main():    
    paquetA=PaquetDeCarte()
    paquetB=PaquetDeCarte()
    paquetA.remplir()
    paquetB.remplir()
    BlackJack(paquetA, paquetB)
    
if __name__=="__main__":
    main()

