'''
Czy mogę ustalić w projekcie pewne zasady dla odczytywanego pliku?
e.g. muszą być same duże litery alfabetu bez żadnych innych znaków
'''
#from exceptions import NoAsciiInFile
from string import ascii_lowercase

'''IS THIS OPTIMAl???'''
def check_if_ascii(letter):  # checks if text is in ascii lowercases
    if letter.lower() in ascii_lowercase:
        return True
    else:
        raise NoAsciiInFile('Files contains no ascii characters')

class NoAsciiInFile(Exception):
    pass
    '''def __init__(self, text):
        super().__init__('Files contains no ascii characters')
        self.text = text'''

class WrongNumberOfLines(Exception):
    pass
    '''def __init__(self, text):
        super().__init__('Files contains more than one line')'''

class FileWasNotFind(FileNotFoundError):
    pass
    '''def __init__(self, text):
        super().__init__('Files contains more than one line')'''

def read_txt_file(path):
    try:
        with open(path, "r") as file:
            lines = file.readlines()  # file's lines
            if int(len(lines)) == 1:  # if there is only one line in file
                data = []
                for line in lines:
                    for letter in line:
                        if check_if_ascii(letter):
                            data.append(letter)
                return(''.join(data))
            else:
                raise WrongNumberOfLines('Files contains more than one line')
    except FileNotFoundError:
        raise FileWasNotFind('File was not find')

def format_to_dict(list_format):
    '''
    Input contains a list formated like: [letter_a letter_b, letter_c letter_d]
    This function will convert it to dictionary like: {'a': 'b', 'c': 'd'}
    A B, C D
    '''
    new_dict = {}
    index = list_format.split(",")
    for letters in index:
        split = letters.split(' ')
        new_dict.update({split[0]: split[1]})
    return new_dict

