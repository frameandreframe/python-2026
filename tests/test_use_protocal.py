import pytest
from python_type.use_protocol import SupportsLen, report_size

def test_report_size_with_list():
    """测试 report_size 函数传入列表"""
    my_list = [1, 2, 3]
    assert report_size(my_list) == "size = 3"


def test_report_size_with_string():
    """测试 report_size 函数传入字符串"""
    my_string = "hello"
    assert report_size(my_string) == "size = 5"


def test_report_size_with_custom_class():
    """测试 report_size 函数传入自定义类 MyBox"""
    class MyBox:
        def __len__(self) -> int:
            return 42

    my_box = MyBox()
    assert report_size(my_box) == "size = 42"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
