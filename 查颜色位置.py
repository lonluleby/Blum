import pyautogui
import time
from PIL import Image

# 定义RGB的最大值和最小值范围
min_rgb = (128, 220, 0)  # 最小RGB值
max_rgb = (223, 255, 116)  # 最大RGB值

# 定义RGB的最大值和最小值范围
# min_rgb = (83, 157, 217)  # 最小RGB值
#
# max_rgb = (87, 160, 220)  # 最大RGB值

# # 定义RGB的最大值和最小值范围
# min_rgb = (9, 124, 145)  # 最小RGB值
# max_rgb = (27, 126, 147)  # 最大RGB值

# 判断颜色是否在范围内
def is_color_in_range(rgb, min_rgb, max_rgb):
    return all(min_val <= val <= max_val for val, min_val, max_val in zip(rgb, min_rgb, max_rgb))

# 获取屏幕截图
def get_screen_image():
    screenshot = pyautogui.screenshot()
    return screenshot

# 查找屏幕上所有符合条件的区域
def find_matching_areas():
    screenshot = get_screen_image()
    width, height = screenshot.size
    matching_coords = []

    # 遍历屏幕上的每个像素
    for x in range(width):
        for y in range(height):
            pixel_color = screenshot.getpixel((x, y))
            if is_color_in_range(pixel_color, min_rgb, max_rgb):
                matching_coords.append((x, y))  # 如果符合条件，添加坐标到列表

    return matching_coords

# 移动鼠标到所有符合条件的位置，并返回RGB值
def move_mouse_to_all_positions():
    matching_coords = find_matching_areas()  # 获取所有符合条件的坐标
    if not matching_coords:
        print("No matching areas found.")
        return

    # 按顺序移动鼠标到所有匹配的坐标
    for index, (x, y) in enumerate(matching_coords):
        pyautogui.moveTo(x, y)  # 移动鼠标到当前坐标
        screenshot = get_screen_image()  # 获取屏幕截图
        pixel_color = screenshot.getpixel((x, y))  # 获取当前坐标的RGB值
        print(f"Moving mouse to ({x}, {y}) - RGB: {pixel_color} ({index + 1}/{len(matching_coords)})")
        time.sleep(3)  # 每次移动后等待0.5秒，避免过于频繁的操作

    print("All positions visited.")

# 主程序
if __name__ == "__main__":
    move_mouse_to_all_positions()
