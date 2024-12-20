import os
import subprocess
import time

import psutil

import autoEarn
import foundProgram
import autoFarm


# # 设置父文件夹的绝对路径
# parent_folder = r'C:\Users\77032\Documents\5个\5个'
def run_exe_in_subfolders(parent_folder,startNumber):
    # 遍历 parent_folder 中的所有子文件夹（最多遍历两级）
    for root, dirs, files in os.walk(parent_folder):
        # 计算当前路径的深度，限制在两级内
        depth = root[len(parent_folder):].count(os.sep)

        # 如果当前深度大于或等于 2，则跳过更深层次的子文件夹
        if depth >= 1:
            dirs[:] = []  # 清空 dirs 列表，避免继续递归子目录

        # 遍历当前目录下的文件和文件夹
        for dir_name in dirs:
            if startNumber <= int(dir_name):
                subfolder_path = os.path.join(root, dir_name)
                exe_path = os.path.join(subfolder_path, 'Telegram.exe')

                # 检查子文件夹是否包含 Telegram.exe
                if os.path.isfile(exe_path):
                    try:
                        print(f"Running {exe_path}...")
                        # 使用 Popen 启动 exe，而不阻塞主程序
                        process = subprocess.Popen(exe_path)
                        # 等待 5 秒钟
                        time.sleep(10)
                        autoFarm.main()
                        autoEarn.main()
                        # 关闭该进程
                        if not close_process(process):
                            print(f"Failed to terminate {exe_path} after waiting.")
                        else:
                            print(f"Terminated {exe_path}, continuing with the next operation...")
                        close_fallback()
                    except FileNotFoundError:
                        print(f"{exe_path} not found!")
                else:
                    print(f"Telegram.exe not found in {subfolder_path}")

def close_process(process, timeout=60):
    """检测进程是否关闭，如果没有关闭，尝试终止它"""
    start_time = time.time()

    while time.time() - start_time < timeout:
        if process.poll() is not None:
            # 如果进程已经退出
            print("Process has already exited.")
            return True

        print("Process is still running, attempting to terminate...")
        try:
            process.terminate()  # 尝试终止进程
            time.sleep(1)  # 给进程时间终止

            if process.poll() is not None:
                print("Process terminated successfully.")
                return True

            # 如果 terminate() 失败，则尝试 kill() 强制终止
            print("Terminate failed, attempting to force kill the process.")
            process.kill()  # 强制终止进程
            time.sleep(1)  # 再给进程时间终止

            if process.poll() is not None:
                print("Process killed successfully.")
                return True

        except Exception as e:
            print(f"Error trying to terminate/kill process: {e}")
            return False

    print("Timeout reached. Process did not terminate.")
    # 强制杀死进程，确保在超时后进程最终终止
    if process.poll() is None:  # 如果进程还活着
        print("Forcing the process to terminate.")
        process.kill()
        return False

    return False


def close_fallback():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'Telegram.exe':  # 这里替换成程序名
            proc.kill()  # 结束进程
            print(f"进程 {proc.info['name']} 已被终止")


def main(parent_folder):
    run_aaa_exe_in_subfolders(parent_folder)


# if __name__ == "__main__":
#     main()
