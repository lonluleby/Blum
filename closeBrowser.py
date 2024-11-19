import psutil
import os
import time
def close_all_browser_processes(browser_name,max_retries=5, delay=1):
    """
    尝试关闭所有 Chrome 浏览器进程。如果进程无法正常关闭，重试几次后强制终止所有进程。
    :param max_retries: 最大重试次数。
    :param delay: 重试间隔时间（秒）。
    :return: 如果成功关闭所有 Chrome 进程，返回 True；否则返回 False。
    """
    retries = 0
    while retries < max_retries:
        browser_procs = [proc for proc in psutil.process_iter(['pid', 'name']) if browser_name.lower() in proc.info['name'].lower()]

        # 如果没有找到浏览器进程，则返回成功
        if not browser_procs:
            print("所有浏览器进程已成功关闭。")
            return True

        # 尝试关闭所有浏览器进程
        for proc in browser_procs:
            try:
                print(f"找到 浏览器 进程: {proc.info['name']} (PID: {proc.info['pid']})")
                proc.terminate()  # 尝试优雅退出
                proc.wait(timeout=3)  # 等待进程退出

                # 如果进程没有退出，强制杀死
                if proc.is_running():
                    print(f"进程 {proc.info['pid']} 未退出，正在强制关闭...")
                    proc.kill()

                print(f"进程 {proc.info['name']} (PID: {proc.info['pid']}) 已关闭。")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # 进程已经消失，或无权限操作，跳过
                continue
            except psutil.TimeoutExpired:
                # 终止超时，强制 kill
                print(f"进程 {proc.info['pid']} 终止超时，正在强制关闭...")
                proc.kill()

        # 如果还有 浏览器 进程，等待重试
        print(f"重试 {retries + 1}/{max_retries}，等待 {delay} 秒后继续...")
        time.sleep(delay)
        retries += 1

    # 达到最大重试次数仍未成功，返回 False
    print("达到最大重试次数，无法关闭所有 浏览器 进程。")
    return False
