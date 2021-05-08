from file_management import (
    save_txt_file,
    read_txt_file,
    save_json_file,
    read_json_file
)
from exceptions import (
    FileNotFound,
    UndefinedFileName,
    WrongFileName,
    DecodeError
)
import pytest
# this module is neccessary to test function with inputs
from io import StringIO

'''
TXT import tests
'''

def test_read_txt_file_not_found():
    path = 'text2021.txt'
    with pytest.raises(FileNotFound):
        read_txt_file(path)

def test_read_txt_file_not_found_no_extension():
    path = 'text2021.'
    with pytest.raises(FileNotFound):
        read_txt_file(path)

def test_read_txt_file_not_found_extension_missing():
    path = 'text2021'
    with pytest.raises(FileNotFound):
        read_txt_file(path)

'''
TXT export tests
'''

def test_save_txt_file_incorrect_name(monkeypatch):
    wrong_file_name = 'text_'
    # Monkey patch input() function
    monkeypatch.setattr('sys.stdin', StringIO(wrong_file_name))
    with pytest.raises(WrongFileName):
        save_txt_file('text')

def test_save_txt_file_incorrect_name_comma(monkeypatch):
    wrong_file_name = 'text,'
    monkeypatch.setattr('sys.stdin', StringIO(wrong_file_name))
    with pytest.raises(WrongFileName):
        save_txt_file('text')

def test_save_txt_file_incorrect_name_without_extension(monkeypatch):
    wrong_file_name = 'text.'
    monkeypatch.setattr('sys.stdin', StringIO(wrong_file_name))
    with pytest.raises(WrongFileName):
        save_txt_file('text')

def test_save_txt_file_empty_name(monkeypatch):
    name_of_the_file = '\n'
    monkeypatch.setattr('sys.stdin', StringIO(name_of_the_file))
    with pytest.raises(UndefinedFileName):
        save_txt_file(name_of_the_file)

'''
JSON import tests
'''

def test_save_json_file_incorrect_name(monkeypatch):
    wrong_file_name = 'text_'
    # Monkey patch input() function
    monkeypatch.setattr('sys.stdin', StringIO(wrong_file_name))
    with pytest.raises(WrongFileName):
        save_json_file('text')

def test_save_json_file_incorrect_name_comma(monkeypatch):
    wrong_file_name = 'text,'
    monkeypatch.setattr('sys.stdin', StringIO(wrong_file_name))
    with pytest.raises(WrongFileName):
        save_json_file('text')

def test_save_json_file_incorrect_name_without_extension(monkeypatch):
    wrong_file_name = 'text.'
    monkeypatch.setattr('sys.stdin', StringIO(wrong_file_name))
    with pytest.raises(WrongFileName):
        save_json_file('text')

def test_save_json_file_empty_name(monkeypatch):
    name_of_the_file = '\n'
    monkeypatch.setattr('sys.stdin', StringIO(name_of_the_file))
    with pytest.raises(UndefinedFileName):
        save_json_file(name_of_the_file)

'''READ JSON FILE TESTS'''

def test_read_json_file_not_found():
    path = 'settings2021.json'
    with pytest.raises(FileNotFound):
        read_json_file(path)

def test_read_json_file_extension_missing():
    path = 'settings.'
    with pytest.raises(FileNotFound):
        read_json_file(path)

def test_read_json_file_wrong_format():
    '''TXT file imported to read as json'''
    path = 'processedText.txt'
    with pytest.raises(DecodeError):
        read_json_file(path)
