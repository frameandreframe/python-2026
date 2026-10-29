# 存放跨测试共享的 fixture

import pytest

def sample_fixture():
    """一个示例 fixture, 可以在多个测试中使用"""
    return 100.0