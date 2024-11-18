import pyautogui
import time
import os
import clickPosition
import closeBrowser
from PIL import Image, ImageDraw

earnOutStart_path = "Earn/earn_OutStart.png"
earnStart_path = "Earn/earn_Start.png"


# 查找屏幕上的图像并返回位置
def locate_image_on_screen(image_path, confidence=0.8, timeout=8, region=None):
    # 检查图像文件是否存在
    if not os.path.exists(image_path):
        print(f"图像文件 {image_path} 不存在，请确保该图像文件在程序运行的目录中。")
        return None

    start_time = time.time()

    # 重试机制：超时后停止查找
    while time.time() - start_time < timeout:
        try:
            # 如果提供了region参数，限制搜索区域
            position = pyautogui.locateOnScreen(image_path, confidence=confidence, region=region)
            if position:
                # 返回图像区域的坐标 (left, top, width, height)
                return position
        except pyautogui.ImageNotFoundException:
            print(f"未找到图像 {image_path}，继续重试...")

        time.sleep(1)  # 每秒检查一次

    print(f"未在 {timeout} 秒内找到图像 {image_path}.")
    return None


# 将指定区域覆盖为白色
def cover_with_white(region):
    """将指定的区域覆盖为白色"""
    left, top, width, height = region

    # 截取指定区域
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # 转为PIL图像对象
    img = screenshot.convert("RGB")

    # 创建ImageDraw对象来绘制白色矩形
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, width, height], fill="white")

    # 保存为临时图像文件
    img.save("temp_screenshot.png")

    # 这里我们不需要用flush()来更新显示
    # 用pyautogui点击以触发更新
    pyautogui.click(left + width // 2, top + height // 2)


def click_Start():
    while True:
        result = locate_image_on_screen(earnStart_path, confidence=0.9, timeout=3)
        if result:
            clickPosition.click_at_position(result)
            time.sleep(8)
            closeBrowser.colse_Browser()
        else:
            break


def main():
    # 第一次匹配区域
    first_match_result = locate_image_on_screen(earnOutStart_path, confidence=0.99)

    if first_match_result:
        # 获取第一次匹配的区域 (left, top, width, height)
        first_match_left, first_match_top, first_match_width, first_match_height = first_match_result
        print(f"第一次匹配区域: {first_match_left}, {first_match_top}, {first_match_width}, {first_match_height}")

        # 将第一次匹配区域覆盖成白色
        cover_with_white(first_match_result)

        # 进行第二次匹配，避免白色区域干扰
        second_match_result = locate_image_on_screen(earnStart_path, confidence=0.9, timeout=3)

        if second_match_result:
            print("2")
        else:
            print("3")


# 运行主程序
if __name__ == "__main__":
    main()
