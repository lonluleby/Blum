import pyautogui
import numpy as np
from PIL import Image

def find_color_in_range_and_move(min_rgb, max_rgb):
    # 获取当前屏幕截图
    screenshot = pyautogui.screenshot()

    # 将截图转换为NumPy数组
    img_array = np.array(screenshot)

    # 分别提取RGB通道
    r = img_array[:,:,0]  # 红色通道
    g = img_array[:,:,1]  # 绿色通道
    b = img_array[:,:,2]  # 蓝色通道

    # 找到在颜色范围内的所有像素
    mask = (
        (r >= min_rgb[0]) & (r <= max_rgb[0]) &
        (g >= min_rgb[1]) & (g <= max_rgb[1]) &
        (b >= min_rgb[2]) & (b <= max_rgb[2])
    )

    # 获取满足条件的像素的坐标
    matches = np.where(mask)

    # 如果找到了符合条件的像素
    if len(matches[0]) > 0:
        # 选择第一个匹配的像素坐标
        y, x = matches[0][0], matches[1][0]

        # 移动鼠标到该位置
        pyautogui.moveTo(x, y)
        print(f"Found color in range at ({x}, {y}) and moved the mouse.")
    else:
        print("No color found in the specified range.")

# 设置颜色范围
min_rgb = (98, 159, 212)  # RGB最小值
max_rgb = (102, 164, 215)  # RGB最大值

# 调用函数
find_color_in_range_and_move(min_rgb, max_rgb)
