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
        super().__init__('Steckerbrett must be a dict type\n')
        self.steckerbrett = steckerbrett

class SteckerbrettRepeatedValues(Exception):
    def __init__(self, steckerbrett):
        super().__init__('Steckerbrett must have different values\n')
        self.steckerbrett = steckerbrett

class OutOfRangeValue(Exception):
    def __init__(self, choice):
        super().__init__('Out of range value was chosen\n')
        self.choice = choice

class IncorrectReflector(Exception):
    def __init__(self, reflector):
        super().__init__('The value for the reflector is incorrect\n')
        self.reflector = reflector

class UndefinedOption(ValueError):
    def __init__(self, choice):
        super().__init__('Inserted option is undefined\n')
        self.choice = choice

class FileNotFound(ValueError):
    def __init__(self, input_file):
        super().__init__('File was not found\n')
        self.input_file = input_file

class IncorrectRotorSettings(ValueError):
    pass

class InvalidRotorValues(ValueError):
    pass


'''
From file_management.py
'''

'''class FileNotFoundError(Exception):
    def __init__(self, input_path):
        super().__init__('File was not found')
        self.input_path = input_path'''

class NoAsciiInFile(Exception):
    def __init__(self, text):
        super().__init__('Files contains no ascii characters\n')
        self.text = text

class WrongNumberOfLines(Exception):
    pass
    '''def __init__(self, text):
        super().__init__('Files contains more than one line')'''

class UndefinedFileName(ValueError):
    pass

class WrongFileFormat(ValueError):
    pass
