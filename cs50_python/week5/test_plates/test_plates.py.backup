import pytest
from plates import is_valid

def test_valid_plates():
    """測試有效的車牌號碼"""
    assert is_valid("CS50") == True
    assert is_valid("CS5") == True
    assert is_valid("AB12") == True
    assert is_valid("HELLO") == True
    assert is_valid("AA") == True

def test_invalid_length():
    """測試無效的長度"""
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("") == False

def test_invalid_start_characters():
    """測試無效的開頭字符 - 加強版"""
    # 第一個字符不是字母
    assert is_valid("1A") == False
    assert is_valid("1AB") == False
    assert is_valid("1ABC") == False
    assert is_valid("2CS50") == False
    assert is_valid("3HELLO") == False

    # 第二個字符不是字母
    assert is_valid("A1") == False
    assert is_valid("A1BC") == False
    assert is_valid("A2345") == False
    assert is_valid("C1S50") == False
    assert is_valid("H1LLO") == False

    # 兩個字符都不是字母
    assert is_valid("12") == False
    assert is_valid("123") == False
    assert is_valid("1234") == False

def test_invalid_numbers():
    """測試無效的數字使用"""
    assert is_valid("CS05") == False
    assert is_valid("CS5A") == False
    assert is_valid("CS50P") == False
    assert is_valid("AB0123") == False
    assert is_valid("AA1B2") == False

def test_non_alphanumeric():
    """測試非字母數字字符"""
    assert is_valid("CS@50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS-50") == False
    assert is_valid("A!") == False

def test_zero_placement():
    """測試數字 0 的位置規則"""
    assert is_valid("CS05") == False
    assert is_valid("AB01") == False
    assert is_valid("AA0") == False
    assert is_valid("BB012") == False

def test_number_placement():
    """測試數字位置規則"""
    assert is_valid("CS5A") == False
    assert is_valid("AB1C2") == False
    assert is_valid("AA1B") == False
    assert is_valid("BB12C") == False

