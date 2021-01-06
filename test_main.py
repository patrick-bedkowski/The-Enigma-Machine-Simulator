from main import format_to_dict, enigma_interface
import pytest
from exceptions import (
    SteckerbrettWrongFormat,
    InvalidRotorValues,
    NoReflectorSelected
)
# this module is neccessary to test function with inputs
from io import StringIO

'''def test_correct_rotors_setting():
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

def test_format_dict():
    steckenbrett_str = 'AB,CD,EF'
    assert format_to_dict(steckenbrett_str)['A'] == 'B'

def test_format_dict_wrong_format_1():
    steckenbrett_str = 'AB, CD,EF'
    with pytest.raises(SteckerbrettWrongFormat):
        format_to_dict(steckenbrett_str)

def test_format_dict_wrong_format_2():
    steckenbrett_str = 'AB,C ,EF'
    with pytest.raises(SteckerbrettWrongFormat):
        format_to_dict(steckenbrett_str)

def test_format_dict_wrong_format_3():
    steckenbrett_str = 'AB,CDE,FG'
    with pytest.raises(SteckerbrettWrongFormat):
        format_to_dict(steckenbrett_str)

'''Tests of Manually inserting rotors value'''
def test_insert_proper_rotors_values():
    enigma = enigma_interface()
    rotors ='1,4,5'
    assert enigma.create_list_of_rotors(rotors) == ['1', '4', '5']

def test_insert_empty_value_of_rotors():
    enigma = enigma_interface()
    rotors = ''
    with pytest.raises(InvalidRotorValues):
        enigma.create_list_of_rotors(rotors)

def test_insert_too_many_values_of_rotors():
    enigma = enigma_interface()
    rotors = '1,2,3,4'
    with pytest.raises(InvalidRotorValues):
        enigma.create_list_of_rotors(rotors)

def test_insert_not_enough_values_of_rotors():
    enigma = enigma_interface()
    rotors = '1,2'
    with pytest.raises(InvalidRotorValues):
        enigma.create_list_of_rotors(rotors)

def test_reflector_value_empty():
    enigma = enigma_interface()
    reflector = ''
    with pytest.raises(NoReflectorSelected):
        enigma.check_if_reflector_has_value(reflector)
