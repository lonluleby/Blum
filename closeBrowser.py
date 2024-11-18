import time

import psutil


def colse_Browser():
    # 指定浏览器的进程名称
    browser_name = "Edge"  # 或 "firefox"

    # 遍历所有进程
    for proc in psutil.process_iter(['pid', 'name']):
        if browser_name.lower() in proc.info['name'].lower():
            # print(f"Terminating {proc.info['name']} with PID {proc.info['pid']}")
            proc.terminate()
            print("已关闭浏览器")
            time.sleep(1)
