import pygetwindow as gw
import pyautogui

def move_window_to_position(x,y):
    """
    将指定标题的窗口移动到目标位置
    """
    # 获取匹配窗口标题的窗口对象
    windows = gw.getWindowsWithTitle("TelegramDesktop")

    if windows:
        window = windows[0]
        # 移动窗口到指定的位置
        window.restore()  # 恢复窗口（如果是最小化状态）
        window.activate()  # 激活窗口
        window.moveTo(x, y)

    else:
        print("未找到小程序窗口")

