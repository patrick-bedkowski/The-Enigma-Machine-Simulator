'''
HOW TO RAISE EXCEPTIONS

def method(self):
  raise Exception("Bad stuff")

def main():
  try:
    method()
  except Exception as e:
    print(f"Hello user this error just happened :( {e}")
'''


class SteckerbrettTypeError(Exception):
    def __init__(self, steckerbrett):
        super().__init__('\nSteckerbrett must be a dict type')
        self.steckerbrett = steckerbrett


class SteckerbrettRepeatedValues(Exception):
    def __init__(self, steckerbrett):
        super().__init__('\nSteckerbrett must have different values')
        self.steckerbrett = steckerbrett


class SteckerbrettWrongFormat(Exception):
    def __init__(self, steckerbrett):
        super().__init__('\nSteckerbrett has wrong format')
        self.steckerbrett = steckerbrett


class SteckerbrettNotInText(Exception):
    def __init__(self, steckerbrett):
        super().__init__('\nSteckerbrett contain characters not seen in inserted text')
        self.steckerbrett = steckerbrett


class ReflectorValueIsUndefined(ValueError):
    def __init__(self, reflector):
        super().__init__('\nInserted Reflector Value is Undefined')
        self.reflector = reflector


class OutOfRangeValue(Exception):
    def __init__(self, choice):
        super().__init__('\nOut of range value was chosen')
        self.choice = choice


class IncorrectReflector(Exception):
    def __init__(self, reflector):
        super().__init__('\nThe value for the reflector is incorrect')
        self.reflector = reflector

class  NoReflectorSelected(Exception):
    def __init__(self, reflector):
        super().__init__('\nNo reflector has been selected')
        self.reflector = reflector

class UndefinedOption(ValueError):
    def __init__(self, choice):
        super().__init__('\nInserted option is undefined')
        self.choice = choice


class FileNotFound(ValueError):
    def __init__(self, input_file):
        super().__init__('\nFile was not found')
        self.input_file = input_file

class IncorrectRotorSettings(ValueError):
    def __init__(self, rotors):
        super().__init__('\nIncorrect number of settings was inserted')
        self.rotors = rotors
    
class InvalidRotorValues(ValueError):
    def __init__(self, rotors):
        super().__init__('\nInvalid rotor values')
        self.rotors = rotors

class InvalidRotorQuantity(ValueError):
    def __init__(self, rotors):
        super().__init__('\nInvalid rotor quantity')
        self.rotors = rotors


'''
From file_management.py
'''

'''class FileNotFoundError(Exception):
    def __init__(self, input_path):
        super().__init__('File was not found')
        self.input_path = input_path'''


class NoAsciiDetected(ValueError):
    def __init__(self, text):
        super().__init__('\nNo ascii characters were inserted')
        self.text = text


class WrongNumberOfLines(ValueError):
    def __init__(self, text):
        super().__init__('\nFile contains more than one line of text')
        self.text = text


class UndefinedFileName(NameError):
    def __init__(self, name):
        super().__init__('\nNo name was inserted')
        self.name = name


class WrongFileName(NameError):
    def __init__(self, name):
        super().__init__('\nFile name assumpions were not met')
        self.name = name
