import pytest
from working import convert

def test_valid_formats():
    """測試有效的輸入格式"""
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

def test_invalid_formats():
    """測試無效的輸入格式"""
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00 PM")  # 缺少空格
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")  # 錯誤的分隔符
    with pytest.raises(ValueError):
        convert("09 AM to 5:001 PM")  # 無效格式
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")  # 24小時制格式
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")  # 錯誤分隔符
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")  # 無效分隔符

def test_edge_cases():
    """測試邊界情況和特殊時間"""
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"  # 夜班
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"  # 夜班帶分鐘
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_invalid_times():
    """測試無效的時間值"""
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")  # 無效分鐘
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # 無效小時
    with pytest.raises(ValueError):
        convert("0:00 AM to 5:00 PM")  # 12小時制中沒有0點
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")  # 無效小時

def test_format_requirements():
    """測試格式要求：確保輸出為兩位數格式"""
    result = convert("1 AM to 2 PM")
    assert result == "01:00 to 14:00"  # 小時應為兩位數

    result = convert("12:05 AM to 1:30 PM")
    assert result == "00:05 to 13:30"  # 確保分鐘格式正確
