import pyfiglet
import sys
import random

# 創建 Figlet 物件
figlet = pyfiglet.Figlet()

# 檢查命令行參數
if len(sys.argv) == 1:
    # 零個參數：隨機字體
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)

elif len(sys.argv) == 3:
    # 兩個參數：檢查格式
    if sys.argv[1] in ["-f", "--font"]:
        font_name = sys.argv[2]
        # 檢查字體是否存在
        if font_name in figlet.getFonts():
            figlet.setFont(font=font_name)
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)

else:
    # 其他數量的參數都是錯誤的
    print("Invalid usage")
    sys.exit(1)

# 提示用戶輸入文本
text = input("Input: ")

# 輸出 ASCII 藝術文字
print("Output:")
print(figlet.renderText(text))
