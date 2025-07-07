import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # 使用正則表達式匹配獨立的 "um"，忽略大小寫
    pattern = r"\bum\b"
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
