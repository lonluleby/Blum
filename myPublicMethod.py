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
from PIL import Image, ImageDraw


earnClaim_path = "Earn/earn_Claim.png"

earnStart_path = "Earn/earn_Start.png"
earnEnd_path = "Earn/earn_End.png"

def click_Claim(screen_region,earnClaim_path):
    while True:
        #查找确认按钮
        result = foundProgram.locate_image_on_screen(earnClaim_path,0.9,3)
        #保证按钮状态都是静态的
        staticCheck(screen_region)
        if result:
            while True:
                #是不是存在确认后的按钮（即将消失）
                result2 = foundProgram.locate_image_on_screen(earnEnd_path, 0.99, 3)
                if result2:
                    time.sleep(1)  # 有的话等一会再检测
                else:
                    time.sleep(1)
                    #找到一个确认按钮坐标，直接点击
                    result = foundProgram.locate_image_on_screen(earnClaim_path, 0.9, 3)
                    clickPosition.click_at_position(result)
                    break
        else:
            while True:
                result = foundProgram.locate_image_on_screen(earnEnd_path, 0.99, 3)
                if result:
                    time.sleep(1)
                else:
                    break
            break


def click_Start(earnStart_path):
    last_position = None
    while True:
        result = foundProgram.locate_image_on_screen(earnStart_path, 0.9, 3)
        if result:
            left, top, width, height = result
            x, y = pyautogui.center((left, top, width, height))  # 获取图像中心坐标
            position = (x, y)  # 假设 result 是一个包含位置的元组 (x, y)
            # 如果当前位置与上一次点击的位置不同，则执行点击
            if position != last_position:
                # 更新上一次点击的位置
                last_position = position
                clickPosition.click_at_position(result)
                time.sleep(1)
                moveToLeft.move_window_to_position(0, 0)
        else:
            break


def is_existence_toAcadmy(*earnClaim_paths,temp_image):
    # 遍历所有路径
    for path in earnClaim_paths:
        result = myPublicMethod.locate_image_in_image(temp_image, path, 0.99)
        if result:
            # 如果某个路径找到图像，返回 True
            print("还存在："+str(path))
            return True
    # 如果所有路径都没有找到图像，返回 None
    return None

def is_existence_toSocial(*earnClaim_paths):
    # 遍历所有路径
    for path in earnClaim_paths:
        result = foundProgram.locate_image_on_screen(path, 0.99,3)
        if result:
            # 如果找到图像，返回 True
            print("还存在："+str(path))
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



def remove_area_from_image(image, region):
    """
    在图像上涂白指定区域
    region = (left, top, width, height)
    """
    left, top, width, height = region
    draw = ImageDraw.Draw(image)
    # 使用白色填充区域
    draw.rectangle([left, top, left + width, top + height], fill="white")
    return image

def locate_image_in_image(image1, image2, confidence=0.8, timeout=3):
    """
    在图片1中查找图片2，返回匹配区域的坐标。
    :param image1: 目标图像，作为查找的图片（图片1）
    :param image2: 要查找的图像（图片2）
    :param confidence: 匹配精度，0.0 到 1.0，默认为 0.8
    :param timeout: 查找超时时间（秒），默认为 8 秒
    :return: 返回匹配的坐标（left, top, width, height），如果没有找到返回 None
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            # 使用 locate 方法在 image1 中查找 image2
            position = pyautogui.locate(image2, image1, confidence=confidence)
            if position:
                return position
        except pyautogui.ImageNotFoundException:
            print(f"未找到能做的任务，继续重试...")

        time.sleep(1)  # 每秒检查一次

    print(f"未在 {timeout} 秒内找到图像。")
    return None
