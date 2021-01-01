from string import ascii_uppercase
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
def check_if_ascii(letter):  # checks if input is in ascii uppercases
    '''
    > It doesn't matter if the input is upper or lower character
    '''
    if letter.lower() in ascii_uppercase:
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
        raise FileWasNotFind('File was not found')

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
.json file operations
'''

def save_json_file(enigma):
    '''
    This function saves all the initial settings of the enigma
    machine to the json file
    '''

    #File is created
    with open('data.json', 'w') as filehandle:
        json.dump(enigma.initial_settings(), filehandle)

    '''
    Proper message is displayed
    '''
    print(f'\nFile data.json was created in the main directory')


def read_json_file(path):
    '''
    This function receives path to .json file that later returns settings
    '''
    try:
        with open(path, "r") as filehandle:  # open file
            data = json.load(filehandle)
            rotors = data['rotors']
            steckenbrett = data['steckenbrett']
            reflector = data['reflector']
            return rotors[0], rotors[1], rotors[2], steckenbrett, reflector
    except FileNotFoundError:
        raise FileWasNotFind('File was not found')

