from enigma_class import Enigma
from string import ascii_uppercase
import sys
from file_management import (
    read_txt_file,
    save_txt_file,
    read_json_file,
    save_json_file
)
from tabulate import tabulate
from exceptions import (
    UndefinedOption,
    SteckerbrettRepeatedValues,
    SteckerbrettWrongFormat,
    SteckerbrettValueError,
    ReflectorValueIsUndefined,
    NoAsciiDetected,
    WrongNumberOfLines,
    InvalidRotorValues,
    WrongFileName,
    UndefinedFileName,
    FileNotFound,
    NoReflectorSelected,
    InvalidRotorQuantity,
    NoTextToProcess,
    DecodeError
)

# Enigma welcome label
from pyfiglet import Figlet
text = Figlet(font='big')


class Enigma_interface:
    def __init__(self, Enigma):
        self._name = 'Enigma Simulator'
        self._option = '\nPlease, insert correct option number'
        self._insert_file_path = 'Please, insert file path again'
        self._return_message = '\nIf you wish to return to main menu, type "y": '
        # Message displayed after keyboard interruption
        self._key_interruption = "\n\nKeyboard interruption detected. Thank you for using my Enigma Simulator."
        self.choice_import_settings = None

    def design_assumptions(self):
        '''
        Asumptions for the inputs. It descibes how to insert values properly
        '''
        assumpions_dist = [
            ['Text',
                f'{chr(62)} must be inserted as uppercases characters\n'+
                f'{chr(62)} must only contain characters of the alphabet in range A-Z\n'+
                f'{chr(62)} must not contain hard spaces'
            ],
            ['Steckerbrett',
                f'{chr(62)} can be left empty\n'+
                f'{chr(62)} must be inserted in pair of letters separated by a commas, e.g. AB,CD\n'+
                f'{chr(62)} must be inserted as uppercases characters\n'+
                f'{chr(62)} must not hold two identical letters'
            ],
            ['Rotors',
                f'{chr(62)} must be inserted in a number of three values separated by a comma, e.g. 1,2,3\n'+
                f'{chr(62)} each value must be a number from range 1-26'
            ],
            ['Reflector',
                f'{chr(62)} must be inserted as one letter choosen from A, B, C'
            ],
            ['Save/Import File name',
                f'{chr(62)} must only consist of characters of the alphabet in range a-z and integer numbers\n'+
                f'{chr(62)} uppercase and lowercase values of letters are acceptable'
            ],
            ['Imported .txt file',
                f'{chr(62)} must consists of characters of the alphabet in range a-z\n'+
                f'{chr(62)} must be inserted as uppercases characters\n'+
                f'{chr(62)} text must be saved in a single line'
            ],
            ['Option Answers ',
                f'{chr(62)} answer must be chosen between ones specified in program and inserted in given way\n'
                +'  e.g. "Insert y/n", you can insert "y" as an affirmative answer, or "n" as negative'
            ]
        ]
        return assumpions_dist

    def keyboard_interruption(self):
        return self._key_interruption

    def start_options(self):
        '''Returns options of intiating simulator'''
        options = [
            ['1. Read text from file',
            '2. Enter own text',
            '3. View design assumptions of the simulator',
            '4. Quit']
        ]
        return options

    def main_menu(self):
        try:
            # initiate menu
            self.start_menu()
            # initaite settings
            list_of_rotors, steckerbrett, reflector = self.setting_menu()
            # after settings are imported, initiate program
            self.initiate_enigma_simulator(list_of_rotors, steckerbrett, reflector)
        except KeyboardInterrupt:
            # If program was interrupted by the key, print message
            print(self.keyboard_interruption())
            sys.exit()

    def start_menu(self):
        '''Returns ciphered text, if proper option was choosen and text was inserted properly'''
        # Prints formated name of simulator
        print(text.renderText(self._name))
        while True:
            # present availabe options to user
            print('\n' + tabulate(self.start_options(), tablefmt='fancy_grid'))
            # empty str
            ciphered_text = ''
            # user inputs option
            choice = input('\nInsert a number of option that you want to use: ')
            if choice == '1':
                ciphered_text = self.input_txt_file()
            elif choice == '2':
                ciphered_text = self.input_txt_by_hand()
            elif choice == '3':
                # print design assumptions
                self.display_assumptions()
            elif choice == '4':
                # Quit application
                print('\nThank you for using The Enigma Machine Simulator')
                sys.exit()
            else:
                print(self._option)
            # if text has been inserted
            if ciphered_text:
                self.ciphered_text = ciphered_text
                break

    '''DISPLAY ASSUMPTIONS'''

    def display_assumptions(self):
        '''This function prints design assumptions for the inputs'''
        print(tabulate(self.design_assumptions(), tablefmt='fancy_grid'))
        while True:
            choice = input(self._return_message)
            if choice == 'y':
                # return to main menu
                break
            else:
                print(self._option)

    '''INPUT TXT PART'''

    def input_txt_file(self):
        '''Imports text from file'''

        while True:
            print(self._return_message)
            input_file = input('\nWrite file path with extension .txt to insert into Enigma: ')
            #
            if input_file == 'y':
                # return to main menu
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

    '''INPUT TXT MANUALLY'''

    def input_txt_by_hand(self):
        '''Returns text inserted by a user'''
        while True:
            print(self._return_message)
            input_txt = input('\nWrite message that you want to insert into Enigma: ')
            if input_txt == 'y':
                # return to main menu
                break
            try:
                if input_txt:
                    # if inserted text contains characters different that ones
                    # from uppercase ascii alphabet, raise an error
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

    def setting_menu(self):
        # User have a choice to import Enigma Simulator Settings from .json file.
        # If user chooses to import settings, he probably doesn't need to save them later in the program.
        # The choice will be remembered and used to initiate "save_json_file" block
        while True:
            choice_import_settings = input(
                '\nWould you like to import Enigma settings from the json file? y/n: '
            )
            if choice_import_settings == 'y':
                # saves user's choice for later use
                self.choice_import_settings = choice_import_settings
                # reads data entered by hand
                list_of_rotors, steckerbrett, reflector = self.import_settings_from_file()
                # after settings have been returned initiate program
                return list_of_rotors, steckerbrett, reflector
            elif choice_import_settings == 'n':
                self.choice_import_settings = choice_import_settings
                # reads data entered by hand
                list_of_rotors, steckerbrett, reflector = self.insert_settings_by_hand()
                # after settings have been initiate program
                return list_of_rotors, steckerbrett, reflector
            else:
                print(self._option)

    '''IMPORT SETTINGS FROM JSON'''

    def import_settings_from_file(self):
        '''Reading settings from to .json file'''
        while True:
            try:
                input_path = input('\nWrite file path with extension .json to insert settings into Enigma: ')
                if input_path:
                    list_of_rotors, steckerbrett, reflector = read_json_file(input_path)
                    # after settings are imported, initiate program
                    return list_of_rotors, steckerbrett, reflector
                else:  # if input_file is empty, raise error
                    raise FileNotFound('File was not found')
            except FileNotFound as Message:
                print(f'{Message}. {self._insert_file_path}')
            except DecodeError as Message:
                print(f'{Message}. Inserted file might contain incorrect data.')

    '''INSERT SETTINGS MANUALLY'''

    '''ROTORS'''
    def insert_settings_by_hand(self):
        '''
        Returns values of rotors in a list, steckerbrett as dictionary, reflector as str
        This function is executed when user wants to enter enigma settings by hand
        '''
        list_of_rotors = self.insert_rotors_values()
        steckerbrett = self.insert_steckerbrett_by_hand()
        reflector = self.insert_reflector_value()
        # after settings are inserted, initiate program
        return list_of_rotors, steckerbrett, reflector

    '''STECKERBRETT'''
    def insert_steckerbrett_by_hand(self):
        '''Returns inserted steckerbrett formated into dictionary'''
        while True:
            steckerbrett = input('\nInsert Steckerbreit values that you want to switch in format "AB,CD": ')
            if steckerbrett:
                # string characters are converted into dictionary
                # and its checked if inserted steckerbrety has empty hard spaces
                try:
                    steckerbrett = self.format_to_dict(steckerbrett)
                    return steckerbrett
                except SteckerbrettWrongFormat as Message:
                    print(f'{Message}. Insert values once again')
                except SteckerbrettRepeatedValues as Message:
                    print(f'{Message}. Insert values once again')

            else:
                # Steckerbrett can have empty str value
                return steckerbrett

    def format_to_dict(self, steckerbrett_str):
        '''
        Function is collecting inserted string values of conjugated letters
        that are separated by a comma. It converts them to a dictionary with
        key and value as conjugated letters. Function returns a dictionary.
        This function also checks if letters inserted into steckerbrett
        '''
        '''
        Values must be inserted like so AB,CD
        This function will convert str value to dictionary like: {'A': 'B', 'C': 'D'}
        '''
        # create a new dictionary to hold keys and values
        new_dict = {}
        # split pairs of letters separated by a comma and create a list
        list_of_letter_pairs = steckerbrett_str.split(",")

        # if steckerbrett inserted
        if steckerbrett_str:
            # iterate through a list containing letters
            for letter_pair in list_of_letter_pairs:
                if len(letter_pair) == 2:
                    # check if there is hard space in a pair of letters
                    # check if first letter in pair is not present in the new dictionary as key
                    if self.check_if_key_contain_space(letter_pair):
                        if self.check_if_key_is_not_repeated(letter_pair, new_dict):
                            new_dict.update({letter_pair[0]: letter_pair[1]})
                else:
                    raise SteckerbrettWrongFormat('Steckerbrett has wrong format')
                # pairs of conjugated letters are updated into new dictionary
        return new_dict

    def check_if_key_contain_space(self, letter_pair):
        '''Raises Error if Steckerbrett holds whitespaces'''
        if " " in letter_pair:
            # raise an exception about wrong Steckerbrett formating
            raise SteckerbrettWrongFormat('Steckerbrett has wrong format')
        else:
            return True

    def check_if_key_is_not_repeated(self, letter_pair, new_dict):
        # if dictionary is not empty
        if new_dict:
            # iterate through keys and values
            for key in new_dict.keys():
                # check if first letter of pair is not in the dictionary as a key
                # When that happens python would simply change value of the inserted key
                # It is necessary to check that condition in this module
                if letter_pair[0] == key:
                    raise SteckerbrettRepeatedValues('Steckerbrett must have different values')
                else:
                    return True
        else:
            return True

    '''ROTORS'''
    def insert_rotors_values(self):
        '''Returns list of rotor values'''
        while True:
            rotors = input('\nInsert three rotor settings separated by comma (numbers 1-26): ')
            try:
                list_of_rotors = self.create_list_of_rotors(rotors)
                return list_of_rotors
            except InvalidRotorValues as Message:
                print(f'{Message}. Insert values once again')
            except InvalidRotorQuantity as Message:
                print(f'{Message}. Insert values once again')

    def create_list_of_rotors(self, rotors):
        '''Returns list of rotor values. Raises Errors, if inserted settings do not meet conditions'''
        # if rotor is not empty
        if rotors:
            # Raises error if there is hard space or one value is missing in str
            if ' ' in rotors or ',,' in rotors:
                raise InvalidRotorValues('Invalid rotor values')

            # create list of splited elements separated by a comma
            list_of_rotors = rotors.split(',')

            # Raises error if there is an empty value like 1,,3
            if all(list_of_rotors) is False:
                raise InvalidRotorValues('Invalid rotor values')
            else:
                # convert values to int
                list_of_rotors = [int(rotor) for rotor in list_of_rotors]
                return list_of_rotors
        else:
            raise InvalidRotorQuantity('Invalid rotor quantity')

    '''REFLECTOR'''

    def insert_reflector_value(self):
        '''Returns value of reflector'''
        while True:
            reflector = input('\nWhich reflector would you like to choose? (A, B, C): ')
            try:
                if self.check_if_reflector_inserted(reflector):
                    return reflector
            except NoReflectorSelected as Message:
                print(f'{Message}. Insert values once again')

    def check_if_reflector_inserted(self, reflector):
        '''Returns true, if the reflector value has been inserted.
        Note that this function does not check the correctness of the input value.
        This condition is checked in the enigma_class file'''
        if reflector:
            return True
        else:
            raise NoReflectorSelected('No reflector has been selected')

    '''Initiating program'''

    def initiate_enigma_simulator(self, list_of_rotors, steckerbrett, reflector):
        '''Here is the main algorythm'''
        try:
            # create object of Enigma class
            enigma = Enigma(list_of_rotors, steckerbrett, reflector)
            processed_text = enigma.encryptingCodec(self.ciphered_text)
            print(f'\nHere is your encrypted message: {processed_text}')

            # Exporting files requires
            # processed text and initial settings
            self.export_txt_menu(processed_text)

            # If user has chosen not to import settings from file
            # Exporting settings inserted by hand is available
            if self.choice_import_settings == 'n':
                self.export_json_menu(enigma.initial_settings)

            # print last message
            print('\nThank you for using my Enigma Machine Simulator')
            '''
            All this exceptions regarding values correctness are raised in enigma_class.py
            '''
        except (InvalidRotorValues,
                InvalidRotorQuantity,
                SteckerbrettRepeatedValues,
                SteckerbrettValueError,
                ReflectorValueIsUndefined) as Message:
            # If incorrect values have been inserted user will be asked to insert them again
            self.initiate_enigma_again(Message)

    def initiate_enigma_again(self, Message):
        '''This function is executed when values inserted by the user were not
        accepted by the enigma_class '''
        if self.choice_import_settings == 'y':
            print(f'{Message}. Seems like imported file contains incorrect settings.'+
                '\nPlease insert all settings again')
            # user must insert all settings again
            list_of_rotors, steckerbrett, reflector = self.setting_menu()
            # after settings are imported, initiate program
            self.initiate_enigma_simulator(list_of_rotors, steckerbrett, reflector)
        elif self.choice_import_settings == 'n':
            print(f'{Message}. Insert all settings again.')
            # user must insert all settings again
            list_of_rotors, steckerbrett, reflector = self.setting_menu()
            # after settings are imported, initiate program
            self.initiate_enigma_simulator(list_of_rotors, steckerbrett, reflector)

    '''
    TXT FILE EXPORTING PART
    '''
    def export_txt_menu(self, processed_text):
        '''Saving message to .txt file'''
        choice = None
        while choice != 'n':
            choice = input('\nWould you like to create a file with saved ciphered text? y/n: ')
            try:
                if choice == 'y':
                    self.export_txt_file(processed_text)
                    break
                elif choice == 'n':
                    continue
                    # go back to initiate_enigma_simulator
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
            choice = input('\nWould you like create a .json file with settings saved? y/n: ')
            try:
                if choice == 'y':
                    self.export_json_file(settings)
                    break
                elif choice == 'n':
                    continue
                    # go back to initiate_enigma_simulator
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
