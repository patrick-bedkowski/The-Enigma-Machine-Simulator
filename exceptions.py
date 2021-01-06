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


class SteckerbrettNotInText(Exception):
    def __init__(self, steckerbrett):
        super().__init__('\n> Steckerbrett contain characters not seen in inserted text')
        self.steckerbrett = steckerbrett


class ReflectorValueIsUndefined(ValueError):
    def __init__(self, reflector):
        super().__init__('\n> Inserted Reflector Value is Undefined')
        self.reflector = reflector


class OutOfRangeValue(Exception):
    def __init__(self, choice):
        super().__init__('\n> Out of range value was chosen')
        self.choice = choice


class IncorrectReflector(Exception):
    def __init__(self, reflector):
        super().__init__('\n> The value for the reflector is incorrect')
        self.reflector = reflector

class  NoReflectorSelected(Exception):
    def __init__(self, reflector):
        super().__init__('\n> No reflector has been selected')
        self.reflector = reflector

class UndefinedOption(ValueError):
    def __init__(self, choice):
        super().__init__('\n> Inserted option is undefined')
        self.choice = choice

class FileNotFound(ValueError):
    def __init__(self, input_file):
        super().__init__('\n> File was not found')
        self.input_file = input_file

class IncorrectRotorSettings(ValueError):
    def __init__(self, rotors):
        super().__init__('\n> Incorrect number of settings was inserted')
        self.rotors = rotors
    
class InvalidRotorValues(ValueError):
    def __init__(self, rotors):
        super().__init__('\n> Invalid rotor values')
        self.rotors = rotors

class InvalidRotorQuantity(ValueError):
    def __init__(self, rotors):
        super().__init__('\n> Invalid rotor quantity')
        self.rotors = rotors

class NoTextToProcess(ValueError):
    def __init__(self, input_txt):
        super().__init__('\n> No text was inserted')
        self.input_txt = input_txt

        


'''
From file_management.py
'''

'''class FileNotFoundError(Exception):
    def __init__(self, input_path):
        super().__init__('File was not found')
        self.input_path = input_path'''


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
