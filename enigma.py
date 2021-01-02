from exceptions import (
    IncorrectReflector,
)
from string import ascii_uppercase
#from file_management import read_txt_file, read_steckerbrett_file

class Enigma:

    # NAPRAW Reflector

    # CZY mogę przyjąć założenie, że użytkownik nie przygotuje sam pliki z błędnymi ustawieniami?
    # WHEN YOU IMPORT SETTINGS TO ENIGMA, PROGRAM ASSUMES THAT YOU WANT TO READ CIPHERED TEXT,
    # so there's no need to save this settings again to external file, because you already have
    # settings file for that encryption

    # write new tests
    # CHECK IF KEY IS NOT IN VALUE AND VICE VERSA

    def __init__(self, alpha = 0, beta = 0, gama = 0, steckerbrett = {}, reflector = 'A'):
        '''
        Class Enigma. Contains attributes:

        :param alpha: initial alpha setting of the rotor
        :type alphat: int
        :default alpha: 0

        :param beta: initial beta setting of the rotor
        :type beta: int
        :default beta: 0

        :param gama: initial gama setting of the rotor
        :type gama: int
        :default gama: 0

        :param steckerbrett: Steckerbrett shows which letters should replace each other
        :type steckerbrett: dict
        :default steckerbrett: {}

        :param reflector: initial reflector setting of the rotor
        :type reflector: str
        :default reflector: 'A'
        '''

        '''
        ascii_uppercase is a string holding "abcdefgh..."
        Atribute is holding list consisting of ascii_uppercase values
        '''
        self._alphabet = [letter for letter in ascii_uppercase]

        #set
        self._alpha = alpha
        self._beta = beta
        self._gama = gama
        self._steckerbrett = steckerbrett

        if reflector in ['A', 'B', 'C']:
            self._reflector = reflector
        else:
            raise IncorrectReflector('The value for the reflector is incorrect')



    def initial_settings(self):
        '''
        This method saves initial settings of the machine, before values (like each rotor)
        are changed due to the iteration.
        It returns dictionary with keys as name, and values as a value of the setting.
        '''
        # Creating dictionary to store initial settings
        enigma_settings = {}
        enigma_settings['rotors'] = self.group_rotors()
        enigma_settings['steckenbrett'] = self._steckerbrett
        enigma_settings['reflector'] = self._reflector

        return enigma_settings


    '''
    SET GET: alpha, beta, gama
    chyba nie są potrzebne, skoro nigdzie w programie
    się do nich nie odwołuje
    '''
    def alpha(self):
        return self._alpha

    def beta(self):
        return self._beta

    def gama(self):
        return self._gama

    def steckerbrett(self):
        return self._steckerbrett

    def reflector(self):
        return self._reflector

    def reflector_values(self, reflector, index):
        '''
        Reflector holds reversed alphabet
        Function Returns alphabet shifted by my setting #!change it
        '''
        '''
        There will be 3 different reflectors to choose from
        '''
        def shift(seq, n):
            return seq[n:] + seq[:n]

        if reflector == "A":
            reflector = self._alphabet[::-1]
        # to nie działa
        if reflector == "B":
            reflector = shift(self._alphabet, 2)
        if reflector == "C":
            reflector = shift(self._alphabet, 3)
        return reflector[index]

    def group_rotors(self):
        '''
        Returns list grouped values of each rotor.
        First index indicates the rotor which is the first to receive code.
        '''
        return [self._alpha, self._beta, self._gama]

    """def remove_interspace(self, text):
        '''
        This method allows to use interspace in cyphered text.
        It removes the interspace from the text, at the same time remembering
        the index of it
        index_of_interspace is an attribute so it can be acessible later
        '''
        new_text = ''
        self._index_of_interspace = []
        index = 0
        for letter in text:
            if letter != " ":
                index += 1
                new_text += letter
            else:
                index += 1
                self._index_of_interspace.append(index-1)
        return new_text"""

    # chyba to nie jest potrzebne do algorytmu
    def Remove_steckerbrett_connections_from_alphabet(self):
        '''
        Letters that are connected in steckerbrett need to be removed
        from alphabet, since they will not be used to assign them to rottor

        '''
        for letter in list(self._steckerbrett.keys()):
            if letter in self._alphabet:
                self._alphabet.remove(letter)
                self._alphabet.remove(self._steckerbrett[letter])
                # from now on, the steckerbrett will be interchangeable - tuple
                self._steckerbrett.update({self._steckerbrett[letter]: letter})

    """def get_rotor_setting(self):
        '''
        This method is not necessary, since it is implemented in the __init__ that rotor value must be 0 <= rotor <= 26
        TO MODIFY LATER: automatically assing each of the rotor new value, not manually at the end
        '''
        for rotor in self._rotors:
            if rotor != 0:
                index = self._rotors.index(rotor)
                rotor = rotor % 26  # rotor makes turn after 26 letters
                self._rotors[index] = rotor  # replace element on the same index

        self.set_new_alpha(self._rotors[0])
        self.set_new_beta(self._rotors[1])
        self.set_new_gama(self._rotors[2])"""

    '''
    Heart of an algorythm.
    '''
    def permutation(self, rotor):
        #'''format alphabet'''
        #formated_alphabet = list(''.join(self._alphabet))
        '''Shifts the alphabet to the right by the value of a rotor with slicing'''
        shifted_alphabet = self._alphabet[-rotor:] + self._alphabet[:-rotor]
        #shifted_alphabet = formated_alphabet[-rotor:] + formated_alphabet[:-rotor]
        return shifted_alphabet

    def inverse_permutation(self, rotor):
        #'''Shifts the alphabet to the left by the value of a rotor'''
        #formated_alphabet = list(''.join(self._alphabet))
        '''Used with slicing'''
        shifted_alphabet = self._alphabet[rotor:] + self._alphabet[:rotor]
        return shifted_alphabet

    def turn_rotors(self):
        '''Turn the rotors'''
        self._alpha += 1
        if self._alpha % 26 == 0:
            self._alpha = 0
            self._beta += 1
        if self._beta % 26 == 0 and self._alpha % 26 == 0:
            self._beta = 1
            self._gama += 1

    def encrypt(self, ciphered_text):
        '''

        '''
        encrypted_text = []
        for letter in ciphered_text:
            '''
            If letter is in steckerbrett, switch it for the coressponding one
            '''
            # if steckerbrett holds values
            if self._steckerbrett:
                #enigma.Remove_steckerbrett_connections_from_alphabet()

                for key, value in self._steckerbrett.items():
                    if key == letter:
                        letter = key
                    elif value == letter:
                        letter = value
                '''if letter in self._steckerbrett.values():
                    letter = self._steckerbrett[letter]
                elif letter in self._steckerbrett.keys():
                    letter = next(k for k, v in self._steckerbrett.items() if v == letter)'''
            else:
                continue

            '''Encrypt by the rotors'''
            self.turn_rotors()
            next_letter = self.permutation(self._alpha)[self._alphabet.index(letter)]
            next_letter = self.permutation(self._beta)[self._alphabet.index(next_letter)]
            next_letter = self.permutation(self._gama)[self._alphabet.index(next_letter)]

            next_letter = self.reflector_values(self._reflector, self._alphabet.index(next_letter))

            next_letter = self.inverse_permutation(self._gama)[self._alphabet.index(next_letter)]
            next_letter = self.inverse_permutation(self._beta)[self._alphabet.index(next_letter)]
            next_letter = self.inverse_permutation(self._alpha)[self._alphabet.index(next_letter)]

            encrypted_text.append(next_letter)
        """
        Add the interspaces
        if self._index_of_interspace:  # if not empty
            for index in range(0, len(self._index_of_interspace)):
                encrypted_text.insert(self._index_of_interspace[index], " ")"""

        '''Return Result'''
        return("".join(encrypted_text))

"""def shift_letter(alphabet):
    #shifting letters to to the left by k times
    alphabet.reverse()
    return alphabet

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(' '.join(alphabet))
print(' '.join(shift_letter(alphabet)))"""
