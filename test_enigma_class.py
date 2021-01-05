from enigma_class import Enigma

def test_normal_insert():
    alpha = 5
    beta = 17
    gama = 24
    steckerbrett = {'A': 'B', 'C': 'D'}
    reflector = 'A'
    enigma = Enigma(alpha, beta, gama, steckerbrett, reflector)
    assert enigma.alpha() == 5
    assert enigma.beta() == 17
    assert enigma.gama() == 24
    assert enigma.reflector() == 'A'
    assert enigma.steckerbrett() == {'A': 'B', 'C': 'D'}


def test_check_default_values():
    enigma = Enigma()
    assert enigma.alpha() == 1
    assert enigma.beta() == 1
    assert enigma.gama() == 1
    assert enigma.reflector() == 'A'
    assert enigma.steckerbrett() == {}


def test_group_rotors():
    alpha = 5
    beta = 17
    gama = 24
    enigma = Enigma(alpha, beta, gama)
    assert enigma.group_rotors() == [5, 17, 24]


def test_initial_settings():
    alpha = 5
    beta = 17
    gama = 24
    steckerbrett = {'A': 'B', 'C': 'D'}
    reflector = 'A'
    enigma = Enigma(alpha, beta, gama, steckerbrett, reflector)
    assert enigma.initial_settings() == {
        "rotors": [5, 17, 24],
        'steckenbrett': {'A': 'B', 'C': 'D'},
        'reflector': 'A'
    }

def test_alphabet():
    enigma = Enigma()
    assert enigma._alphabet == [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

def test_initaite_reflector_A():
    enigma = Enigma(reflector = 'A')
    assert enigma._reflector_alphabet == [
        'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'
    ]

def test_initaite_reflector_B():
    enigma = Enigma(reflector = 'B')
    assert enigma._reflector_alphabet == [
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B'
    ]

def test_initaite_reflector_C():
    enigma = Enigma(reflector = 'C')
    assert enigma._reflector_alphabet == [
        'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G'
    ]

def test_reflector_C_with_indexes():
    enigma = Enigma(reflector = 'A')
    assert enigma.reflect_letter(0) == 'V'
    assert enigma.reflect_letter(1) == 'W'
    assert enigma.reflect_letter(2) == 'X'

def test_reflector_C_with_indexes():
    enigma = Enigma(reflector = 'B')
    assert enigma.reflect_letter(0) == 'C'
    assert enigma.reflect_letter(1) == 'D'
    assert enigma.reflect_letter(2) == 'E'

def test_reflector_C_with_indexes():
    enigma = Enigma(reflector = 'C')
    assert enigma.reflect_letter(0) == 'H'
    assert enigma.reflect_letter(1) == 'I'
    assert enigma.reflect_letter(2) == 'J'

def test_turn_rotors():
    alpha = 1
    beta = 1
    gama = 1
    enigma = Enigma(alpha, beta, gama)
    enigma.turn_rotors()
    assert enigma.alpha() == 2
    assert enigma.beta() == 1
    assert enigma.gama() == 1 

def test_turn_rotors_border_value_A():
    alpha = 26
    beta = 1
    gama = 1
    enigma = Enigma(alpha, beta, gama)
    enigma.turn_rotors()
    assert enigma.alpha() == 1
    assert enigma.beta() == 2
    assert enigma.gama() == 1

def test_turn_rotors_border_value_B():
    alpha = 1
    beta = 26
    gama = 1
    enigma = Enigma(alpha, beta, gama)
    enigma.turn_rotors()
    assert enigma.alpha() == 2
    assert enigma.beta() == 26
    assert enigma.gama() == 1

def test_turn_rotors_border_value_A_and_B():
    alpha = 26
    beta = 26
    gama = 1
    enigma = Enigma(alpha, beta, gama)
    enigma.turn_rotors()
    assert enigma.alpha() == 1
    assert enigma.beta() == 1
    assert enigma.gama() == 2
    
def test_turn_rotors_border_value_all_rotors():
    alpha = 26
    beta = 26
    gama = 26
    enigma = Enigma(alpha, beta, gama)
    enigma.turn_rotors()
    assert enigma.alpha() == 1
    assert enigma.beta() == 1
    assert enigma.gama() == 1

def test_steckerbrett_change_letters():
    enigma = Enigma(steckerbrett = {'A': 'B', 'C': 'D'})
    assert enigma.steckerbrett_change_letters('A') == 'B'
    assert enigma.steckerbrett_change_letters('D') == 'C'
    assert enigma.steckerbrett_change_letters('E') == 'E'

def test_encrypt_message():
    alpha = 5
    beta = 17
    gama = 24
    steckerbrett = {'O': 'Z', 'B': 'D'}
    reflector = 'A'
    text = 'BACKTOSCHOOL'
    enigma = Enigma(alpha, beta, gama, steckerbrett, reflector)

    assert enigma.encryptingCodec(text) == 'CHHDUQORZYAQ'

def test_decrypt_message():
    alpha = 5
    beta = 17
    gama = 24
    steckerbrett = {'O': 'Z', 'B': 'D'}
    reflector = 'A'
    text = 'CHHDUQORZYAQ'
    enigma = Enigma(alpha, beta, gama, steckerbrett, reflector)

    assert enigma.encryptingCodec(text) == 'BACKTOSCHOOL'
