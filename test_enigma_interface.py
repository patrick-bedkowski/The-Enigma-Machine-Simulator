from enigma_interface import Enigma_interface
from enigma_class import Enigma
import pytest
from exceptions import (
    SteckerbrettWrongFormat,
    InvalidRotorValues,
    NoReflectorSelected,
    InvalidRotorQuantity,
    SteckerbrettRepeatedValues
)
# this module is neccessary to test function with inputs
from io import StringIO


'''FORMAT Steckerbrett to dictionary'''


def test_format_dict():
    enigma_if = Enigma_interface(Enigma)
    steckenbrett_str = 'AB,CD,EF'
    assert enigma_if.format_to_dict(steckenbrett_str)['A'] == 'B'

def test_format_dict_wrong_format_space():
    enigma_if = Enigma_interface(Enigma)
    steckenbrett_str = 'AB, CD,EF'
    with pytest.raises(SteckerbrettWrongFormat):
        enigma_if.format_to_dict(steckenbrett_str)

def test_format_dict_wrong_format_space_one_value():
    enigma_if = Enigma_interface(Enigma)
    steckenbrett_str = 'AB,C ,EF'
    with pytest.raises(SteckerbrettWrongFormat):
        enigma_if.format_to_dict(steckenbrett_str)

def test_format_dict_wrong_format_too_many_values():
    enigma_if = Enigma_interface(Enigma)
    steckenbrett_str = 'AB,CDE,FG'
    with pytest.raises(SteckerbrettWrongFormat):
        enigma_if.format_to_dict(steckenbrett_str)

def test_format_dict_repeated_key_in_another_key():
    enigma_if = Enigma_interface(Enigma)
    steckenbrett_str = 'AB,AC'
    with pytest.raises(SteckerbrettRepeatedValues):
        enigma_if.format_to_dict(steckenbrett_str)

'''REFLECTOR'''

# two upcoming tests, show the use of StringIO module to monkeypatch inputs

def test_reflector_correct_value(monkeypatch):
    enigma_if = Enigma_interface(Enigma)
    # Monkey patch input() function
    monkeypatch.setattr('sys.stdin', StringIO('A'))
    assert enigma_if.insert_reflector_value() == 'A'

def test_reflector_incorrect_value(monkeypatch):
    '''
    Even though program does not raise an error when inserted reflector option
    is not defined in the project, it is correct. The purpose of insert_reflector_value
    method, is to catch an empty value.
    This wrong inserted value of reflector will be later catched in enigma_class part.
    '''
    enigma_if = Enigma_interface(Enigma)
    # Monkey patch input() function
    monkeypatch.setattr('sys.stdin', StringIO('D'))
    assert enigma_if.insert_reflector_value() == 'D'

def test_reflector_empty():
    enigma_if = Enigma_interface(Enigma)
    # Monkey patch input() function
    reflector = ''
    with pytest.raises(NoReflectorSelected):
        enigma_if.check_if_reflector_inserted(reflector)

'''ROTOR INSERTS'''


def test_insert_rotors_correct_values():
    enigma_if = Enigma_interface(Enigma)
    rotors = '1,2,3'
    assert enigma_if.create_list_of_rotors(rotors) == [1, 2, 3]

def test_insert_rotors_space():
    enigma_if = Enigma_interface(Enigma)
    rotors = '1, 2,3'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_space_empty():
    enigma_if = Enigma_interface(Enigma)
    rotors = '1, ,2'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_empty():
    enigma_if = Enigma_interface(Enigma)
    rotors = '1,,2'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_empty_last():
    enigma_if = Enigma_interface(Enigma)
    rotors = '1,2,'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_empty_first():
    enigma_if = Enigma_interface(Enigma)
    rotors = ',1,2'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_empty_borders():
    enigma_if = Enigma_interface(Enigma)
    rotors = ',1,'
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_empty_value_of_rotors():
    enigma_if = Enigma_interface(Enigma)
    rotors = ''
    with pytest.raises(InvalidRotorQuantity):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_incorrect_quantity_space():
    enigma_if = Enigma_interface(Enigma)
    rotors = '1,2 '
    with pytest.raises(InvalidRotorValues):
        enigma_if.create_list_of_rotors(rotors)

def test_insert_rotors_zero_before_value():
    enigma_if = Enigma_interface(Enigma)
    rotors = '1,2,01'
    '''This works, because python when converting string value "01"
    to intiger, detects that zero is present in front of integer and ignores it'''
    assert enigma_if.create_list_of_rotors(rotors) == [1, 2, 1]
