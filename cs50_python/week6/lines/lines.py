import sys

def main():
    # 檢查是否提供了正確數量的命令行參數
    if len(sys.argv) != 2:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 2 else "Too many command-line arguments")

    filename = sys.argv[1]

    # 檢查檔案是否以 .py 結尾
    if not filename.endswith('.py'):
        sys.exit("Not a Python file")

    # 嘗試開啟並讀取檔案
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    # 計算代碼行數
    loc = 0
    for line in lines:
        # 去除空白字符來檢查是否為空行或註釋
        stripped_line = line.strip()

        # 跳過空行（只包含空白字符的行）
        if not stripped_line:
            continue

        # 跳過註釋（以 # 開頭的行，可選地前面有空白字符）
        if stripped_line.startswith('#'):
            continue

        # 這是一行代碼
        loc += 1

    print(loc)

if __name__ == "__main__":
    main()
