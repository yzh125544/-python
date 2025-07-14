# test_project.py
import pytest
from project import preprocess_text, get_top_words, calculate_lexical_diversity

def test_preprocess_text():
    """Tests the text preprocessing function."""
    assert preprocess_text("  hello \n\n\n world  \r\n ") == "hello\n\nworld"
    assert preprocess_text("test. \n another test.") == "test. another test."
    assert preprocess_text("\t  \n\n  final \n test  ") == "final\n\ntest"

def test_get_top_words():
    """Tests the word frequency statistics function."""
    text = "apple banana apple orange banana apple"
    stop_words = {'orange'}
    # Expected result: apple 3 times, banana 2 times
    expected = [('apple', 3), ('banana', 2)]
    assert get_top_words(text, stop_words, 2) == expected
    # Test with an empty string
    assert get_top_words("", stop_words) == []

def test_calculate_lexical_diversity():
    """Tests the lexical diversity calculation function."""
    words1 = ["a", "b", "c", "a", "b"] # 5 words, 3 unique
    assert calculate_lexical_diversity(words1) == 0.6
    words2 = ["go", "go", "go"] # 3 words, 1 unique
    assert calculate_lexical_diversity(words2) == pytest.approx(1/3)
    # Test with an empty list
    assert calculate_lexical_diversity([]) == 0.0
