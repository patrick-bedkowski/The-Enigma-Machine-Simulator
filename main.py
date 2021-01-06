from enigma_class import Enigma
from string import ascii_uppercase
from file_management import (
    read_txt_file,
    save_txt_file,
    read_json_file,
    save_json_file,
    check_if_ascii
)
from tabulate import tabulate
from exceptions import (
    UndefinedOption,
    SteckerbrettRepeatedValues,
    SteckerbrettWrongFormat,
    SteckerbrettNotInText,
    ReflectorValueIsUndefined,
    NoAsciiDetected,
    WrongNumberOfLines,
    IncorrectRotorSettings,
    InvalidRotorValues,
    WrongFileName,
    UndefinedFileName,
    FileNotFound,
    NoReflectorSelected,
    InvalidRotorQuantity,
    NoTextToProcess
)

# Enigma welcome label
from pyfiglet import Figlet
text = Figlet(font='big')

class enigma_interface:
    def __init__(self, Enigma):
        self._option = '\nPlease, insert correct option number'
        self._name = 'Enigma Simulator'
        self._insert_file_path = 'Please, insert file path again'
        self._return_message = '\nIf you wish to return to main menu, type "y": '
        self.choice_import_settings = None

    def design_assumptions(self): #! przenieść do enigmy.py
        '''
        Asumptions for the inputs. It descibes how to insert values properly
        '''
        assumpions_dist = [
            ['Text',
                f'{chr(62)} must be inserted as uppercases characters\n'+\
                f'{chr(62)} must only contain characters of the alphabet in range A-Z'
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
                +'  e.g. "Insert y/n", you can insert "y" as an affirmative answer, or "n" as negative'
            ]
        ]
        return assumpions_dist

    def display_assumptions():
        pass

    def start_options(self):
        '''Returns options of intiating simulator'''
        options = [
            ['1. Read text from file',
            '2. Enter own text',
            '3. View design assumptions of the simulator']
        ]
        return options

    def start_menu(self):
        # Prints formated name of simulator
        print(text.renderText(self._name))
        print(tabulate(self.start_options(), tablefmt='fancy_grid'))
        while True:
            choice = input(f'\nInsert a number of option that you want to use: ')
            if choice == '1':
                ciphered_text = self.input_txt_file()
                break
            elif choice == '2':
                ciphered_text = self.input_txt_by_hand()
                break
            elif choice == '3':
                # print design assumptions
                self.display_assumptions()
                break
            else:
                print(self._option)
        # if loop is finished, go to the setting menu
        self.setting_menu(ciphered_text)
        
    
    def input_txt_file(self):
        '''User chooses to import file'''

        while True:
            print(self._return_message)
            input_file = input(f'\nWrite file path with extension .txt to insert into Enigma: ')
            if input_file == 'y':
                self.start_menu()
                break
            try:
                ciphered_text = read_txt_file(input_file)
                return ciphered_text
            except FileNotFound as Message:
                print(f'{Message}. {self._insert_file_path}')
            except WrongNumberOfLines as Message:
                print(f'{Message}. {self._insert_file_path}')
            except NoTextToProcess as Message:
                    print(f'{Message}. Please, insert file with message')
            except NoAsciiDetected as Message:
                print(f'{Message}. {self._insert_file_path}')
    
    def input_txt_by_hand(self):
        '''Returns text inserted by a user'''
        while True:
            print(self._return_message)
            input_txt = input(f'\nWrite message that you want to insert into Enigma: ')
            if input_txt == 'y':
                self.start_menu()
                break
            try:
                if input_txt:
                    # if inserted text contains characters not from uppercase ascii alphabet,
                    # raise an error
                    if any(letter not in ascii_uppercase for letter in input_txt):
                        raise NoAsciiDetected('No ascii characters were inserted')
                    else:
                        return input_txt
                else:
                    raise NoTextToProcess('No text was inserted')
            except NoTextToProcess as Message:
                    print(f'{Message}. Please, insert message again')
            except NoAsciiDetected as Message:
                    print(f'{Message}. Please, insert message again')

    def display_assumptions(self):
        print(tabulate(self.design_assumptions(), tablefmt='fancy_grid'))
        while True:
            choice = input(self._return_message)
            if choice == 'y':
                self.start_menu()
                break
            else:
                print(self._option)
    
    def setting_menu(self, ciphered_text):
        # User have a choice to import Enigma Simulator Settings from .json file.
        # If user chooses to import settings, he probably doesn't need to save them later in the program.
        # The choice will be remembered and used to initiate "save_json_file" block
        setting_were_not_inserted = True
        while setting_were_not_inserted:
            self.choice_import_settings = input(
                f'\nWould you like to import Enigma settings from the json file? y/n: '
            )
            if self.choice_import_settings == 'y':
                #add to check this imported settings
                alpha, beta, gama, steckerbrett, reflector = self.import_settings_from_file()
                setting_were_not_inserted = False
            elif self.choice_import_settings == 'n':
                '''Insert settings by hand'''
                # reads data entered by hand
                alpha, beta, gama, steckerbrett, reflector = self.insert_settings_by_hand()
                setting_were_not_inserted = False
            else:
                print(self._option)
            self.initiate_enigma_simulator(alpha, beta, gama, steckerbrett, reflector, ciphered_text)
        
    def import_settings_from_file(self):
        '''Reading settings from to .json file'''
        while True:
            try:
                input_path = input(f'\nWrite file path with extension .json to insert settings into Enigma: ')
                if input_path:
                    alpha, beta, gama, steckerbrett, reflector = read_json_file(input_path)
                    return alpha, beta, gama, steckerbrett, reflector
                else:  # if input_file is empty, raise error
                    raise FileNotFound('File was not found')
            except FileNotFound as Message:
                print(f'{Message}. {self._insert_file_path}')
    
    def insert_settings_by_hand(self):
        '''
        Returns values of rotors in a list, steckerbrett as dictionary, reflector as str
        This function is executed when user wants to enter enigma settings by hand
        '''
        list_of_rotors = self.insert_rotors_values()
        steckerbrett = self.insert_steckerbrett_by_hand()
        reflector = self.insert_reflector_value()
        
        return list_of_rotors[0], list_of_rotors[1], list_of_rotors[2], steckerbrett, reflector

    def insert_steckerbrett_by_hand(self):
        '''Returns inserted steckerbrett values and formated into dictionary'''
        steckerbrett_has_wrong_format = True
        while steckerbrett_has_wrong_format:
            steckerbrett = input(f'\nInsert Steckerbreit values that you want to switch in format "AB,CD": ')
            if steckerbrett:
                # string characters are converted into dictionary
                # and its checked if inserted steckerbrety has empty spaces
                try:
                    steckerbrett = format_to_dict(steckerbrett)
                    steckerbrett_has_wrong_format = False
                except SteckerbrettWrongFormat as Message:
                    print(Message)
                    print('Insert values once again')
        return steckerbrett

    def insert_rotors_values(self):
        '''Returns list of rotor values'''
        while True:
            rotors = input(f'\nInsert three rotor settings separated by coma (numbers 1-26): ')
            try:
                list_of_rotors = self.create_list_of_rotors(rotors)
                return list_of_rotors
            except InvalidRotorQuantity as Message:
                print(Message)
                print('Insert values once again')

    def create_list_of_rotors(self, rotors):
        if rotors:
            # remove spaces from inserted text
            rotors = rotors.replace(" ", "")
            #create list of splited elements separated by a coma 
            list_of_rotors = rotors.split(',')
            # if number of inserted settings is 3, return list of rotors
            if len(list_of_rotors) == 3:
                return list_of_rotors
            else:
                raise InvalidRotorQuantity('Invalid rotor quantity') #! sprawdź czy napis taki sam
        else:
            raise InvalidRotorQuantity('Invalid rotor quantity')

    def insert_reflector_value(self):
        '''Returns value of reflector'''
        while True:
            reflector = input(f'\nWhich reflector would you like to choose? (A, B, C): ')
            try:
                self.check_if_reflector_has_value(reflector)
                return reflector
            except InvalidRotorValues as Message:
                print(Message)
                print('Insert values once again')
    

    def check_if_reflector_has_value(self, reflector):
        if not reflector:
            raise NoReflectorSelected('No reflector has been selected')
    
    '''Initiating program'''
    def initiate_enigma_simulator(self, alpha, beta, gama, steckenbrett, reflector, ciphered_text):
        '''Enigma Machine Simulator'''
        '''Here's main algorythm'''
        # create object of Enigma class
        try:
            enigma = Enigma(alpha, beta, gama, steckenbrett, reflector)
            processed_text = enigma.encryptingCodec(ciphered_text)
            print(f'\nHere is your encrypted message: {processed_text}')

            # Exporting files requires
            # processed text and initial settings 
            self.export_txt_menu(processed_text)
            # If user chosed not to import settings from file
            # Exporting settings inserted by hand is available 
            if self.choice_import_settings == 'n':
                self.export_json_menu(enigma.initial_settings)
            # print last message
            print('\nThank you for using my Enigma Machine Simulator')
        except InvalidRotorValues as Message:
            if self.choice_import_settings == 'y':
                print(f'{Message}. Seems like imported file contain incorrect rotor value.'+\
                    '\nPlease restart program with correct settings')
            elif self.choice_import_settings == 'n':
                print(f'{Message}. Insert proper values again.')
                # user must insert all settings again
                self.initiate_enigma_simulator(self.insert_settings_by_hand())
    
    '''
    TXT FILE EXPORTING PART
    '''
    def export_txt_menu(self, processed_text):
        '''Saving message to .txt file'''
        choice = None
        while choice != 'n':
            choice = input(f'\nWould you like create a file with ciphered text saved? y/n: ')
            try:
                if choice == 'y':
                    self.export_txt_file(processed_text)
                    break
                elif choice == 'n':
                    continue
                    # go to the next menu
                else:
                    raise UndefinedOption('Inserted option is undefined')
            except UndefinedOption as Message:
                print(f'{Message}. Insert option once again')

    def export_txt_file(self, message_to_save):
        while True:
            try:
                save_txt_file(message_to_save)
                break
            except UndefinedFileName as Message:
                print(f'{Message}. Insert proper name for the file')
            except WrongFileName as Message:
                print(f'{Message}. Give your file a different name')
    '''
    JSON FILE EXPORTING PART
    '''
    def export_json_menu(self, settings):
        '''Saving message to .txt file'''
        choice = None
        while choice != 'n':
            choice = input(f'\nWould you like create a .json file with settings saved? y/n: ')
            try:
                if choice == 'y':
                    self.export_json_file(settings)
                    break
                elif choice == 'n':
                    continue
                    # go to the next menu
                else:
                    raise UndefinedOption('Inserted option is undefined')
            except UndefinedOption as Message:
                print(f'{Message}. Insert option once again')

    def export_json_file(self, settings):
        while True:
            try:
                save_json_file(settings)
                break
            except UndefinedFileName as Message:
                print(f'{Message}. Insert proper name for the file')
            except WrongFileName as Message:
                print(f'{Message}. Give your file a different name')

    '''def exporting_txt_menu(self):
        while True:
            try:
                input_path = input(f'\nWrite file path with extension .json to insert settings into Enigma: ')
                if input_path:
                    alpha, beta, gama, steckerbrett, reflector = read_json_file(input_path)
                    return alpha, beta, gama, steckerbrett, reflector
                else:  # if input_file is empty, raise error
                    raise FileNotFound('File was not found')
            except FileNotFound as Message:
                print(f'{Message}. {self._insert_file_path}')'''


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

        if len(letter_pair) == 2:
            # checks if there is blank space in a pair of letters
            # I did not implement another function to check that condition,
            # because it is connected with the code in this function
            if " " in letter_pair:
                # raise an exception about wrong Steckerbrett formating
                raise SteckerbrettWrongFormat('Steckerbrett has wrong format')
        else:
            raise SteckerbrettWrongFormat('Steckerbrett has wrong format')
        # pairs of conjugated letters are updated into new dictionary
        new_dict.update({letter_pair[0]: letter_pair[1]})
    return new_dict

"""            

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

"""
def main():
    enigma = enigma_interface(Enigma)
    enigma.start_menu()
"""
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
                raise NoAsciiDetected('No ascii characters were inserted')
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

        #print(enigma._rotors)
        #shift = enigma.permutation(alpha)
        #print(shift)
        #print(enigma.permutation(shift))
        #inverted = enigma.inverse_permutation(alpha)
        #print(inverted)
        '''Returning message'''
        processed_text = enigma.encryptingCodec(ciphered_text)
        print(f'\nHere is encrypted message: processed_text)

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
    except NoAsciiDetected as Message:
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

"""

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
