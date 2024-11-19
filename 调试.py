import psutil

# 获取所有正在运行的进程
for proc in psutil.process_iter(['pid', 'name']):
    try:
        # 如果进程名中包含 'chrome'，则输出该进程信息
        if 'chrome' in proc.info['name'].lower():
            print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # 处理进程可能在查询时已结束的情况
        pass
