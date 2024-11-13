import tkinter as tk
from tkinter import messagebox
import pyautogui
from PIL import ImageGrab

class ScreenshotTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # 隐藏主窗口
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.screenshot = None
        self.rect_id = None
        self.canvas = None

    def get_screen_resolution(self):
        # 获取屏幕分辨率
        screen_width, screen_height = pyautogui.size()
        return screen_width, screen_height

    def start_capture(self):
        # 创建一个透明的窗口用于截图
        screen_width, screen_height = self.get_screen_resolution()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.attributes("-transparentcolor", "white")
        self.root.attributes("-topmost", True)  # 设置窗口为最上层

        self.canvas = tk.Canvas(self.root, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.root.deiconify()  # 显示窗口
        self.root.mainloop()

    def on_press(self, event):
        # 记录鼠标按下时的位置
        self.start_x = event.x
        self.start_y = event.y
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red", width=2)

    def on_drag(self, event):
        # 更新矩形的大小
        self.end_x = event.x
        self.end_y = event.y
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_release(self, event):
        # 截取矩形区域的截图并返回坐标
        self.end_x = event.x
        self.end_y = event.y
        self.root.quit()  # 退出Tkinter循环

        # 截图区域
        left, top = min(self.start_x, self.end_x), min(self.start_y, self.end_y)
        right, bottom = max(self.start_x, self.end_x), max(self.start_y, self.end_y)
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))  # 截取指定区域

        # 返回截图区域的屏幕坐标和分辨率
        print(f"LEFT, TOP, RIGHT, BOTTOM = {left}, {top}, {right}, {bottom}")
        screenshot.show()  # 展示截图
        print(f"截图区域分辨率: 宽度 = {right - left}, 高度 = {bottom - top}")

if __name__ == "__main__":
    tool = ScreenshotTool()
    tool.start_capture()
