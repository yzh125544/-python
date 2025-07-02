import random

def get_positive_integer(prompt):
    """取得正整數輸入的輔助函數"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                continue
        except ValueError:
            continue

# 主程式
def main():
    # 取得遊戲級別
    level = get_positive_integer("Level: ")

    # 生成隨機數字
    secret_number = random.randint(1, level)

    # 開始猜數字遊戲
    while True:
        guess = get_positive_integer("Guess: ")

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
