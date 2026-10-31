import pytest

from python_type.worth_knowing import get_user, first


def test_get_user_with_valid():
    assert get_user(42) is None


# 基础行为
def test_first_returns_first_int():
    assert first([1, 2, 3]) == 1


def test_first_returns_single_element():
    assert first([42]) == 42

def test_first_returns_element_itself():
    obj = {"k": "v"}
    items = [obj, {"other": 1}]
    assert first(items) is obj # 同一性断言


if __name__ == "__main__":
    pytest.main([__file__, "-v"])