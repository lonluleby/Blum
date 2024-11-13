import pygetwindow as gw


def move_window_to_position(x, y):
    """
    将所有标题中包含 'PWAS' 的窗口移动到目标位置，并确保窗口位于最上层
    """
    # 获取所有打开的窗口标题
    all_titles = gw.getAllTitles()

    # 筛选出包含 "PWAS" 的窗口标题
    windows = [title for title in all_titles if "‎Blum" in title]

    if windows:
        for title in windows:
            try:
                # 获取匹配窗口标题的窗口对象
                window = gw.getWindowsWithTitle(title)[0]

                # 使窗口恢复并激活，确保窗口在最上层
                window.restore()  # 恢复窗口（如果是最小化状态）
                window.activate()  # 激活窗口
                # 移动窗口到指定的位置
                window.moveTo(x, y)
                print(f"窗口 '{title}' 移动到 ({x}, {y})")
            except Exception as e:
                print(f"无法操作窗口 '{title}': {e}")
    else:
        print("未找到包含 'Blum' 的窗口")


# # 示例用法
# if __name__ == "__main__":
#     move_window_to_position(0, 0)
