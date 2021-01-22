from string import ascii_uppercase
from exceptions import (
    ReflectorValueIsUndefined,
    InvalidRotorValues,
    SteckerbrettRepeatedValues,
    SteckerbrettValueError,
    InvalidRotorQuantity
)

class Enigma:

    def __init__(self, list_of_rotors = [1, 1, 1], steckerbrett = {}, reflector = 'A'):
        '''
        Class Enigma. Contains attributes:

        :param list_of_rotors: initial rotor settings
        :type list_of_rotors: list
        :default list_of_rotors: [1, 1, 1]

        :param steckerbrett: Steckerbrett shows which letters should be replaceed with another
        :type steckerbrett: dict
        :default steckerbrett: {}

        :param reflector: initial reflector setting of the rotor
        :type reflector: str
        :default reflector: 'A'

        :param alpha: initial rotor setting
        :type alpha: int

        :param beta: initial rotor setting
        :type beta: int

        :param gamma: initial rotor setting
        :type gamma: int

        :param alphabet: uppercase ascii alphabet
        :type gamma: list

        :param initial_settings: holds inserted settings
        :type initial_settings: dict
        '''

        '''
        ascii_uppercase is a string holding "ABCDEF..."
        Alphabet atribute is holding list consisting of ascii_uppercase characters
        '''
        self._alphabet = [letter for letter in ascii_uppercase]

        '''Checks rotor values'''
        if len(list_of_rotors) == 3:
            self._alpha = self._check_set_rotor_value(list_of_rotors[0])
            self._beta = self._check_set_rotor_value(list_of_rotors[1])
            self._gamma = self._check_set_rotor_value(list_of_rotors[2])
            self._list_of_rotors = list_of_rotors
        else:
            raise InvalidRotorQuantity('Invalid rotor quantity')

        # If steckerbrett has been inserted, check its content
        if steckerbrett:
            if (
                self._steckerbrett_check_for_same_values(steckerbrett)
                and self._steckerbrett_check_values(steckerbrett)
            ):
                self._steckerbrett = steckerbrett
        else:
            # if steckerbrett is empty, assign an empty dictionary to it
            self._steckerbrett = steckerbrett

        # if inserted reflector is in list of defined values, initiate reflector
        if self._reflector_check_model(reflector):
            self._reflector = reflector

        # save initial settings, before they are changed
        # due to the program changing some of them
        self.initial_settings = self._initial_settings()

    def _check_set_rotor_value(self, rotor):
        '''This function checks If inserted rotors are in range 1-26'''
        try:
            if rotor not in range(1, 27):
                raise InvalidRotorValues('Invalid rotor values')
            else:
                return int(rotor)
        except ValueError:
            raise InvalidRotorValues('Invalid rotor values')

    '''STECKERBRETT / PLUGBOARD'''

    def _steckerbrett_check_for_same_values(self, steckerbrett_dict):
        '''
        Steckerbrett cannot hold two same values. This function checks if
        a character is repeated, either as a key or a value. Return True if
        there is no duplicates
        '''
        # create a list where detected values, keys are stored
        detected_values_keys = []

        # iterate through keys, values
        for key, value in steckerbrett_dict.items():
            # if key, value is the same as in the detection list, raise an error
            if key in detected_values_keys or value in detected_values_keys:
                raise SteckerbrettRepeatedValues('Steckerbrett must have different values')
            elif key == value:
                raise SteckerbrettRepeatedValues('Steckerbrett must have different values')
            else:
                # if key, value repetition has not been detected, append them into detection list
                detected_values_keys.extend([key, value])
        # return information that repetition of the values has not been detected
        return True

    def _steckerbrett_check_values(self, steckerbrett_dict):
        '''
        Steckerbrett cannot hold values that are not characters in used alphabet.
        Function Returns Boolean value True, or raises error.
        '''
        for key, value in steckerbrett_dict.items():
            if key in self._alphabet and value in self._alphabet:
                continue
            else:
                raise SteckerbrettValueError('Value inserted into Steckerbrett is incorrect')
        return True

    '''REFLECTOR'''

    def _reflector_check_model(self, reflector):
        '''Returns Boolean Value True if inserted reflector value
        matches reflectors specified in the project'''
        list_of_supported_reflectors = ['A', 'B', 'C']
        if reflector not in list_of_supported_reflectors:
            raise ReflectorValueIsUndefined('Inserted Reflector Value is Undefined')
        else:
            return True

    def _reflector_alphabet(self):
        '''
        Returns a lsit with reflector alphabet in it, based on the choosing of the reflector
        '''
        '''
        Each of the specific reflector has defined alphabet,
        that must not be changed.
        These are original reflector settings used in Engima machine from 1939
        '''
        if self._reflector == "A":
            # Original setting for reflector type UKW-A
            return [
                'E','J','M','Z','A','L','Y','X','V','B','W','F','C',
                'R','Q','U','O','N','T','S','P','I','K','H','G','D'
            ]
        elif self._reflector == "B":
            # Original setting for reflector type UKW-B
            return [
                'Y','R','U','H','Q','S','L','D','P','X','N','G','O',
                'K','M','I','E','B','F','Z','C','W','V','J','A','T'
            ]
        elif self._reflector == "C":
            # Original setting for reflector type UKW-C
            return [
                'F','V','P','J','I','A','O','Y','E','D','R','Z','X',
                'W','G','C','T','K','U','Q','S','B','N','M','H','L'
            ]

    '''Save initial settings'''

    def _initial_settings(self):
        '''
        This method saves initial settings of the machine, before each rotor value
        is changed due to the ciphering process.
        It returns dictionary with keys as name of the setting, and values as a value of the setting.
        '''
        # Creating dictionary to store initial settings
        enigma_settings = {}
        enigma_settings['rotors'] = self._list_of_rotors
        enigma_settings['steckenbrett'] = self._steckerbrett
        enigma_settings['reflector'] = self._reflector
        return enigma_settings

    '''Heart of an algorythm.'''

    def _turn_rotors(self):
        '''Turn the rotors'''

        # All rotors are in border position (26,26,26)
        if self._gamma % 26 == 0 and self._beta % 26 == 0 and self._alpha % 26 == 0:
            self._alpha = 1
            self._beta = 1
            self._gamma = 1
        # Rotor A and B are in border position (26,26,x) x < 26
        elif self._beta % 26 == 0 and self._alpha % 26 == 0:
            self._alpha = 1
            self._beta = 1
            self._gamma += 1
        # Rotor A is in border position (26,x,x) x < 26
        elif self._alpha % 26 == 0:
            self._alpha = 1
            self._beta += 1
        # None of rotors is in border position (x,x,x) x < 26
        else:
            self._alpha += 1

    def _rotor_alphabet(self, rotor):
        '''Returns a list with rotor alphabet, based on the choosing of the rotor in method's parameter'''

        if rotor == 'alpha':
            # Original settings for the alpha rotor
            rotor_alphabet = [
                'E','K','M','F','L','G','D','Q','V','Z','N','T','O',
                'W','Y','H','X','U','S','P','A','I','B','R','C','J'
            ]
        elif rotor == 'beta':
            # Original settings for the beta rotor
            rotor_alphabet = [
                'A','J','D','K','S','I','R','U','X','B','L','H','W',
                'T','M','C','Q','G','Z','N','P','Y','F','V','O','E'
            ]
        elif rotor == 'gamma':
            # Original settings for the gamma rotor
            rotor_alphabet = [
                'B','D','F','H','J','L','C','P','R','T','X','V','Z',
                'N','Y','E','I','W','G','A','K','M','U','S','Q','O'
            ]
        return rotor_alphabet

    def _shift(self, alphabet, n):
        '''Returns input alphabet shifted to right n-1 times. n is the current setting of rotor'''
        '''not n times, because when rotor is in 1 position its
        shifted alphabet will return the same hardcoded/not shifted list,
        as in the origial machine'''
        return alphabet[(-n+1):] + alphabet[:(-n+1)]

    def _steckerbrett_change_letters(self, letter):
        '''
        If letter is in steckerbrett, switch it for the corresponding one
        '''
        '''
        When letter is inserted to simulator it is checked for steckerbrett keys,
        values. If letter has been found on key or value position,
        it is changed for the corresponding one.

        Input/Output:            A                    C
                                 |                    |
        conjuncted letters:     [A - M]          [B - C]
                                     |            |
                                     |            |
        Rotor operations:            .M -> ... -> B.
        '''
        for key, value in self._steckerbrett.items():
            if letter == key:
                letter = value
            elif letter == value:
                letter = key
            else:
                continue
            # if no matches have been found, letter will not be changed
        return letter

    def encryptingCodec(self, inserted_text):
        '''
        Returns processed ciphered_text
        '''
        ciphered_text = []
        for letter in inserted_text:

            # if two letters are conjuncted, one is switched with the other
            # for further coding
            if self._steckerbrett:
                letter = self._steckerbrett_change_letters(letter)

            # before first letter has been replaced, turn rotors
            self._turn_rotors()

            '''Main ciphering algorithm'''

            '''
            For better understanding upcoming algorythm, it is highly recommended
            to open how_TEMS_work file, where this process is explained using images.

            First, self._rotor_alphabet gets a list with specific rotor alphabet. After that ROTOR'S alphabet
            is shifted (self._alpha - 1) times the right. That produces a list that defines letter changing.
            Then, it is calculated what index has a LETTER (inserted into the rotor) in ascii alphabet,
            using .index() on self._alphabet.
            At the end, new letter is selected from previously selected list on the same index.
            '''

            '''EACH alphabet of the rotor defines how letter is changed with one another when it is inserted
            into the rotor. To better understand this process, align together ascii and rotor alphabet:
            ASCII alphabet:       ['A','B','C','D','E','F','G'...]
            ALPHA ROTOR alphabet: ['E','K','M','F','L','G','D'...]
            When letter enters rotor ALPHA (before going through reflector), it is changed with one placed
            on the same index in another list. Letter 'C' will be changed with letter 'M'.
            All above is described when ALPHA setting is one, thus its alphabet is not shifted.

            It is important to keep in mind the direction the letter is inserted into the rotor.
            When the letter has passed the reflector and goes once again through ALPHA rotor it is
            changed with another one, in an opposite way. 'K' will be changed with 'B'.
            '''

            # get next letter by replacing it by rotor alphabet's letter on certain index
            next_letter = self._shift(self._rotor_alphabet('alpha'), self._alpha)[self._alphabet.index(letter)]
            next_letter = self._shift(self._rotor_alphabet('beta'), self._beta)[self._alphabet.index(next_letter)]
            next_letter = self._shift(self._rotor_alphabet('gamma'), self._gamma)[self._alphabet.index(next_letter)]

            next_letter = self._reflector_alphabet()[self._alphabet.index(next_letter)]

            next_letter = self._alphabet[self._shift(self._rotor_alphabet('gamma'),self._gamma).index(next_letter)]
            next_letter = self._alphabet[self._shift(self._rotor_alphabet('beta'),self._beta).index(next_letter)]
            next_letter = self._alphabet[self._shift(self._rotor_alphabet('alpha'),self._alpha).index(next_letter)]

            # Once again conjuncted letters are replaced with each other
            if self._steckerbrett:
                next_letter = self._steckerbrett_change_letters(next_letter)

            # append encripted letter to ciphered_text
            ciphered_text.append(next_letter)

        # return message created by combining every letter from the list
        return("".join(ciphered_text))
