import pyautogui
import time
from PIL import ImageChops
import numpy as np
import os
from glob import glob
import cv2
import foundProgram
import clickPosition
import closeBrowser
import moveToLeft
import myPublicMethod

screen_region = (0, 0, 760, 1300)

earnKeyword_path = "Earn/earn_Keyword.png"
earnVerify_path = "Earn/earn_Verify.png"
earnClaim_path = "Earn/earn_Claim.png"
earnStart_path = "Earn/earn_Start.png"
earnVerify2_path = "Earn/earn_Verify2.png"
earnEnd_path = "Earn/earn_End.png"
image_verify_path = "earnVerify"
earnOutStart_path = "Earn/earn_OutStart.png"


def write_keyword(keyword):
    result = foundProgram.locate_image_on_screen(earnKeyword_path, 0.99)
    if result:
        clickPosition.click_at_position(result)
        pyautogui.write(keyword)
        time.sleep(3)
        result = foundProgram.locate_image_on_screen(earnVerify_path, 0.99)
        if result:
            clickPosition.click_at_position(result)
        time.sleep(1)


def find_images_in_screen(image_verify_path):
    # 获取文件夹中的所有图片文件
    image_verify_paths = glob(os.path.join(image_verify_path, '*.*'))

    #排除干扰项
    result = foundProgram.locate_image_on_screen(earnOutStart_path, 0.99)
    # 获取第一次匹配的区域
    left, top, width, height = result
    i=0
    if result:
        while True:

            # 获取整个屏幕的截图
            screenshot = pyautogui.screenshot()
            # 将第一次匹配的区域涂白
            modified_screenshot = myPublicMethod.remove_area_from_image(screenshot, (left, top, width, height))
            # 保存修改后的截图用于调试
            modified_screenshot.save(str(i)+"modified_screenshot.png")
            # 将修改后的图片保存到临时文件并作为新的图像进行第二次匹配
            modified_screenshot.save("temp_image.png")
            i=i+1
            # 第二次匹配：使用涂白后的图片
            result = myPublicMethod.locate_image_in_image("temp_image.png",earnStart_path, 0.99)
            if result:
                print("9999")
                clickPosition.click_at_position(result)
                moveToLeft.move_window_to_position(0,0)
                myPublicMethod.staticCheck(screen_region)
            else:
                break
    else:
        time.sleep(1)
        print("8888")
        myPublicMethod.click_Start()

    myPublicMethod.staticCheck(screen_region)

    if closeBrowser.close_all_browser_processes("chrom"):
        print("浏览器已关闭")
    else:
        print("浏览器没关")


    for image_path in image_verify_paths:
        result = foundProgram.locate_image_on_screen(earnVerify2_path, 0.99, 3)
        if result:
            # 加载图片
            result = foundProgram.locate_image_on_screen(image_path, 0.99,1)
            if result:
                keyword = os.path.splitext(os.path.basename(image_path))[0]
                clickPosition.click_at_position_offset(result, 300, 0)
                time.sleep(3)
                write_keyword(keyword)

            else:
                print("当前界面无未输入keywords的任务")
        else:
            break

    myPublicMethod.staticCheck(screen_region)


# 滚动并检查图像变化
def toDo():
    # 截取初始屏幕

    while True:

        #遍历文件，判断当前界面是否存在未做完的任务
        find_images_in_screen(image_verify_path)
        #将所有已做完任务Claim
        myPublicMethod.click_Claim(screen_region)

        while True:
            result = foundProgram.locate_image_on_screen(earnEnd_path, 0.99, 3)
            if result:
                time.sleep(1)
            else:
                break

        # 排除干扰项
        result = foundProgram.locate_image_on_screen(earnOutStart_path, 0.99)
        if result:
            # 获取第一次匹配的区域
            left, top, width, height = result
            # 获取整个屏幕的截图
            screenshot = pyautogui.screenshot()
            # 将第一次匹配的区域涂白
            modified_screenshot = myPublicMethod.remove_area_from_image(screenshot, (left, top, width, height))
            # 保存修改后的截图用于调试
            modified_screenshot.save("modified_screenshot.png")
            # 将修改后的图片保存到临时文件并作为新的图像进行第二次匹配
            modified_screenshot.save("temp_image.png")
            # 第二次匹配：使用涂白后的图片
            if myPublicMethod.is_existence(earnVerify2_path, earnClaim_path,earnStart_path, temp_image="temp_image.png"):
                print("还有任务没做完")
            else:
                print("任务已经全部做完")
                break




if __name__ == "__main__":

    toDo()