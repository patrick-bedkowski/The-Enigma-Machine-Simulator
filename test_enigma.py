from enigma import Enigma, format_to_dict
from exceptions import SteckerbrettTypeError

def test_normal_values():
    alpha = 5
    beta = 17
    gama = 24
    steckerbrett = "ab,cd"
    enigma = Enigma(alpha, beta, gama, steckerbrett)
    assert enigma.alpha() == 5
    assert enigma.beta() == 17
    assert enigma.gama() == 24
    assert format_to_dict(enigma.steckerbrett()) == {'a': 'b', 'c': 'd'}

'''def test_format_to_dict():
    steckerbrett = "ab, cd"
    format_to_dict(steckerbrett)'''