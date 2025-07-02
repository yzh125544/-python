import pytest
from um import count

def test_basic_cases():
    """測試基本情況"""
    assert count("hello, um, world") == 1
    assert count("yummy") == 0
    assert count("Um, um, UM!") == 3

def test_case_insensitive():
    """測試大小寫不敏感"""
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("uM") == 1

def test_word_boundaries():
    """測試單詞邊界"""
    assert count("umbrella") == 0
    assert count("yummy") == 0
    assert count("sum") == 0
    assert count("album") == 0
    assert count("forum") == 0
    assert count("medium") == 0

def test_multiple_occurrences():
    """測試多次出現"""
    assert count("um um um") == 3
    assert count("Um, um, and um again") == 3
    assert count("Well, um, I think, um, that's um correct") == 3

def test_punctuation():
    """測試標點符號情況"""
    assert count("um!") == 1
    assert count("um?") == 1
    assert count("um.") == 1
    assert count("um,") == 1
    assert count("(um)") == 1
    assert count("'um'") == 1
    assert count("\"um\"") == 1

def test_empty_and_edge_cases():
    """測試空字符串和邊界情況"""
    assert count("") == 0
    assert count("   ") == 0
    assert count("um") == 1
    assert count(" um ") == 1
    assert count("um um") == 2
