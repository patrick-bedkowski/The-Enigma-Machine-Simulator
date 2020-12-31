from string import ascii_lowercase
from exceptions import (
    NoAsciiInFile,
    WrongFileFormat,
    WrongNumberOfLines,
    FileWasNotFind,
    UndefinedFileName
)
import json
from enigma import Enigma

'''IS THIS OPTIMAl???'''
def check_if_ascii(letter):  # checks if input is in ascii lowercases
    '''
    > It doesn't matter if the input is upper or lower character
    '''
    if letter.lower() in ascii_lowercase:
        return True
    else:
        return False

def get_input(text):
    return input(text)


'''
.txt file operations
'''

def read_txt_file(path):
    '''
    This function receives path to .txt file that later returns as string
    '''
    try:
        with open(path, "r") as file:  # open file
            lines = file.readlines()  # file's lines
            if int(len(lines)) == 1:  # if there is only one line in file
                data = []
                for line in lines:
                    for letter in line:
                        if check_if_ascii(letter):
                            data.append(letter)
                        else:
                            raise NoAsciiInFile('No ascii characters were inserted')
                return(''.join(data))  # return text
            else:
                raise WrongNumberOfLines('Files contains more than one line') # wrong format of the file
    except FileNotFoundError:
        raise FileWasNotFind('File was not find')

def save_txt_file(text):
    '''
    This function receives text that is later appended to the created .txt file
    > User chooses name of the file, and program adds .txt extension to it
    > Allowed characters used to name a file are numbers and letters from range a-z
    > If there is already a .txt file  with that name, program will overwrite this file
    '''

    '''
    User enters name of the file that will be created.
    Later that name is checked for unallowable characters
    '''
    # I implemented function "get_input" so It will be possible to monkeypatch it if I want to return empty input
    name_of_the_file = get_input('\nGive your file a name. Extension will be added automatically : ')
    if name_of_the_file:  # if name was inserted
        for letter in name_of_the_file:  # iterate through every letter
            if check_if_ascii(letter) or letter.isdigit():  # if letter mets assumpions continue
                continue
            else:
                raise WrongFileFormat('File name assumpions were not met')
    else:
        raise UndefinedFileName('No name was inserted')

    '''
    File is created
    '''
    with open(f"{name_of_the_file}.txt", "w") as file:
        file.write(text)

    '''
    Proper message is displayed
    '''
    print(f'\nFile {name_of_the_file}.txt was created in the main directory')
    #! Czy powinienem zapytać użytkownika o miejsce w jakim chce zapisać plik?

'''
Saving all settings
'''
def save_json_file(enigma):
    '''
    Creating dictionary to store settings from enigma object #! is it obj
    '''
    enigma_settings = {}
    enigma_settings['rotors'] = enigma.set_rotors()
    enigma_settings['steckenbrett'] = enigma.steckerbrett()
    enigma_settings['reflector'] = enigma.reflector()

    '''
    File is created
    '''
    with open('data.json', 'w') as filehandle:
        json.dump(enigma_settings, filehandle)

    '''
    Proper message is displayed
    '''
    print(f'\nFile data.json was created in the main directory')

'''
.json file operations
'''


