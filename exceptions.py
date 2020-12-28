class SteckerbrettTypeError(Exception):
    def __init__(self, steckerbrett):
        super().__init__('Steckerbrett must be a dict type')
        self.steckerbrett = steckerbrett

class NoAsciiInFile(Exception):
    def __init__(self, text):
        super().__init__('Files contains no ascii characters')
        self.text = text
