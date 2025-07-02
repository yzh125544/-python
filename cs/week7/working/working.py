import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r'^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$'
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Input does not match required format")

    h1, m1, mer1, h2, m2, mer2 = match.groups()

    h1, m1 = int(h1), int(m1) if m1 else 0
    h2, m2 = int(h2), int(m2) if m2 else 0

    if not (1 <= h1 <= 12) or not (0 <= m1 < 60):
        raise ValueError("Invalid start time")
    if not (1 <= h2 <= 12) or not (0 <= m2 < 60):
        raise ValueError("Invalid end time")

    def to_24_hour(h, m, mer):
        if mer == 'AM':
            if h == 12:
                h = 0
        else:
            if h != 12:
                h += 12
        return h, m

    h1_24, m1_24 = to_24_hour(h1, m1, mer1)
    h2_24, m2_24 = to_24_hour(h2, m2, mer2)

    # 關鍵修正：確保小時和分鐘都格式化為兩位數
    return f"{h1_24:02}:{m1_24:02} to {h2_24:02}:{m2_24:02}"

if __name__ == "__main__":
    main()

