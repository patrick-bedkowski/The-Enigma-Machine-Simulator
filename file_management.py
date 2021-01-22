from string import ascii_letters
from exceptions import (
    NoAsciiDetected,
    WrongFileName,
    WrongNumberOfLines,
    UndefinedFileName,
    FileNotFound,
    NoTextToProcess,
    DecodeError
)
import json


def check_if_ascii(letter):
    '''
    Function returns True if argument is an alphabet character
    '''
    if letter in ascii_letters:
        return True
    else:
        return False


'''
TXT file operations
'''


def read_txt_file(input_file):
    '''
    This function receives path to .txt file that later returns as string
    '''
    try:
        with open(input_file, "r") as file:  # open file
            lines = file.readlines()  # file's lines
            # if any line from file is empty, raise error
            if any(len(line.strip()) == 0 for line in lines):
                raise NoTextToProcess('No text was inserted')
            else:
                if int(len(lines)) == 1:  # if there is only one line in file
                    data = []
                    for line in lines:
                        for letter in line:
                            if check_if_ascii(letter):
                                data.append(letter)
                            else:
                                raise NoAsciiDetected('No ascii characters were inserted')
                    text = ''.join(data)
                    return text  # return text
                else:
                    raise WrongNumberOfLines('Files does not contain one line. Format it or choose a different one')
    except FileNotFoundError:
        raise FileNotFound('File was not found')


def save_txt_file(text):
    '''
    This function receives text that is later appended to the created .txt file
    > User chooses name of the file, and program adds .txt extension to it
    > Allowed characters used to name a file are numbers and letters from range a-z upper and lowercases
    > If there is already a .txt file with that name, program will overwrite this file
    '''

    '''
    User enters name of the file that will be created.
    Later that name is checked for unallowable characters
    '''
    name_of_the_file = input('\nGive your file a name. Extension will be added automatically : ')
    if name_of_the_file:  # if name was inserted
        # Create file
        create_file_txt(name_of_the_file, text)
        '''
        Proper message is displayed
        '''
        print(f'\nFile {name_of_the_file}.txt was created in the main directory')
    else:
        raise UndefinedFileName('No name was inserted')


def create_file_txt(name_of_the_file, text):
    '''
    Function creates a file using name from the argument.
    Raises an error If filename contain
    '''
    # iterate through every character
    for character in name_of_the_file:
        # letter is checked for characters from ascii alphabet
        if check_if_ascii(character) or character.isdigit():  # if letter mets assumpions continue
            continue  # if assumptions are met, continue iterating
        else:
            raise WrongFileName('File name assumpions were not met')
    # If no exception has been raised create file
    with open(f"{name_of_the_file}.txt", "w") as file:
        file.write(text)


'''
JSON file operations
'''


def save_json_file(settings):
    '''
    This function saves all the initial settings of the enigma machine to the json file
    '''

    name_of_the_file = input('\nGive your file a name. Extension will be added automatically : ')
    if name_of_the_file:  # if name was inserted
        # Create file
        create_file_json(name_of_the_file, settings)
        # Proper message is displayed
        print(f'\n{name_of_the_file}.json was created in the main directory')
    else:
        raise UndefinedFileName('No name was inserted')


def create_file_json(name_of_the_file, settings):
    '''
    This function receives text that is later appended to the created .txt file
    > User chooses name of the file, and program adds .txt extension to it
    > Allowed characters used to name a file are numbers and letters from range a-z upper and lowercases
    > If there is already a .txt file with that name, program will overwrite this file
    '''
    for letter in name_of_the_file:  # iterate through every letter
        # letter is checked for characters from ascii alphabet
        if check_if_ascii(letter) or letter.isdigit():  # if letter mets assumpions continue
            continue
        else:
            raise WrongFileName('File name assumpions were not met')
    # If no exception has been raised continue
    '''
    File is created
    '''
    # create json file, add .json extension
    with open(f'{name_of_the_file}.json', 'w') as filehandle:
        json.dump(settings, filehandle)


def read_json_file(path):
    '''
    This function receives path to .json file that later returns settings.
    '''
    try:
        with open(path, "r") as filehandle:  # open file
            data = json.load(filehandle)
            list_of_rotors = data['rotors']
            steckenbrett = data['steckenbrett']
            reflector = data['reflector']
            return list_of_rotors, steckenbrett, reflector
    except FileNotFoundError:
        raise FileNotFound('File was not found')
    except json.JSONDecodeError:
        raise DecodeError('\n> Inserted settings file is incorrect')
    # DecodeError is raised when argument inserted into function is not an json file,
    # e.g. inserted file is txt and JSON cannot decode it
