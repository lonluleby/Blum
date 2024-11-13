import pyautogui

def click_at_position(position):
    """
    模拟点击图像的中心位置
    :param position: 图像的坐标信息 (left, top, width, height)
    """
    if position:
        # 计算图像的中心点
        left, top, width, height = position
        x, y = pyautogui.center((left, top, width, height))  # 获取图像中心坐标
        print(f"点击坐标: ({x}, {y})")
        pyautogui.moveTo(x, y,duration=0.5)  # 移动鼠标到 (x, y) 位置
        pyautogui.click()  # 在当前位置点击
        print("点击操作已完成")
    else:
        print("无效的位置，无法进行点击操作")

