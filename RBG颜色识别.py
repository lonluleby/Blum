import pyautogui
import numpy as np
from PIL import ImageGrab
import time


# 设定目标颜色的 RGB 范围
def is_color_in_range(pixel, min_rgb, max_rgb):
    """
    检查一个像素的颜色是否在指定的RGB范围内。
    :param pixel: (r, g, b) 元组表示的像素颜色
    :param min_rgb: (r_min, g_min, b_min) 颜色范围的最小值
    :param max_rgb: (r_max, g_max, b_max) 颜色范围的最大值
    :return: True 表示颜色在范围内，False 表示不在范围内
    """
    return np.all(pixel >= min_rgb) and np.all(pixel <= max_rgb)


# 获取屏幕截图
def get_screen_image():
    screenshot = ImageGrab.grab()  # 获取屏幕截图
    return np.array(screenshot)  # 转为NumPy数组以便操作


# 在屏幕上搜索目标颜色范围
def find_color_in_screen(min_rgb, max_rgb):
    screen = get_screen_image()  # 获取屏幕截图
    height, width, _ = screen.shape

    for y in range(height):
        for x in range(width):
            pixel = screen[y, x]  # 获取当前像素的颜色值
            if is_color_in_range(pixel, min_rgb, max_rgb):
                return x, y  # 返回找到的第一个符合条件的像素坐标
    return None  # 如果没有找到符合条件的像素，则返回None


# 模拟鼠标移动到指定坐标
def move_mouse_to_color(min_rgb, max_rgb):
    color_coord = find_color_in_screen(min_rgb, max_rgb)

    if color_coord is not None:
        x, y = color_coord
        print(f"Found color at position: ({x}, {y})")
        pyautogui.moveTo(x, y, duration=1)  # 移动鼠标到该坐标位置，duration为移动时间
    else:
        print("Color not found on screen")


# 主程序
if __name__ == "__main__":

    start_time1 = time.time()

    while time.time() - start_time1 < 10:
        # 设置颜色范围
        min_rgb = np.array([128, 220, 0])  # 最小RGB值（例如：暗红色）
        max_rgb = np.array([223, 255, 116])  # 最大RGB值（例如：浅红色）

        print("Searching for the color on screen...")
        move_mouse_to_color(min_rgb, max_rgb)
