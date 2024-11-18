import pyautogui
import time
import os
import clickPosition
import foundProgram
from pynput.mouse import Controller
import blumGameBoot
import moveToLeft
import moveTegram

blumProgramImage_path = "Blum/blum.png"  # 替换为你自己的图像路径
blumLaunch_path="Blum/blum_launch.png"
blumService_path="Blum/blum_Service.png"
blumContinue_path="Blum/blum_Continue.png"
blumClaim_path="Blum/blum_Claim.png"
blumStartFarming_path="Blum/blum_StartFarming.png"
blumHomepath="Blum/blum_Home.png"
blum3Point_path="Blum/blum_3Point.png"
blumReload_path="Blum/blum_Reload.png"
blumPlay_path = "Blum/blum_Play.png"
blumBack_path = "Blum/blum_Back.png"
blumBlum_path = "Blum/blum_Blum.png"
blumFarming_path = "Blum/blum_Farming.png"

def main():
    result = foundProgram.locate_image_on_screen(blumProgramImage_path)
    if result:
        clickPosition.click_at_position(result)
        print(f"找到blum小程序")
    else:
        print("没找到blum小程序")
    time.sleep(2)
    result =foundProgram.locate_image_on_screen(blumLaunch_path)
    if result:
        clickPosition.click_at_position(result)
        print(f"找到blum小程序登录按钮")
    else:
        print("没找到blum小程序登录按钮")
    time.sleep(3)
    result =foundProgram.locate_image_on_screen(blumService_path)
    if result:
        clickPosition.click_at_position(result)
        print(f"找到blum服务确认按钮")
    else:
        print("没找到blum服务确认按钮")
    time.sleep(15)
    result =foundProgram.locate_image_on_screen(blumBlum_path)
    if result:
        clickPosition.click_at_position(result)
        print(f"找到blum服务确认按钮")
    else:
        print("没找到blum服务确认按钮")
    moveToLeft.move_window_to_position(0,0)
    moveTegram.move_window_to_position(1000,0)

    while True:
        # 查找B
        result = foundProgram.locate_image_on_screen(blumHomepath)

        if result:
            break  # 找到后退出循环
        else:
            # 如果没有找到
            result = foundProgram.locate_image_on_screen(blumContinue_path)
            if result:
                clickPosition.click_at_position(result)
                break
            else:
                result = foundProgram.locate_image_on_screen(blum3Point_path)
                clickPosition.click_at_position(result)
                result = foundProgram.locate_image_on_screen(blumReload_path)
                clickPosition.click_at_position(result)
                print("重新打开小程序")
                time.sleep(15)  # 暂停 1 秒，避免过于频繁地调用，减少系统资源消耗
    time.sleep(3)
    result =foundProgram.locate_image_on_screen(blumContinue_path)
    if result:
        clickPosition.click_at_position(result)
        print(f"找到blum每日奖励确认按钮")
    else:
        print("没找到blum每日奖励确认按钮")
    time.sleep(3)
    result =foundProgram.locate_image_on_screen(blumClaim_path)
    if result:
        clickPosition.click_at_position(result)
        print(f"找到blum收获按钮")
    else:
        print("没找到blum收获确认按钮")
    time.sleep(3)
    result =foundProgram.locate_image_on_screen(blumStartFarming_path)
    if result:
        clickPosition.click_at_position(result)
        print(f"找到blum开始按钮")
    else:
        print("没找到blum开始按钮")
    time.sleep(3)
    # 获取当前鼠标位置
    result =foundProgram.locate_image_on_screen(blumFarming_path)
    if result:
        clickPosition.click_at_position(result)
    else:
        print("已开始Farm")

    x, y = pyautogui.position() #获取当前位置

    # 将鼠标向上移动 200 像素
    while True:
        pyautogui.moveTo(x, y - 300, duration=0.5)
        pyautogui.scroll(-200)
        time.sleep(1)
        result =foundProgram.locate_image_on_screen(blumPlay_path,0.8,3)
        if result:
            print(f"有票，开始玩游戏")
            clickPosition.click_at_position(result)
            time.sleep(1)
            blumGameBoot.main()
            result = foundProgram.locate_image_on_screen(blumBack_path)
            clickPosition.click_at_position(result)
            time.sleep(1)
        else:
            print("没票了")
            break




# 示例用法
if __name__ == "__main__":
    main()
