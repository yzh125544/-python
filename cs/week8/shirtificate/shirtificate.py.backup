from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        """為每頁添加標題"""
        self.set_font('Arial', 'B', 50)
        self.cell(0, 60, 'CS50 Shirtificate', 0, 1, 'C')

def main():
    name = input("Name: ")

    # 創建PDF實例
    pdf = PDF()
    pdf.add_page()

    # 設置自動分頁為關閉，避免內容溢出到第二頁
    pdf.set_auto_page_break(auto=False)

    # 添加T恤圖片（居中）
    try:
        # 嘗試載入實際的T恤圖片
        img_width = 180
        img_height = 180
        x = (210 - img_width) / 2  # A4寬度為210mm，計算居中位置
        y = 70  # 距離頂部70mm
        pdf.image('shirtificate.png', x, y, img_width, img_height)

        # 在T恤上添加用戶姓名（白色文字）
        pdf.set_xy(x, y + 75)  # 定位到T恤中央
        pdf.set_text_color(255, 255, 255)  # 白色文字
        pdf.set_font('Arial', 'B', 24)
        pdf.cell(img_width, 10, f"{name} took CS50!", 0, 1, 'C')

    except FileNotFoundError:
        # 如果圖片文件不存在，使用矩形模擬
        img_width = 180
        img_height = 180
        x = (210 - img_width) / 2
        y = 70

        # 繪製代表T恤的藍色矩形
        pdf.set_fill_color(70, 130, 180)  # 鋼藍色
        pdf.rect(x, y, img_width, img_height, 'F')

        # 在模擬T恤上添加用戶姓名
        pdf.set_xy(x, y + 75)
        pdf.set_text_color(255, 255, 255)  # 白色文字
        pdf.set_font('Arial', 'B', 24)
        pdf.cell(img_width, 10, f"{name} took CS50!", 0, 1, 'C')

    # 輸出PDF文件
    pdf.output('shirtificate.pdf')

if __name__ == "__main__":
    main()
