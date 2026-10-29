import pytest
from python_type.union_syntax import parse, parse_before

def test_parse_with_int() -> int:
    """测试 parse 函数传入整数"""
    assert parse(42) == 42

def test_parse_with_str() -> int:
    """测试 parse 函数传入字符串"""
    assert parse("123") == 123

def test_parse_with_invalid_str() -> None:
    """测试 parse 函数传入无法转换的字符串"""
    assert parse("abc1") == None