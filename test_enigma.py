from enigma import Enigma
from exceptions import SteckerbrettTypeError
from file_management import format_to_dict

def test_normal_values():
    alpha = 5
    beta = 17
    gama = 24
    steckerbrett = "a b,c d"
    enigma = Enigma(alpha, beta, gama, steckerbrett)
    assert enigma.alpha() == 5
    assert enigma.beta() == 17
    assert enigma.gama() == 24
    assert format_to_dict(enigma.steckerbrett()) == {'a': 'b', 'c': 'd'}

def test_format_to_dict():
    steckerbrett = "a b, c d"
    format_to_dict(steckerbrett)