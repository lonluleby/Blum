import pyautogui
from PIL import Image

# 定义截图的区域
LEFT, TOP, RIGHT, BOTTOM = 0, 0, 760, 1300

# 截取指定区域的屏幕截图
screenshot = pyautogui.screenshot(region=(LEFT, TOP, RIGHT-LEFT, BOTTOM-TOP))

# 显示截图
screenshot.show()
