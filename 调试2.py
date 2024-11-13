import pyautogui
import time
import os
import clickPosition
import foundBlumProgram

blumProgramImage_path = "Blum/blum.png"  # 替换为你自己的图像路径


def main():
    result = foundBlumProgram.locate_image_on_screen(blumProgramImage_path)
    if result:
        clickPosition.click_at_position(result)
        print(f"找到blum小程序")
    else:
        print("没找到blum小程序。")


# 示例用法
if __name__ == "__main__":
    main()
