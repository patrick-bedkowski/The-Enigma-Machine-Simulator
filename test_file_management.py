'''from file_management import save_txt_file, read_txt_file, format_text
from string import ascii_lowercase
import pytest

def test_read_txt_file():
    input_path = 'ciphered_text.txt'
    ciphered_text = read_txt_file(input_path)
    assert (ciphered_text == 'BACKTOSCHOOl')

def test_is_in_alphabet():
    alphabet = ascii_lowercase
    split = [letter for letter in alphabet]
    assert ('a' in split)

'''