from enigma import Enigma
from file_management import read_txt_file, save_txt_file, save_json_file, read_json_file
from tabulate import tabulate
from exceptions import OutOfRangeValue, SteckerbrettRepeatedValues

# Enigma welcome label
from pyfiglet import Figlet
text = Figlet(font='big')

# function that
def format_text(text):
    return f'\n{text}'

def design_assumptions(): #! przenieść do enigmy.py
    '''
    Asumptions for the inputs. It descibes how to insert values properly

    '''
    assumpions_dist = [
        ['Text',
            f'{chr(62)} can be inserted as lowercases or uppercases\n'+\
            f'{chr(62)} must only contain characters of the alphabet in range a-z'
        ],
        ['Steckenbrett',
            f'{chr(62)} can be left empty\n'+\
            f'{chr(62)} must be inserted in pair of letters separated by a commas, e.g. AB, CD\n'+\
            f'{chr(62)} must not hold two identical letters'
        ],
        ['Rotors',
            f'{chr(62)} must be inserted in a number of three values separated by a comma, e.g. 1,2,3\n'+\
            f'{chr(62)} each value must be a number from range 1-26'
        ],
        ['Reflector',
            f'{chr(62)} can be choosen from one of the options: A, B, C'
        ],
        ['Save/Import Files',
            f'{chr(62)} name can only consists of characters of the alphabet in range a-z and numbers'
        ],
        ['Imported .txt file',
            f'{chr(62)} must consists of characters of the alphabet in range a-z'+\
            f'{chr(62)} uppercase and lowercase values of letters are acceptable'+\
            f'{chr(62)} text must be saved in a single line'
        ],
        ['Option Answers ',
            f'{chr(62)} answer must be chosen between ones specified in program and inserted in given way\n'\
            +'  e.g. "Insert y/n", you can insert "y" as an affirmative answer, or "n" to reject it'
        ]
    ]
    return assumpions_dist


def format_to_dict(steckenbrett_str):
    '''
    Function is collecting inserted string values of conjugated letters
    that are separated by a coma. It converts them to a dictionary with
    key and value as conjugated letters. Function returns a dictionary.
    '''
    '''
    Values must be inserted like so AB,CD
    This function will convert str value to dictionary like: {'a': 'b', 'c': 'd'}
    '''
    new_dict = {}
    # split pairs of letters separated by a coma and create a list
    list_of_letter_pairs = steckenbrett_str.split(",")
    # iterate through a list containing letters
    for letters in list_of_letter_pairs:
        # pairs of conjugated letters are updated into new dictionary
        new_dict.update({letters[0]: letters[1]})
    return new_dict

def steckerbrett_check_for_values(steckerbrett_dict):
    '''
    Steckerbrett cannot hold two same values.
    We need to check if it is true.
    '''
    # create a list where detected values, keys are stored
    detected_values_keys = []

    # iterate through keys, values
    for key, value in steckerbrett_dict.items():
        # if key, value is the same as in the detection list, raise an error
        if key in detected_values_keys and value in detected_values_keys:
            raise SteckerbrettRepeatedValues('Steckerbrett must have different values')
        else:
            # if key, value repetition has not been detected, append them into detection list
            detected_values_keys.append(key, value)
    # return information that repetition of the values has not been detected
    return True


def check_if_rotors_values_are_correct(list_of_rotors):
    '''
    This function inspects how many settings were inserted,
    and if values mets asumptions
    '''
    # check how many of the rotor settings were inserted
    if len(list_of_rotors) != 3:
        raise ValueError('Incorrect number of settings was inserted')

    # iterate through every rotor setting
    for rotor in list_of_rotors:
        # if setting is not a number and in range 1-26 raise exception
        if int(rotor) in range(1,27):
            continue
        else:
            raise ValueError('Invalid rotor values')  # break and raise error
    # If all the values are correct, continue with the program
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
            raise OutOfRangeValue('Out of range value was chosen')
    except ValueError:
        raise ValueError('No number was inserted')

    # User have a choice to import Enigma Simulator Settings from .json file.
    # If user chooses to import settings, he probably doesn't need to save them later in the program.
    # The choice will be remembered and used to initiate "save_json_file" block
    choice_import_settings = input(format_text('Would you like to import Enigma settings from the json file? y/n: ')).lower()
    if choice_import_settings == 'y':
        '''Reading settings from to .json file'''
        input_path = input(format_text('Write file path with extension .json to insert settings into Enigma: '))
        while input_path:
            if input_path:
                alpha, beta, gama, steckerbrett, reflector = read_json_file(input_path)
                break
            else:
                print('No file inserted') #! change it so it looks good
                print('Insert path again, or insert b to restart program: ')
    elif choice_import_settings == 'n':
        alpha, beta, gama, steckerbrett, reflector = enter_settings_by_hand()

    enigma = Enigma(alpha, beta, gama, steckerbrett, reflector)

    """Conditions"""
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