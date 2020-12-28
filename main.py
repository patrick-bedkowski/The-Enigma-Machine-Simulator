from enigma import Enigma
from file_management import read_txt_file, format_to_dict
from tabulate import tabulate

# Enigma welcome label
from pyfiglet import Figlet
text = Figlet(font='big')


def design_assumptions():
    '''Asumptions for the inputs'''
    return [
        [f'{chr(62)} Text must contain characters of the alphabet in range a-z'],
        [f'{chr(62)} Text can be inserted as lowercases or uppercases'],
        [f'{chr(62)} Steckenbrett values must be inserted in pair of letters separated by a comma, e.g. AB, CD'],
        [f'{chr(62)} Steckenbrett values can not hold two the same letters'],
        [f'{chr(62)} Rotors setting must be a number from range 1-26'],
        [f'{chr(62)} Reflector can be choosen from one of the options: A, B, C']
    ]


def check_if_rotors_values_are_correct(list_of_rotors):
    # check how many settings were inserted
    if len(list_of_rotors) != 3:
        raise ValueError('Incorrect number of settings was inserted')

    for rotor in list_of_rotors:
        if int(rotor) <= 26 and int(rotor) >= 1:
            continue
        else:
            raise ValueError('Invalid rotor values')  # break and raise error
    return True


def enter_settings_by_hand():
    steckerbrett = input('Insert Steckerbreit values that you want to switch, in format "AB, CD": ')
    if steckerbrett:  # if steckerbrett is not empty, format to dictionary
            steckerbrett = format_to_dict(steckerbrett)

    rotors = input('Insert three rotor settings separated by coma (numbers 1-26): ')
    list_of_rotors = rotors.split(',')

    if (check_if_rotors_values_are_correct(list_of_rotors)):
        return steckerbrett, int(list_of_rotors[0]), int(list_of_rotors[1]), int(list_of_rotors[2])


def main():
    """Variables"""
    print(text.renderText('Enigma Simulator'))
    print('| To start choose one of the options\n\
| 1. Read from file 2. Import own text 3. View design assumptions of the machine\n'
    )

    try:
        choice = int(input('Insert a number of option that you want to use: '))
        if choice == 1:
            input_path = input('Write file path with extension to insert into Enigma: ')
            ciphered_text = read_txt_file(input_path)
        elif choice == 2:
            ciphered_text = input('Write message that you want to insert into Enigma: ').upper()
            if any(letter.isdigit() for letter in ciphered_text):  # if there's a number in inserted text
                raise Exception('Text must contain letters from a-z only')
        elif choice == 3:
            print(tabulate(design_assumptions(), tablefmt="github"))

            choice = (input('\nWhen you are ready to restart the simulator type y: '))
            while choice:
                if choice == 'y':
                    main()
                else:
                    print('Insert proper value')
                    choice = (input('\nWhen you are ready to restart the simulator type y: '))
        else:
            raise Exception('Out of range options was chosen')
    except ValueError:
        raise ValueError('No number was inserted')

    choice_import_settings = input('Would you like to import Enigma settings from the json file? y/n: ')
    if choice_import_settings == 'y':
        pass
    elif choice_import_settings == 'n':
        steckerbrett, alpha, beta, gama = enter_settings_by_hand()
        enigma = Enigma(alpha, beta, gama, steckerbrett)

        """Conditions"""
        if enigma.steckerbrett(): # steckerbrett not empty
            if enigma.steckerbrett_is_dict() and enigma.steckerbrett_check_for_values() and enigma.steckerbrett_check_for_keys():
                #enigma.Remove_steckerbrett_connections_from_alphabet()
                """if ' ' in ciphered_text:
                    ciphered_text = enigma.remove_interspace(ciphered_text)
                    print(enigma._index_of_interspace == [])
                    print(enigma._index_of_interspace)"""
                #print(enigma._rotors)
                #shift = enigma.permutation(alpha)
                #print(shift)
                #print(enigma.permutation(shift))
                #inverted = enigma.inverse_permutation(alpha)
                #print(inverted)
        print(f'Here is encrypted message: {enigma.encrypt(ciphered_text)}')
    else:
        raise Exception('Wrong answer')

    #steckerbrett = read_steckerbrett_file()


if __name__ == '__main__':
    main()
