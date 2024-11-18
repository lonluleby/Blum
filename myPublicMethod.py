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



earnClaim_path = "Earn/earn_Claim.png"

earnStart_path = "Earn/earn_Start.png"


def click_Claim(screen_region):
    while True:
        result = foundProgram.locate_image_on_screen(earnClaim_path,0.9,3)
        if result:
            clickPosition.click_at_position(result)
            staticCheck(screen_region)
        else:
            break

def click_Start():
    while True:
        result = foundProgram.locate_image_on_screen(earnStart_path,0.9,3)
        if result:
            clickPosition.click_at_position(result)
            time.sleep(8)
            closeBrowser.colse_Browser()
        else:
            break

def is_existence(*earnClaim_paths):
    # 遍历所有路径
    for path in earnClaim_paths:
        result = foundProgram.locate_image_on_screen(path, 0.9, 3)
        if result:
            # 如果某个路径找到图像，返回 True
            return True
    # 如果所有路径都没有找到图像，返回 None
    return None




def take_screenshot(region):
    screenshot = pyautogui.screenshot(region=region)
    return screenshot

# 计算两张图片的差异
def image_diff(img1, img2):
    # 将PIL图片转换为NumPy数组
    img1_np = np.array(img1)
    img2_np = np.array(img2)

    # 计算差异
    diff = np.abs(img1_np - img2_np)
    diff_sum = np.sum(diff)

    # 返回差异总和
    return diff_sum



# 滚动并检查图像变化
def staticCheck(screen_region):
    # 截取初始屏幕
    prev_screenshot = take_screenshot(screen_region)
    while True:
        # 截取0.5s后的屏幕
        time.sleep(0.5)
        curr_screenshot = take_screenshot(screen_region)

        # 计算图像差异
        diff = image_diff(prev_screenshot, curr_screenshot)

        print(f"图像差异: {diff}")

        # 如果差异非常小，说明页面没有发生显著变化，可能是到底了
        if diff < 100:  # 设定一个合理的差异阈值，根据实际情况调整
            break
        # 更新上一次截图
        prev_screenshot = curr_screenshot

# # 示例用法
# if __name__ == "__main__":
#     scroll_until_bottom()