from exceptions import SteckerbrettTypeError
#from file_management import read_txt_file, read_steckerbrett_file

class Enigma:
    def __init__(self, alpha = 0, beta = 0, gama = 0, steckerbrett = {}):
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

        :param steckerbrett: Steckerbrett-shows which letters should replace each other
        :type steckerbrett: dict
        :default steckerbrett: {}
        '''

        #alfabet ascii
        self._alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        #self._ciphered_text = (ciphered_text).upper()  # converts text to upper letters
        self._steckerbrett = steckerbrett
        '''Pytanie czy mogę zrobić
        self._alpha = self.set_new_alpha(alpha)
        Wtedy od razu sprawdzi mi też wyjątki
        '''
        self._alpha = alpha
        self._beta = beta
        self._gama = gama
        self._reflector = self.set_reflector()
        self._rotors = self.set_rotors()
        self._index_of_interspace = []

    '''SET, GET: alpha, beta, gama'''
    '''After setting up new rotor values, program also needs to initaite get_rotor_settings'''
    def alpha(self):
        return self._alpha

    def beta(self):
        return self._beta

    def gama(self):
        return self._gama

    def steckerbrett(self):
        return self._steckerbrett

    def set_new_alpha(self, new_alpha):
        if isinstance(new_alpha, int) is False:
            pass
        if new_alpha < 0 and new_alpha > 27:
            pass  # invalid number
        self._alpha = new_alpha

    def set_new_beta(self, new_beta):
        if isinstance(new_beta, int) is False:
            pass
        if new_beta < 0 and new_beta > 27:
            pass  # invalid number
        self._beta = new_beta

    def set_new_gama(self, new_gama):
        if isinstance(new_gama, int) is False:
            pass
        if new_gama < 0 and new_gama > 27:
            pass  # invalid number
        self._gama = new_gama

    def set_reflector(self):
        '''Reflector holds reversed alphabet'''
        '''There will be 3 different reflectors to choose from'''
        reflector = self._alphabet[::-1]
        return reflector

    def set_rotors(self):
        '''
        Creates a list with rotor values.
        First index indicates the rotor which is the first to receive code
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

    '''Conditions'''
    def steckerbrett_is_dict(self):
        '''
        Steckerbrett must be an dict type. If it is not then raise error
        '''
        if self._steckerbrett:  # if steckerbrett is not empty, check if it has correct type
            if type(self._steckerbrett) is not dict:
                raise SteckerbrettTypeError('Steckerbrett must be a dict type')
            else:
                return True
        else:
            return True

    def steckerbrett_check_for_values(self):
        '''
        Steckerbrett cannot hold two same values.
        We need to check if it is true.
        '''
        repeated_values = []
        for value in self._steckerbrett.values():
            if value in repeated_values:
                # raise SteckerbrettRepeatedValues('Steckerbrett must have different values')
                return False
            else:
                repeated_values.append(value)
        return True

    def steckerbrett_check_for_keys(self):
        '''
        Steckerbrett cannot hold two same keys.
        We need to check if it is true.
        '''
        repeated_keys = []
        for key in self._steckerbrett.keys():
            if key in repeated_keys:
                # raise SteckerbrettRepeatedKeys('Steckerbrett must have different keys')
                return False
            else:
                repeated_keys.append(key)
        return True

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
    Heart of an algorythm. All rotors
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
            if letter in self._steckerbrett:
                '''
                If letter is in steckerbrett, switch it for the coressponding one
                '''
                letter = self._steckerbrett[letter]
            else:
                '''Encrypt by the rotors'''
                self.turn_rotors()
                next_letter = self.permutation(self._alpha)[self._alphabet.index(letter)]
                next_letter = self.permutation(self._beta)[self._alphabet.index(next_letter)]
                next_letter = self.permutation(self._gama)[self._alphabet.index(next_letter)]

                next_letter = self._reflector[self._alphabet.index(next_letter)]

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


#! przenieść do enigma.py
def format_to_dict(list_format):
    '''
    Input contains a list formated like: [letter_a letter_b, letter_c letter_d]
    This function will convert it to dictionary like: {'a': 'b', 'c': 'd'}
    A B, C D
    '''
    new_dict = {}
    index = list_format.split(",")
    for letters in index:
        new_dict.update({letters[0]: letters[1]})
    return new_dict


"""def shift_letter(alphabet):
    #shifting letters to to the left by k times
    alphabet.reverse()
    return alphabet

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(' '.join(alphabet))
print(' '.join(shift_letter(alphabet)))"""
