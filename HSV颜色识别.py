import time
import pyautogui
import numpy as np
import cv2
from PIL import ImageGrab

print("请确保游戏在屏幕上可见，程序将在5秒后开始搜索。")
time.sleep(5)
# 设置游戏窗口的参数（假设已知游戏窗口位置和大小）
game_window = (0, 0, 1000, 1200)  # (left, top, right, bottom)，你可以根据实际情况调整

# 目标颜色范围 (HSV) — 假设我们要点击的物体是红色
# 红色的HSV范围示例

lower_color = np.array([30,57,136])
upper_color = np.array([50,181,255])

# 模拟游戏点击的频率（每秒检查）
click_delay = 1  # 每0.1秒检查一次



def get_game_screen():
    """
    截取游戏窗口的屏幕，返回图片
    """
    screen = ImageGrab.grab(bbox=game_window)
    return np.array(screen)


def find_target_objects(screen):
    """
    通过HSV颜色过滤，找到屏幕中符合颜色范围的物体坐标
    """
    # 转换颜色到HSV，方便进行颜色过滤
    hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)

    # 使用inRange来创建颜色范围的掩膜
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # 获取符合条件的坐标
    target_coords = np.column_stack(np.where(mask > 0))  # 获取所有匹配位置的坐标

    target_hsv_values = hsv[target_coords[:, 0], target_coords[:, 1]]
    print(type(target_hsv_values))
    # 如果有符合条件的坐标，返回一个随机坐标
    if target_coords.shape[0] > 0:
        idx = np.random.randint(0, target_coords[0].size)  # 随机选择一个坐标的索引
        return target_coords[0][idx], target_coords[1][idx]  # 返回选中的坐标
    return None


def click_on_target(coords):
    """
    模拟鼠标点击目标位置
    """
    if coords is not None:
        # 点击最上面的物体（假设物体从上到下依次排列）
        y, x = coords  # 获取第一个目标的位置
        pyautogui.moveTo(x, y, duration=0.02)
        # pyautogui.click(x, y)
        # print(f"Clicked on object at ({x}, {y})")


def main():
    """
    主程序循环，不断截取屏幕并模拟点击
    """
    start_time1 = time.time()

    while time.time() - start_time1 < 2:
        # 截取游戏屏幕

        screen = get_game_screen()
        # screenshot = pyautogui.screenshot('screenshot.png')
        # screenshot.show()  # 显示截图

        # 查找符合颜色范围的物体
        target_coords = find_target_objects(screen)
        print(target_coords)
        # 如果找到目标物体，模拟点击
        click_on_target(target_coords)

        # 等待一定时间再继续
        time.sleep(click_delay)



if __name__ == "__main__":
    main()
