import pyautogui
import time
import os

# 等待用户准备屏幕
print("请确保“251”文件夹在屏幕上可见，程序将在5秒后开始搜索。")
time.sleep(5)

# 使用绝对路径
folder_image = "2511.png"  # 替换为文件夹图像的绝对路径
exe_image = "app.png"  # 替换为 a.exe 图像的绝对路径

# 检查图像文件是否存在
if not os.path.exists(folder_image):
    print("文件夹图像文件不存在，请检查路径。")
else:
    print("开始查找文件夹...")

    # 查找“251”文件夹在屏幕上的位置
    folder_position = pyautogui.locateOnScreen(folder_image)

    if folder_position:
        left, top, width, height = folder_position
        print(f"文件夹坐标: 左={left}, 上={top}, 宽={width}, 高={height}")

        # 执行双击进入文件夹
        # pyautogui.doubleClick(x=left + width // 2, y=top + height // 2)
        pyautogui.moveTo(left, top, duration=1)  # duration参数表示移动所需的时间（秒）
        pyautogui.doubleClick()

        print("已双击文件夹。")

        # 等待文件夹加载
        time.sleep(2)

        # 查找 a.exe 文件的坐标
        if os.path.exists(exe_image):
            print("开始查找 Telegram.exe...")
            exe_position = pyautogui.locateOnScreen(exe_image)

            if exe_position:
                exe_left, exe_top, exe_width, exe_height = exe_position
                print(f"a.exe 坐标: 左={exe_left}, 上={exe_top}, 宽={exe_width}, 高={exe_height}")
                pyautogui.moveTo(exe_left, exe_top, duration=1)  # duration参数表示移动所需的时间（秒）
                pyautogui.doubleClick()
            else:
                print("未找到名为 Telegram.exe 的文件。")
        else:
            print("Telegram.exe 图像文件不存在，请检查路径。")
    else:
        print("未找到名为“251”的文件夹。")
