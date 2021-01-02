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
        super().__init__('Steckerbrett must be a dict type')
        self.steckerbrett = steckerbrett

class SteckerbrettRepeatedValues(Exception):
    def __init__(self, steckerbrett):
        super().__init__('Steckerbrett must have different values')
        self.steckerbrett = steckerbrett

class OutOfRangeValue(Exception):
    def __init__(self, choice):
        super().__init__('Out of range value was chosen')
        self.choice = choice

class IncorrectReflector(Exception):
    def __init__(self, reflector):
        super().__init__('The value for the reflector is incorrect')
        self.reflector = reflector


'''
From file_management.py
'''

class NoAsciiInFile(Exception):
    def __init__(self, text):
        super().__init__('Files contains no ascii characters')
        self.text = text

class WrongNumberOfLines(Exception):
    pass
    '''def __init__(self, text):
        super().__init__('Files contains more than one line')'''

class FileWasNotFind(FileNotFoundError):
    pass
    '''def __init__(self, text):
        super().__init__('Files contains more than one line')'''

class UndefinedFileName(ValueError):
    pass

class WrongFileFormat(ValueError):
    pass
