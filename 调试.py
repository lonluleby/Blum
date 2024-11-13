from PIL import ImageGrab

# 定义截图区域
LEFT, TOP, RIGHT, BOTTOM = 0, 0, 960, 800

# 截图
screenshot = ImageGrab.grab(bbox=(LEFT, TOP, RIGHT, BOTTOM))

# 保存截图
screenshot.show()
