from enigma_class import Enigma
from enigma_interface import Enigma_interface

def main():
    # Create an object of Enigma_interface class
    enigma = Enigma_interface(Enigma)
    # Initiate menu
    enigma.start_menu()

if __name__ == '__main__':
    main()
