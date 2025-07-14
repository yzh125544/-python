from jar import Jar
import pytest

def test_init():
    # 測試有效容量
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    # 測試預設容量
    jar_default = Jar()
    assert jar_default.capacity == 12
    assert jar_default.size == 0

    # 測試無效容量
    with pytest.raises(ValueError):
        Jar(-1)  # 負數容量
    with pytest.raises(ValueError):
        Jar(3.5)  # 非整數容量
    with pytest.raises(ValueError):
        Jar("ten")  # 字串容量

def test_str():
    jar = Jar()
    assert str(jar) == ""  # 空罐子
    jar.deposit(1)
    assert str(jar) == "🍪"  # 一塊餅乾
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"  # 12塊餅乾

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(2)
    assert jar.size == 5

    # 測試超過容量的情況
    with pytest.raises(ValueError):
        jar.deposit(1)  # 會超過容量

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    # 測試取出數量超過現有餅乾的情況
    with pytest.raises(ValueError):
        jar.withdraw(3)  # 只剩2塊但要取3塊

    jar.withdraw(2)
    assert jar.size == 0

def test_capacity_property():
    """測試容量屬性"""
    jar = Jar(20)
    assert jar.capacity == 20
    # 確保容量是唯讀的
    assert hasattr(Jar.capacity, 'fget')

def test_size_property():
    """測試大小屬性"""
    jar = Jar()
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3
