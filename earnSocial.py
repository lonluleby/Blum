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


# 滚动并检查图像变化
def toDo():
    # 截取初始屏幕

    while True:
        myPublicMethod.click_Start()

        if closeBrowser.close_all_browser_processes("chrom"):
            print("浏览器已关闭")
        else:
            print("浏览器没关")

        myPublicMethod.click_Claim(screen_region)

        if myPublicMethod.is_existence_toSocial(earnClaim_path, earnStart_path):
            print("还有任务没做完")
        else:
            print("任务已经全部做完")
            break



if __name__ == "__main__":

    toDo()