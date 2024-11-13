import pyautogui
import numpy as np
from PIL import Image
import time

# 定义区域，左上角和右下角坐标
left, top, right, bottom = 0, 0, 780, 1400  # 示例区域，坐标需根据实际情况调整

# 定义颜色范围，使用RGB格式
color_min = (167, 236, 89)  # RGB最小值
color_max = (237, 252, 192)  # RGB最大值

def screenshot_and_find_color():
    """截取屏幕并寻找符合条件的颜色"""
    # 截取指定区域的屏幕截图
    # a=time.time()
    screenshot = pyautogui.screenshot(region=(left, top, right - left, bottom - top))

    # 转换截图为Numpy数组
    screenshot_np = np.array(screenshot)

    # 创建一个布尔数组，标记符合条件的像素
    mask = np.all((color_min <= screenshot_np) & (screenshot_np <= color_max), axis=-1)

    # 找到符合条件的第一个像素位置
    if np.any(mask):
        # 获取符合条件像素的坐标
        y, x = np.where(mask)
        random_index = np.random.choice(len(x))  # 随机选择一个索引
        abs_x, abs_y = left + x[random_index], top + y[random_index]

        # 移动鼠标到该位置
        # b=time.time()-a
        # print(str(b))
        pyautogui.click(abs_x, abs_y)
        pyautogui.click(abs_x, abs_y + 80)
        pyautogui.click(abs_x, abs_y + 100)
        # pyautogui.moveTo(abs_x, abs_y+100)
        # pyautogui.click()
        # print(f"鼠标移动到位置: ({abs_x}, {abs_y})")
        return True

    print("未找到符合条件的颜色")
    return False


def main():
    """主函数，循环截图并查找符合颜色的区域"""
    start_time=time.time()
    while time.time() - start_time < 30:
        screenshot_and_find_color()



if __name__ == "__main__":
    main()
