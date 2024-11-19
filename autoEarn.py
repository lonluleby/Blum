import pyautogui
import time
import os
import clickPosition
import foundProgram
from pynput.mouse import Controller
import blumGameBoot
import moveToLeft
import closeBrowser
import moveTegram
import earnAcadmy

earnEarn_path = "Earn/earn_Earn.png"
earnWeekly_path = "Earn/earn_Weekly.png"
earnNew_path = "Earn/earn_New.png"
earnAcademy_path= "Earn/earn_Academy.png"



def main():
    result = foundProgram.locate_image_on_screen(earnEarn_path, 0.9)
    if result:
        clickPosition.click_at_position(result)
        print(f"找到任务")
    else:
        print("没找到任务")
    time.sleep(2)

    result = foundProgram.locate_image_on_screen(earnWeekly_path, 0.9)
    if result:
        clickPosition.move_at_position(result)
        pyautogui.scroll(-600)
    time.sleep(2)

    result = foundProgram.locate_image_on_screen(earnNew_path, 0.9)
    if result:
        clickPosition.move_at_position(result)
        pyautogui.scroll(-100)
    time.sleep(2)

    #做Academy任务
    result = foundProgram.locate_image_on_screen(earnAcademy_path, 0.9)
    if result:
        clickPosition.click_at_position(result)
        # 获取当前鼠标位置
        current_x, current_y = pyautogui.position()
        # 将鼠标向下移动100个像素
        pyautogui.moveTo(current_x, current_y + 100)
        pyautogui.scroll(-250)
    time.sleep(2)

    earnAcadmy.toDo()





# 示例用法
if __name__ == "__main__":
    main()