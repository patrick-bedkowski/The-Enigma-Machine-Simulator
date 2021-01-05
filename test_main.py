'''from main import check_if_rotors_values_are_correct
import pytest

def test_correct_rotors_setting():
    rotors = '20,9,10'
    list_of_rotors = rotors.split(',')
    assert check_if_rotors_values_are_correct(list_of_rotors) is True


def test_too_many_rotor_settings():
    with pytest.raises(ValueError):
        rotors = '20,9,1,20'
        check_if_rotors_values_are_correct(rotors)


def test_not_enough_rotor_settings():
    with pytest.raises(ValueError):
        rotors = '20,9'
        check_if_rotors_values_are_correct(rotors)
'''