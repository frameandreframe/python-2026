# 测试文件名必须以test开头
import pytest
# 注意: 直接导入包名， 不要带 src
from python_type.five_essentials import calculate_discount

def test_calculate_discount_normal():
    """测试正常情况的折扣计算"""
    # 100 块的商品打 20% 的折扣，应该得到 80 块
    assert calculate_discount(100, 20) == 80.0


def test_calculate_discount_zero_percent():
    """测试折扣为 0% 的情况"""
    assert calculate_discount(100, 0) == 100.0


def test_calculate_discount_float_price():
    """测试价格为浮点数的情况"""
    assert calculate_discount(99.9, 10) == pytest.approx(89.91, rel=1e-2) # 使用近似比较，允许小的浮点误差

def test_calculate_discount_full():
    """测试折扣为 100% 的情况"""
    assert calculate_discount(100, 100) == 0.0

