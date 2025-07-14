import sys
import os
from PIL import Image, ImageOps

def main():
    # 檢查命令行參數數量
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments" if len(sys.argv) < 3 else "Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # 檢查檔案副檔名
    valid_extensions = ['.jpg', '.jpeg', '.png']
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    # 驗證副檔名是否有效
    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid input")

    # 驗證輸入和輸出檔案副檔名是否相同
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    # 檢查輸入檔案是否存在並處理圖片
    try:
        # 開啟輸入圖片
        photo = Image.open(input_file)

        # 開啟T恤圖片
        shirt = Image.open("shirt.png")

        # 調整並裁剪輸入圖片以匹配T恤尺寸
        photo = ImageOps.fit(photo, shirt.size)

        # 將T恤覆蓋在照片上
        photo.paste(shirt, shirt)

        # 儲存結果
        photo.save(output_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
