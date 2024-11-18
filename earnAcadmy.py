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
import myPublicMethod

screen_region = (0, 0, 760, 1300)

earnKeyword_path = "Earn/earn_Keyword.png"
earnVerify_path = "Earn/earn_Verify.png"
earnClaim_path = "Earn/earn_Claim.png"
earnStart_path = "Earn/earn_Start.png"
earnVerify2_path = "Earn/earn_Verify2.png"

image_verify_path = "earnVerify"



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

    myPublicMethod.click_Start()

    myPublicMethod.staticCheck(screen_region)

    for image_path in image_verify_paths:
        # 加载图片
        result = foundProgram.locate_image_on_screen(image_path, 0.99,1)
        if result:
            keyword = os.path.splitext(os.path.basename(image_path))[0]
            clickPosition.click_at_position_offset(result, 300, 0)
            time.sleep(3)
            write_keyword(keyword)

        else:
            print("当前界面无未输入keywords的任务")

    myPublicMethod.staticCheck(screen_region)


# 滚动并检查图像变化
def toDo():
    # 截取初始屏幕

    while True:

        #遍历文件，判断当前界面是否存在未做完的任务
        find_images_in_screen(image_verify_path)
        #将所有已做完任务Claim
        myPublicMethod.click_Claim(screen_region)

        if myPublicMethod.is_existence(earnStart_path,earnVerify2_path,earnClaim_path):
            result = foundProgram.locate_image_on_screen(earnStart_path, 0.9, 3)

        else:
            break



if __name__ == "__main__":
    time.sleep(2)
    toDo()