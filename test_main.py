from main import enigma_interface
from enigma_class import Enigma
import pytest
from exceptions import (
    SteckerbrettWrongFormat,
    InvalidRotorValues,
    NoReflectorSelected,
    InvalidRotorQuantity,
    ReflectorValueIsUndefined
)
# this module is neccessary to test function with inputs
from io import StringIO

def test_format_dict():
    enigma_if = enigma_interface(Enigma)
    steckenbrett_str = 'AB,CD,EF'
    assert enigma_if.format_to_dict(steckenbrett_str)['A'] == 'B'

def test_format_dict_wrong_format_1():
    enigma_if = enigma_interface(Enigma)
    steckenbrett_str = 'AB, CD,EF'
    with pytest.raises(SteckerbrettWrongFormat):
        enigma_if.format_to_dict(steckenbrett_str)

def test_format_dict_wrong_format_2():
    enigma_if = enigma_interface(Enigma)
    steckenbrett_str = 'AB,C ,EF'
    with pytest.raises(SteckerbrettWrongFormat):
        enigma_if.format_to_dict(steckenbrett_str)

def test_format_dict_wrong_format_3():
    enigma_if = enigma_interface(Enigma)
    steckenbrett_str = 'AB,CDE,FG'
    with pytest.raises(SteckerbrettWrongFormat):
        enigma_if.format_to_dict(steckenbrett_str)

'''Tests of Manually inserting rotors value'''
def test_insert_proper_rotors_values():
    enigma_if = enigma_interface(Enigma)
    rotors ='1,4,5'
    assert enigma_if.create_list_of_rotors(rotors) == ['1', '4', '5']

def test_insert_empty_value_of_rotors():
    enigma_if = enigma_interface(Enigma)
    rotors = ''
    with pytest.raises(InvalidRotorQuantity):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_too_many_values_of_rotors():
    enigma_if = enigma_interface(Enigma)
    rotors = '1,2,3,4'
    with pytest.raises(InvalidRotorQuantity):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_not_enough_values_of_rotors():
    enigma_if = enigma_interface(Enigma)
    rotors = '1,2'
    with pytest.raises(InvalidRotorQuantity):
        enigma_if.create_list_of_rotors(rotors)

# two upcoming tests, show the use of StringIO module to monkeypatch inputs

def test_reflector_correct_value(monkeypatch):
    enigma_if = enigma_interface(Enigma)
    # Monkey patch input() function
    monkeypatch.setattr('sys.stdin', StringIO('A'))
    assert enigma_if.insert_reflector_value() == 'A'

def test_reflector_incorrect_value(monkeypatch):
    '''
    Even though program does not raise an error when inserted reflector option
    is not defined in the project, it is correct. The purpose of insert_reflector_value,
    is to catch empty value.
    This wrong inseret value of reflector will be later catched in enigma_class part.
    '''
    enigma_if = enigma_interface(Enigma)
    # Monkey patch input() function
    monkeypatch.setattr('sys.stdin', StringIO('D'))
    assert enigma_if.insert_reflector_value() == 'D'

def test_reflector_empty():
    enigma_if = enigma_interface(Enigma)
    # Monkey patch input() function
    reflector = ''
    with pytest.raises(NoReflectorSelected):
        enigma_if.check_if_reflector_inserted(reflector)


'''ROTOR INSERTS'''

def test_insert_rotors_correct_values():
    enigma_if = enigma_interface(Enigma)
    rotors = '1,2,3'
    assert enigma_if.create_list_of_rotors(rotors) == ['1', '2', '3']

def test_sample():
    strin = '1,,2'
    lista = strin.split(',')
    assert ',,' in strin

def test_insert_rotors_space():
    enigma_if = enigma_interface(Enigma)
    rotors = '1, 2,3'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_space_empty():
    enigma_if = enigma_interface(Enigma)
    rotors = '1, ,2'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_empty():
    enigma_if = enigma_interface(Enigma)
    rotors = '1,,2'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_empty_last():
    enigma_if = enigma_interface(Enigma)
    rotors = '1,2,'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_empty_first():
    enigma_if = enigma_interface(Enigma)
    rotors = ',1,2'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_empty_borders():
    enigma_if = enigma_interface(Enigma)
    rotors = ',1,'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_incorrect_quantity():
    enigma_if = enigma_interface(Enigma)
    rotors = '1,2'
    with pytest.raises(InvalidRotorQuantity):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_incorrect_quantity_space():
    enigma_if = enigma_interface(Enigma)
    rotors = '1,2 '
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)