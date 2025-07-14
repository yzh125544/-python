import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # 正則表達式匹配四個1-3位數字，用點分隔
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)

    if not match:
        return False

    # 檢查每個部分是否在0-255範圍內
    parts = match.groups()
    for part in parts:
        # 拒絕前導零，除非整個部分就是 '0'
        if len(part) > 1 and part.startswith('0'):
            return False

        if not part.isdigit():
            return False

        num = int(part)
        if num < 0 or num > 255:
            return False

    return True

if __name__ == "__main__":
    main()

