from enigma import Enigma
from file_management import read_txt_file, save_txt_file, save_json_file, read_json_file
from tabulate import tabulate
from exceptions import (
    UndefinedOption,
    SteckerbrettRepeatedValues,
    SteckerbrettWrongFormat,
    SteckerbrettNotInText,
    ReflectorValueIsUndefined,
    NoAsciiInFile,
    WrongNumberOfLines,
    IncorrectRotorSettings,
    InvalidRotorValues,
    WrongFileName,
    UndefinedFileName,
    FileNotFound
)

# Enigma welcome label
from pyfiglet import Figlet
text = Figlet(font='big')

def design_assumptions(): #! przenieść do enigmy.py
    '''
    Asumptions for the inputs. It descibes how to insert values properly

    '''
    assumpions_dist = [
        ['Text',
            f'{chr(62)} must be inserted as uppercases characters\n'+\
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
            f'{chr(62)} must be inserted as one letter choosen from A, B, C'
        ],
        ['Save/Import Files',
            f'{chr(62)} name can only consists of characters of the alphabet in range a-z and integer numbers'
        ],
        ['Imported .txt file',
            f'{chr(62)} must consists of characters of the alphabet in range a-z\n'+\
            f'{chr(62)} uppercase and lowercase values of letters are acceptable\n'+\
            f'{chr(62)} text must be saved in a single line'
        ],
        ['Option Answers ',
            f'{chr(62)} answer must be chosen between ones specified in program and inserted in given way\n'\
            +'  e.g. "Insert y/n", you can insert "y" as an affirmative answer, or "n" to reject it'
        ]
    ]
    return assumpions_dist

def check_if_rotor_values_are_correct(list_of_rotors):
    '''
    This function inspects how many settings were inserted,
    and if values mets asumptions
    '''
    # check how many of the rotor settings were inserted
    if len(list_of_rotors) != 3:
        raise IncorrectRotorSettings('Incorrect number of settings was inserted')

    # iterate through every rotor setting
    for rotor in list_of_rotors:
        # if setting is not a number and in range 1-26 raise exception
        if int(rotor) not in range(1, 27):
            raise InvalidRotorValues('Invalid rotor values')  # raise an error
    # If all the values are correct, continue with the program
    return True


def format_to_dict(steckenbrett_str):
    '''
    Function is collecting inserted string values of conjugated letters
    that are separated by a coma. It converts them to a dictionary with
    key and value as conjugated letters. Function returns a dictionary.
    This function also checks if letters inserted into steckerbrett
    have no empty spaces.
    '''
    '''
    Values must be inserted like so AB,CD
    This function will convert str value to dictionary like: {'a': 'b', 'c': 'd'}
    '''
    # create a new dictionary
    new_dict = {}
    # split pairs of letters separated by a coma and create a list
    list_of_letter_pairs = steckenbrett_str.split(",")

    # iterate through a list containing letters
    for letter_pair in list_of_letter_pairs:
        # checks if there is blank space in a pair of letters
        # I did not implement another function to check that condition,
        # because it is connected with the code in this function
        if " " in letter_pair:
            # raise an exception about wrong Steckerbrett formating
            raise SteckerbrettWrongFormat('Steckerbrett has wrong format')

        # pairs of conjugated letters are updated into new dictionary
        new_dict.update({letter_pair[0]: letter_pair[1]})
    return new_dict


def steckerbrett_check_for_same_values(steckerbrett_dict):
    '''
    Steckerbrett cannot hold two same values. This function checks if
    a character is repeated, either as a key or a value. Return True if
    there is no duplicates
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
            detected_values_keys.extend([key, value])
    # return information that repetition of the values has not been detected
    return True

# This is redundant
def steckerbrett_check_if_value_in_text(steckerbrett_dict, text):
    '''
    This function checks if characters inserted into steckerbrett pairs'
    as first letter is in the Inserted text. Boolean value True is returned
    if all keys are also in Text.
    '''
    '''e.g. Inserted text: "SCHOOL" and Steckerbrett "AS,SL" is wrong,
    because letter A is not in the inserted text.
    Steckerbrett's keys are suppose to represent a letter in inserted text,
    that will be replaced with different one.
    '''

    # iterate through keys of steckerbrett dictionary
    for key in steckerbrett_dict.keys():
        if key not in text:
            raise SteckerbrettNotInText('\n\
                Steckerbrett contains characters not seen in inserted text\
                \n')

    # return information that repetition of the values has not been detected
    return True

def reflector_check_model(reflector):
    '''Returns Boolean Value True if inserted reflector value
    matches reflectors specified in the project'''
    list_of_supported_reflectors = ['A', 'B', 'C']
    if reflector not in list_of_supported_reflectors:
        raise ReflectorValueIsUndefined('Inserted Reflector Value is Undefined')
    else:
        return True

def enter_settings_by_hand(ciphered_text):
    '''
    This function is executed when user wants to enter enigma settings by hand
    '''
    steckerbrett = input(f'\nInsert Steckerbreit values that you want to switch in format "AB,CD": ')
    if steckerbrett:  # if steckerbrett is not empty, check assumptions
        # string characters are converted into dictionary
        # and its checked if inserted steckerbrety has empty spaces
        steckerbrett = format_to_dict(steckerbrett)
        # All inputs are checked for design assumptions
        '''if (
            steckerbrett_check_if_value_in_text(steckerbrett, ciphered_text)
            and steckerbrett_check_for_same_values(steckerbrett)
        ):'''
        if steckerbrett_check_for_same_values(steckerbrett):
            pass

    rotors = input(f'\nInsert three rotor settings separated by coma (numbers 1-26): ')
    list_of_rotors = rotors.split(',')

    reflector = input(f'\nWhich reflector would you like to choose? (A, B, C): ')
    # implement checking reflector value

    # All inputs are checked for design assumptions
    if (
        check_if_rotor_values_are_correct(list_of_rotors)
        and reflector_check_model(reflector)
    ):
        return int(list_of_rotors[0]), int(list_of_rotors[1]), int(list_of_rotors[2]), steckerbrett, reflector
    # if assumptions are not met, proper exception will be raised inside "check_if_rotors_values_are_correct" function


def main():
    '''
    MAIN PROGRAM OF THE ENIGMA SIMULATOR

    At the beginning user is asked to choose one of the options:
        > text will be imported from the .txt file
        > user wants to enter text through terminal
        > view design assumptions of the enigma machine

    '''
    try:
        print(text.renderText('Enigma Simulator'))
        options = [['1. Read text from file', '2. Enter own text', '3. View design assumptions of the simulator']]
        print(tabulate(options, tablefmt='fancy_grid'))
        choice = int(input(f'\nInsert a number of option that you want to use: '))
        # if choice is empty or is not a number, exception ValueError will be raised,
        # indicating that no number was inserted
        if choice == 1:
            input_file = input(f'\nWrite file path with extension .txt to insert into Enigma: ')
            # if is not empty
            if input_file:
                ciphered_text = read_txt_file(input_file)
            # if input_file is empty, raise error
            else:
                raise FileNotFound('File was not found')

        elif choice == 2:
            # user inserts own text
            ciphered_text = input(f'\nWrite message that you want to insert into Enigma: ')

            # if inserted text contain no ascii characters, raise error
            if any(letter.isdigit() for letter in ciphered_text):
                raise NoAsciiInFile('No ascii characters were inserted')
        elif choice == 3:
            # print design assumptions
            print(tabulate(design_assumptions(), tablefmt='fancy_grid'))

            # user can restart program after reading desing assumptions
            choice = input(f'\nWhen you are ready to restart the simulator type y: ')
            if choice == 'y':
                # restart main program
                main()
            else:
                raise UndefinedOption('Inserted option is undefined')
        else:
            raise UndefinedOption('Inserted option is undefined')

        # User have a choice to import Enigma Simulator Settings from .json file.
        # If user chooses to import settings, he probably doesn't need to save them later in the program.
        # The choice will be remembered and used to initiate "save_json_file" block
        choice_import_settings = input(f'\nWould you like to import Enigma settings from the json file? y/n: ')
        if choice_import_settings == 'y':
            '''Reading settings from to .json file'''
            input_path = input(f'\nWrite file path with extension .json to insert settings into Enigma: ')
            if input_path:
                alpha, beta, gama, steckerbrett, reflector = read_json_file(input_path)
            else:  # if input_file is empty, raise error
                raise FileNotFound('File was not found')
        # if user don't want to import file with settings,
        # settings must be inserted manualy
        elif choice_import_settings == 'n':
            # reads data entered by hand
            alpha, beta, gama, steckerbrett, reflector = enter_settings_by_hand(ciphered_text)
        else:
            raise UndefinedOption('Inserted option is undefined')

        # create object of Enigma class
        enigma = Enigma(alpha, beta, gama, steckerbrett, reflector)

        """Interspaces can be removed"""
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
        print(f'\nHere is encrypted message: {processed_text}')

        '''Saving PART'''

        '''Saving message to .txt file'''
        choice = input(f'\nWould you like to save this to the file? y/n: ')
        if choice == 'y':
            save_txt_file(processed_text)
        elif choice == 'n':
            pass # continue with the program
        else:
            raise UndefinedOption('Inserted option is undefined')

        '''Saving settings of the simulator to .json file'''
        choice = input(f'\nWould you like to save enigma settings to the file? y/n: ')
        if choice == 'y':
            save_json_file(enigma)
        elif choice == 'n':
            pass  # continue with the program
        else:
            raise UndefinedOption('Inserted option is undefined')

        # print last message
        print('\nThank you for using my Enigma Machine Simulator')
    except FileNotFound as Message:
        print(Message)
    except NoAsciiInFile as Message:
        print(Message)
    except WrongNumberOfLines as Message:
        print(Message)
    except WrongFileName as Message:
        print(Message)
    except SteckerbrettNotInText as Message:
        print(Message)
    except SteckerbrettRepeatedValues as Message:
        print(Message)
    except SteckerbrettWrongFormat as Message:
        print(Message)
    except ReflectorValueIsUndefined as Message:
        print(Message)
    except UndefinedFileName as Message:
        print(Message)
    except UndefinedOption as Message:
        print(Message)
    except IncorrectRotorSettings as Message:
        print(Message)
    except InvalidRotorValues as Message:
        print(Message)
    except ValueError:
        # when a character, that cannot be converted into int, is inserted raise error
        print(UndefinedOption('Inserted option is undefined'))



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
