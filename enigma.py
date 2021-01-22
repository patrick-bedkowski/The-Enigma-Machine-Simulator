from enigma_class import Enigma
from enigma_interface import Enigma_interface


def main():
    # Create an object of Enigma_interface class
    enigma_if = Enigma_interface(Enigma)
    # Initiate menu
    enigma_if.main_menu()


if __name__ == '__main__':
    main()
