import pyautogui
import time
import os
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 截取“251”文件夹的图像
folder_image = "Blum/blum.png"  # 你需要手动准备此图像


def check_image_exists(image_path):
    """检查图像文件是否存在"""
    if not os.path.exists(image_path):
        logging.error(f"图像文件 {image_path} 不存在，请确保该图像文件在程序运行的目录中。")
        return False
    return True


def locate_image_on_screen(image_path, confidence=0.8, timeout=10):
    """在屏幕上查找图像位置，增加超时机制"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            position = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if position:
                return position
        except pyautogui.ImageNotFoundException:
            logging.warning(f"未找到图像 {image_path}，继续重试...")
        time.sleep(0.5)  # 每半秒检查一次
    logging.error(f"未在 {timeout} 秒内找到图像 {image_path}.")
    return None


def main():
    """主程序执行流程"""
    if not check_image_exists(folder_image):
        return

    logging.info("开始搜索图像...")
    folder_position = locate_image_on_screen(folder_image)

    if folder_position:
        left, top, width, height = folder_position
        logging.info(f"文件夹坐标: 左={left}, 上={top}, 宽={width}, 高={height}")
    else:
        logging.error("未找到名为“251”的文件夹。")


if __name__ == "__main__":
    main()
