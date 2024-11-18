import pyautogui
import numpy as np
from PIL import Image
import time
import threading
import foundProgram
import clickPosition
# 定义常量和配置
# LEFT, TOP, RIGHT, BOTTOM = 0, 0, 450, 800 # 检测区域
LEFT, TOP, RIGHT, BOTTOM =0, 0, 760, 1200  #公司电脑
COLOR1_MIN = np.array([98, 159, 212])  # 冰  公司电脑
COLOR1_MAX = np.array([102, 164, 215])
# COLOR1_MIN = np.array([83, 157, 217])  # 冰
# COLOR1_MAX = np.array([87, 160, 220])
COLOR2_MIN = np.array([167, 236, 89])  # 雪花 公司电脑
COLOR2_MAX = np.array([237, 252, 192])
# COLOR2_MIN = np.array([128, 220, 0])  # 雪花
# COLOR2_MAX = np.array([223, 255, 116])
COLOR3_MIN = np.array([53, 131, 149])  # 冰冻时间 公司电脑
COLOR3_MAX = np.array([64, 133, 156])
# COLOR3_MIN = np.array([9, 124, 145])  # 冰冻时间
# COLOR3_MAX = np.array([27, 126, 147])
CLICK_OFFSETS = [80, 100]  # 点击偏移量

blumRewards_path = "Blum/blum_Rewards.png"


mouse_lock = threading.Lock()

def screenshot_and_find_color():
    """优化后的截图和颜色查找函数"""
    # 使用numpy数组预先分配内存
    screenshot = np.array(pyautogui.screenshot(region=(LEFT, TOP, RIGHT - LEFT, BOTTOM - TOP)))

    # 当前是否为冰冻时间
    mask3 = np.all((COLOR3_MIN <= screenshot) & (screenshot <= COLOR3_MAX), axis=-1)
    if np.any(mask3):
        mask4 = np.all((COLOR2_MIN <= screenshot) & (screenshot <= COLOR2_MAX), axis=-1)
        if np.any(mask4):
            y, x = np.nonzero(mask4)
            random_idx = np.random.randint(len(x))
            abs_x, abs_y = LEFT + x[random_idx], TOP + y[random_idx]
            pyautogui.click(abs_x, abs_y)
            return True
        return False
    # 一次性计算两个颜色掩码
    mask1 = np.all((COLOR1_MIN <= screenshot) & (screenshot <= COLOR1_MAX), axis=-1)
    if np.any(mask1):
        y, x = np.nonzero(mask1)
        random_idx = np.random.randint(len(x))
        abs_x, abs_y = LEFT + x[random_idx], TOP + y[random_idx]

        # 批量执行点击
        for offset in CLICK_OFFSETS:
            pyautogui.click(abs_x, abs_y + offset)
        return True

    mask2 = np.all((COLOR2_MIN <= screenshot) & (screenshot <= COLOR2_MAX), axis=-1)
    if np.any(mask2):
        y, x = np.nonzero(mask2)
        random_idx = np.random.randint(len(x))
        abs_x, abs_y = LEFT + x[random_idx], TOP + y[random_idx]

        # 批量执行点击
        for offset in CLICK_OFFSETS:
            pyautogui.click(abs_x, abs_y + offset)
        return True

    return False


def concurrent_screenshots(stop_event):
    """并发执行截图和查找颜色"""
    while not stop_event.is_set():
        screenshot_and_find_color()

def gameOver(stop_event):
    while True:
        result = foundProgram.locate_image_on_screen(blumRewards_path,0.8,100)
        if result:
            stop_event.set()
            break



def main():
    """主函数，启动两个线程实现并发"""
    # 创建两个线程并启动
    stop_event = threading.Event()

    thread1 = threading.Thread(target=concurrent_screenshots, args=(stop_event,))
    thread2 = threading.Thread(target=concurrent_screenshots, args=(stop_event,))
    thread3 = threading.Thread(target=concurrent_screenshots, args=(stop_event,))
    thread4 = threading.Thread(target=gameOver, args=(stop_event,))
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    # 等待线程执行完成
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

if __name__ == "__main__":
    main()
