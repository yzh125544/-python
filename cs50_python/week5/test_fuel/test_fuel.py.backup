import pytest
from fuel import convert, gauge


def test_convert_valid_fractions():
    """測試有效的分數轉換"""
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("99/100") == 99
    assert convert("1/4") == 25
    assert convert("1/3") == 33  # 33.33... 四捨五入為 33


def test_convert_invalid_format():
    """測試無效格式拋出 ValueError"""
    with pytest.raises(ValueError):
        convert("a/b")  # 非數字
    with pytest.raises(ValueError):
        convert("3/a")  # Y 不是數字
    with pytest.raises(ValueError):
        convert("a/3")  # X 不是數字
    with pytest.raises(ValueError):
        convert("1-2")  # 沒有斜線
    with pytest.raises(ValueError):
        convert("1/2/3")  # 多個斜線


def test_convert_invalid_values():
    """測試無效數值拋出異常"""
    with pytest.raises(ValueError):
        convert("5/3")  # X > Y
    with pytest.raises(ValueError):
        convert("10/5")  # X > Y
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # 除以零
    with pytest.raises(ZeroDivisionError):
        convert("5/0")  # 除以零


def test_gauge_empty():
    """測試空油箱情況"""
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    """測試滿油箱情況"""
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_normal():
    """測試正常百分比顯示"""
    assert gauge(2) == "2%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(98) == "98%"


def test_convert_edge_cases():
    """測試邊界情況"""
    assert convert("1/100") == 1  # 最小顯示為 E
    assert convert("99/100") == 99  # 最大顯示為 F
    assert convert("2/100") == 2  # 剛好超過 E 閾值
    assert convert("98/100") == 98  # 剛好低於 F 閾值
