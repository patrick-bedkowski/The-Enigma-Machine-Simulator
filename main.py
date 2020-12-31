from enigma import Enigma, format_to_dict
from file_management import read_txt_file, save_txt_file, save_json_file
from tabulate import tabulate
from exceptions import OutOfRangeValue
import pandas as pd

# Enigma welcome label
from pyfiglet import Figlet
text = Figlet(font='big')

#! czy to moze tak byc
def format_text(text):
    return f'\n{text}'

def design_assumptions(): #! przenieść do enigmy.py
    '''
    Asumptions for the inputs. It consists of each category and its values

    '''
    assumpions_dist = [
        ['Text',
            f'{chr(62)} can be inserted as lowercases or uppercases\n'+\
            f'{chr(62)} must contain characters of the alphabet in range a-z'
        ],
        ['Steckenbrett',
            f'{chr(62)} can be left empty\n'+\
            f'{chr(62)} must be inserted in pair of letters separated by a comma, e.g. AB, CD\n'+\
            f'{chr(62)} must not hold two identical letters'
        ],
        ['Rotors',
            f'{chr(62)} must be inserted in a number of three values separated by a comma, e.g. 1,2,3\n'+\
            f'{chr(62)} each value must be a number from range 1-26'
        ],
        ['Reflector',
            f'{chr(62)} can be choosen from one of the options: A, B, C'
        ]
    ]
    return assumpions_dist


def check_if_rotors_values_are_correct(list_of_rotors): #! przenieść do enigmy.py
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
    '''
    This function is executed when user wants to enter enigma settings by hand
    '''
    steckerbrett = input(format_text('Insert Steckerbreit values that you want to switch, in format "AB, CD": '))
    if steckerbrett:  # if steckerbrett is not empty, format to dictionary
            steckerbrett = format_to_dict(steckerbrett)

    rotors = input(format_text('Insert three rotor settings separated by coma (numbers 1-26): '))
    list_of_rotors = rotors.split(',')

    reflector = input(format_text('Which reflector would you like to choose? (A, B, C): '))
    #implement checking reflector value

    if (check_if_rotors_values_are_correct(list_of_rotors)):
        return int(list_of_rotors[0]), int(list_of_rotors[1]), int(list_of_rotors[2]), steckerbrett, reflector


def main():
    '''
    MAIN PROGRAM OF THE ENIGMA SIMULATOR

    At the beginning user is asked to choose one of the options:
        >text will be imported from the .txt file
        >user wants to enter text through terminal
        >view design assumptions of the enigma machine

    '''
    print(text.renderText('Enigma Simulator'))
    options = [['1. Read text from file','2. Enter own text','3. View design assumptions of the simulator']]
    print(tabulate(options, tablefmt='fancy_grid'))

    try:
        choice = int(input(format_text('Insert a number of option that you want to use: ')))
        if choice == 1:
            input_path = input(format_text('Write file path with extension .txt to insert into Enigma: '))
            while input_path:
                if input_path:
                    ciphered_text = read_txt_file(input_path)
                    break
                else:
                    print('No file inserted') #! change it so it looks good
                    print('Insert path again, or insert b to restart program: ')

        elif choice == 2:
            ciphered_text = input(format_text('Write message that you want to insert into Enigma: ')).upper()
            if any(letter.isdigit() for letter in ciphered_text):  # if there's a number in inserted text
                raise Exception('Text must contain letters from a-z only')
        elif choice == 3:
            print(tabulate(design_assumptions(), tablefmt='fancy_grid'))


            choice = (input(format_text('When you are ready to restart the simulator type y: ')))
            while choice:
                if choice == 'y':
                    main()
                else:
                    print(format_text('Insert proper value'))
                    choice = (input(format_text('When you are ready to restart the simulator type y: ')))
        else:
            raise OutOfRangeValue('Out of range options was chosen')
    except ValueError:
        raise ValueError('No number was inserted')

    choice_import_settings = input(format_text('Would you like to import Enigma settings from the json file? y/n: '))
    if choice_import_settings == 'y':
        pass
    elif choice_import_settings == 'n':
        alpha, beta, gama, steckerbrett, reflector = enter_settings_by_hand()

        enigma = Enigma(alpha, beta, gama, steckerbrett, reflector)

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
        '''Returning message'''
        processed_text = enigma.encrypt(ciphered_text)
        print(format_text(f'Here is encrypted message: {processed_text}'))

        '''Saving message to .txt file'''
        current_choice = input(format_text('Would you like to save this to the file? y/n: '))
        while current_choice:
            if current_choice == 'y':
                save_txt_file(processed_text)
                break
            elif current_choice == 'n':
                break  # continue with the program
            else:
                print(format_text('Insert proper option'))
                current_choice = input(format_text('Would you like to save this to the file? y/n: '))
                break  # THE END

        '''Saving settings of the simulator to .json file'''
        current_choice = input(format_text('Would you like to save enigma settings to the file? y/n: '))
        while current_choice:
            if current_choice == 'y':
                save_json_file(enigma)
                break
            elif current_choice == 'n':
                break  # continue with the program
            else:
                print(format_text('Insert proper option'))
                current_choice = input(format_text('Would you like to save enigma settings to the file? y/n: '))
                break  # THE END
    else:
        raise Exception('Wrong answer')

    print('\nThank you for using my Enigma Machine Simulator')

    #steckerbrett = read_steckerbrett_file()


if __name__ == '__main__':
    main()


'''
why imports matter

It has to run the whole file I believe, even if you import one function
Because there is no way for the interpreter to know before hand whether there is other code that that function needs
like the imports at the top of the file, the function might rely on
so it runs the imports for file_management.py when you import it in main.py
but main.py is in the imports
so it tries to run that
and that tries to import file_manage.py
'''