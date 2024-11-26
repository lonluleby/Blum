import  executeFilesInOrder
import time


# parent_folder = r'E:\telegram'
parent_folder = r'C:\Users\77032\Documents\5个\5个'
startNumber = 252

# 示例用法
if __name__ == "__main__":
    start_time1=time.time()
    executeFilesInOrder.run_exe_in_subfolders(parent_folder,startNumber)
    end_time1=time.time()
    print("耗时："+str(end_time1-start_time1))
    input("按任意键退出...")
