import pytest
from python_type.three_funcs import get_names, get_scores, get_numbers

def test_get_name():
    assert get_names() == ["Alice", "Bob"]

def test_get_scores():
    assert get_scores() == {"Alice": 90, "Bob": 85}

def test_get_numbers():
    assert get_numbers() == [1, 2, 3]