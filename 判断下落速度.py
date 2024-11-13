import pyautogui
import time

time.sleep(3)
# 第一次截图并保存
start_time=time.time()
screenshot1 = pyautogui.screenshot()
# screenshot1.save("screenshot1.png")
# print("第一张截图已保存：screenshot1.png")


# 等待 1 秒
time.sleep(0.947)

# 第二次截图并保存
end_time=time.time()
screenshot2 = pyautogui.screenshot()
# screenshot2.save("screenshot2.png")
# print("第二张截图已保存：screenshot2.png")
time=end_time-start_time
print(time)
screenshot1.show()  # 显示截图
screenshot2.show()  # 显示截图


#382/s