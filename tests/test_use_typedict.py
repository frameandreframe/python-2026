import pytest
from python_type.use_typedict import User, create_user


def test_create_user_normal():
    """测试正常情况的 User 创建"""
    expected = {"id": 1, "name": "Alice", "email": None}
    assert create_user({"id": 1, "name": "Alice", "email": None}) == expected


def test_create_user_missing_email():
    """测试缺少 email 键的情况"""
    with pytest.raises(TypeError, match="email"):
        create_user({"id": 1, "name": "Alice"})  # 缺少 email 键，应该抛出 TypeError


if __name__ == "__main__":
    pytest.main([__file__, "-v"])