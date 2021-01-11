from enigma_class import Enigma
from exceptions import SteckerbrettValueError, ReflectorValueIsUndefined, SteckerbrettRepeatedValues
import pytest

def test_normal_insert():
    alpha = 5
    beta = 17
    gamma = 24
    steckerbrett = {'A': 'B', 'C': 'D'}
    reflector = 'A'
    enigma = Enigma(alpha, beta, gamma, steckerbrett, reflector)
    assert enigma.alpha() == 5
    assert enigma.beta() == 17
    assert enigma.gamma() == 24
    assert enigma.reflector() == 'A'
    assert enigma.steckerbrett() == {'A': 'B', 'C': 'D'}


def test_check_default_values():
    enigma = Enigma()
    assert enigma.alpha() == 1
    assert enigma.beta() == 1
    assert enigma.gamma() == 1
    assert enigma.reflector() == 'A'
    assert enigma.steckerbrett() == {}


def test_group_rotors():
    alpha = 5
    beta = 17
    gamma = 24
    enigma = Enigma(alpha, beta, gamma)
    assert enigma.group_rotors() == [5, 17, 24]


def test_initial_settings():
    alpha = 5
    beta = 17
    gamma = 24
    steckerbrett = {"A": "B", "C": "D"}
    reflector = "A"
    enigma = Enigma(alpha, beta, gamma, steckerbrett, reflector)

    assert enigma.initial_settings == {
        "rotors": [5, 17, 24],
        "steckenbrett": {'A': 'B', 'C': 'D'},
        "reflector": 'A'
    }

'''
TEST Steckerbrett
'''

def test_steckerbrett_check_values_correct():
    steckerbrett_dict = {"A": "B", "C": "D"}
    enigma = Enigma(steckerbrett = steckerbrett_dict)

    assert enigma.steckerbrett_check_values(steckerbrett_dict)

def test_steckerbrett_value_not_in_ascii():
    steckerbrett_dict = {"A": "3", "C": "D"}

    with pytest.raises(SteckerbrettValueError):
        enigma = Enigma(steckerbrett = steckerbrett_dict)

def test_steckerbrett_key_not_in_ascii():
    steckerbrett_dict = {"1": "8", "C": "D"}
    with pytest.raises(SteckerbrettValueError):
        enigma = Enigma(steckerbrett = steckerbrett_dict)

def test_steckerbrett_key_and_value_not_in_ascii():
    steckerbrett_dict = {"1": "8", "C": "D"}
    with pytest.raises(SteckerbrettValueError):
        enigma = Enigma(steckerbrett = steckerbrett_dict)

def test_steckerbrett_key_and_value_have_same_value():
    steckerbrett_dict = {"A": "A", "C": "D"}
    with pytest.raises(SteckerbrettRepeatedValues):
        enigma = Enigma(steckerbrett = steckerbrett_dict)


def test_steckerbrett_key_is_repeated_in_values():
    steckerbrett_dict = {"A": "B", "C": "A"}
    with pytest.raises(SteckerbrettRepeatedValues):
        enigma = Enigma(steckerbrett = steckerbrett_dict)

def test_steckerbrett_value_is_repeated():
    steckerbrett_dict = {"A": "B", "C": "B"}
    with pytest.raises(SteckerbrettRepeatedValues):
        enigma = Enigma(steckerbrett = steckerbrett_dict)

def test_alphabet():
    enigma = Enigma()
    assert enigma._alphabet == [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
'''REFLECTOR'''

def test_reflector_inserted_as_space_value():
    with pytest.raises(ReflectorValueIsUndefined):
        enigma = Enigma(reflector = " ")

def test_initaite_reflector_A():
    enigma = Enigma(reflector = 'A')
    assert enigma.reflector_alphabet() == [
        'E','J','M','Z','A','L','Y','X','V','B','W','F','C',
        'R','Q','U','O','N','T','S','P','I','K','H','G','D'
    ]

def test_initaite_reflector_B():
    enigma = Enigma(reflector = 'B')
    assert enigma.reflector_alphabet() == [
        'Y','R','U','H','Q','S','L','D','P','X','N','G','O',
        'K','M','I','E','B','F','Z','C','W','V','J','A','T'
    ]

def test_initaite_reflector_C():
    enigma = Enigma(reflector = 'C')
    assert enigma.reflector_alphabet() == [
        'F','V','P','J','I','A','O','Y','E','D','R','Z','X',
        'W','G','C','T','K','U','Q','S','B','N','M','H','L'
    ]

def test_reflector_A_with_indexes():
    enigma = Enigma(reflector = 'A')
    assert enigma.reflector_alphabet()[0] == 'E'
    assert enigma.reflector_alphabet()[1] == 'J'
    assert enigma.reflector_alphabet()[2] == 'M'

def test_reflector_B_with_indexes():
    enigma = Enigma(reflector = 'B')
    assert enigma.reflector_alphabet()[0] == 'Y'
    assert enigma.reflector_alphabet()[1] == 'R'
    assert enigma.reflector_alphabet()[2] == 'U'

def test_reflector_C_with_indexes():
    enigma = Enigma(reflector = 'C')
    assert enigma.reflector_alphabet()[0] == 'F'
    assert enigma.reflector_alphabet()[1] == 'V'
    assert enigma.reflector_alphabet()[2] == 'P'

def test_turn_rotors():
    alpha = 1
    beta = 1
    gamma = 1
    enigma = Enigma(alpha, beta, gamma)
    enigma.turn_rotors()
    assert enigma.alpha() == 2
    assert enigma.beta() == 1
    assert enigma.gamma() == 1

def test_turn_rotors_border_value_A():
    alpha = 26
    beta = 1
    gamma = 1
    enigma = Enigma(alpha, beta, gamma)
    enigma.turn_rotors()
    assert enigma.alpha() == 1
    assert enigma.beta() == 2
    assert enigma.gamma() == 1

def test_turn_rotors_border_value_B():
    alpha = 1
    beta = 26
    gamma = 1
    enigma = Enigma(alpha, beta, gamma)
    enigma.turn_rotors()
    assert enigma.alpha() == 2
    assert enigma.beta() == 26
    assert enigma.gamma() == 1

def test_turn_rotors_border_value_A_and_B():
    alpha = 26
    beta = 26
    gamma = 1
    enigma = Enigma(alpha, beta, gamma)
    enigma.turn_rotors()
    assert enigma.alpha() == 1
    assert enigma.beta() == 1
    assert enigma.gamma() == 2

def test_turn_rotors_border_value_all_rotors():
    alpha = 26
    beta = 26
    gamma = 26
    enigma = Enigma(alpha, beta, gamma)
    enigma.turn_rotors()
    assert enigma.alpha() == 1
    assert enigma.beta() == 1
    assert enigma.gamma() == 1

def test_steckerbrett_change_letters():
    enigma = Enigma(steckerbrett = {'A': 'B', 'C': 'D'})
    assert enigma.steckerbrett_change_letters('A') == 'B'
    assert enigma.steckerbrett_change_letters('D') == 'C'
    assert enigma.steckerbrett_change_letters('E') == 'E'

'''SIMPLE ENCRYPTION AND DECRYPTION'''

def test_encrypt_message():
    alpha = 5
    beta = 18
    gamma = 24
    steckerbrett = {'O': 'Z', 'B': 'D', 'W': 'T', 'E': 'L'}
    reflector = 'B'
    text = 'WARSAWUNIVERSITYOFTECHNOLOGY'
    enigma = Enigma(alpha, beta, gamma, steckerbrett, reflector)

    assert enigma.encryptingCodec(text) == 'LLQROUVWFPLXYJFOAGEREQVGMCZQ'

def test_decrypt_message():
    alpha = 5
    beta = 18
    gamma = 24
    steckerbrett = {'O': 'Z', 'B': 'D', 'W': 'T', 'E': 'L'}
    reflector = 'B'
    text = 'LLQROUVWFPLXYJFOAGEREQVGMCZQ'
    enigma = Enigma(alpha, beta, gamma, steckerbrett, reflector)

    assert enigma.encryptingCodec(text) == 'WARSAWUNIVERSITYOFTECHNOLOGY'


