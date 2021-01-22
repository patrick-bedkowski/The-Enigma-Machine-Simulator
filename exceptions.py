'''
This module holds EXCEPTIONS used in enigma_class and enigma_interface
'''

class SteckerbrettTypeError(Exception):
    def __init__(self, steckerbrett):
        super().__init__('\n> Steckerbrett must be a dict type')
        self.steckerbrett = steckerbrett


class SteckerbrettRepeatedValues(Exception):
    def __init__(self, steckerbrett):
        super().__init__('\n> Steckerbrett must have different values')
        self.steckerbrett = steckerbrett


class SteckerbrettWrongFormat(Exception):
    def __init__(self, steckerbrett):
        super().__init__('\n> Steckerbrett has wrong format')
        self.steckerbrett = steckerbrett


class SteckerbrettValueError(Exception):
    def __init__(self, steckerbrett):
        super().__init__('\n> Value inserted into Steckerbrett is incorrect')
        self.steckerbrett = steckerbrett


class ReflectorValueIsUndefined(ValueError):
    def __init__(self, reflector):
        super().__init__('\n> Inserted Reflector Value is Undefined')
        self.reflector = reflector


class IncorrectReflector(Exception):
    def __init__(self, reflector):
        super().__init__('\n> The value for the reflector is incorrect')
        self.reflector = reflector


class NoReflectorSelected(Exception):
    def __init__(self, reflector):
        super().__init__('\n> No reflector has been selected')
        self.reflector = reflector


class OutOfRangeValue(Exception):
    def __init__(self, choice):
        super().__init__('\n> Out of range value was chosen')
        self.choice = choice


class InvalidRotorQuantity(ValueError):
    def __init__(self, list_of_rotors):
        super().__init__('\n> Invalid rotor quantity')
        self.list_of_rotors = list_of_rotors


class InvalidRotorValues(ValueError):
    def __init__(self, rotors):
        super().__init__('\n> Invalid rotor values')
        self.rotors = rotors


class UndefinedOption(ValueError):
    def __init__(self, choice):
        super().__init__('\n> Inserted option is undefined')
        self.choice = choice


class FileNotFound(ValueError):
    def __init__(self, input_file):
        super().__init__('\n> File was not found')
        self.input_file = input_file


class NoTextToProcess(ValueError):
    def __init__(self, input_txt):
        super().__init__('\n> No text was inserted')
        self.input_txt = input_txt


class NoAsciiDetected(ValueError):
    def __init__(self, text):
        super().__init__('\n> No ascii characters were inserted')
        self.text = text


class WrongNumberOfLines(ValueError):
    def __init__(self, text):
        super().__init__('\n> Files does not contain one line. Format it or choose a different one')
        self.text = text


class UndefinedFileName(NameError):
    def __init__(self, name):
        super().__init__('\n> No name was inserted')
        self.name = name


class WrongFileName(NameError):
    def __init__(self, name):
        super().__init__('\n> File name assumpions were not met')
        self.name = name


class DecodeError(Exception):
    def __init__(self, variable):
        super().__init__('\n> Inserted settings file is incorrect')
        self.variable = variable
