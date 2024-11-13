import os
import subprocess
import time
import foundBlumProgram
import autoFarm


# # 设置父文件夹的绝对路径
# parent_folder = r'C:\Users\77032\Documents\5个\5个'
def run_aaa_exe_in_subfolders(parent_folder):
    # 遍历 parent_folder 中的所有子文件夹（最多遍历两级）
    for root, dirs, files in os.walk(parent_folder):
        # 计算当前路径的深度，限制在两级内
        depth = root[len(parent_folder):].count(os.sep)

        # 如果当前深度大于或等于 2，则跳过更深层次的子文件夹
        if depth >= 1:
            dirs[:] = []  # 清空 dirs 列表，避免继续递归子目录

        # 遍历当前目录下的文件和文件夹
        for dir_name in dirs:
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
                    # 关闭该进程
                    if not close_process(process):
                        print(f"Failed to terminate {exe_path} after waiting.")
                    else:
                        print(f"Terminated {exe_path}, continuing with the next operation...")
                except FileNotFoundError:
                    print(f"{exe_path} not found!")
                except Exception as e:
                    print(f"An unexpected error occurred while running {exe_path}: {e}")
            else:
                print(f"Telegram.exe not found in {subfolder_path}")

def close_process(process, timeout=5):
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
        except Exception as e:
            print(f"Error trying to terminate process: {e}")
            return False
    print("Timeout reached. Process did not terminate.")
    return False


def main(parent_folder):
    run_aaa_exe_in_subfolders(parent_folder)


# if __name__ == "__main__":
#     main()
