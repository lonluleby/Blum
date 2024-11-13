import os
from PIL import Image
import numpy as np
from collections import Counter


# 获取文件夹中的所有图片路径
def get_image_paths(folder_path):
    image_paths = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.PNG', '.jpg', '.jpeg', '.bmp', '.gif')):  # 常见图片格式
            image_paths.append(os.path.join(folder_path, filename))
    return image_paths


# 获取图片的颜色（RGB）信息
def get_image_colors(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')  # 转换为RGB模式
    colors = np.array(image).reshape(-1, 3)  # 将图片转换为每个像素的RGB值
    return colors


# 统计所有图片的颜色分布
def get_colors_from_images(image_paths):
    all_colors = []
    for image_path in image_paths:
        colors = get_image_colors(image_path)
        all_colors.extend(tuple(color) for color in colors)
    return all_colors


# 获取颜色的频率并返回前十名
def get_top_colors(all_colors, top_n=10):
    color_counter = Counter(all_colors)
    top_colors = color_counter.most_common(top_n)
    return top_colors


# 计算前十名颜色的整体范围
def calculate_color_range(top_colors):
    min_color = np.array([255, 255, 255])  # 初始化最小值为最大值
    max_color = np.array([0, 0, 0])  # 初始化最大值为最小值
    for color, count in top_colors:
        min_color = np.minimum(min_color, color)
        max_color = np.maximum(max_color, color)

    color_range = max_color - min_color
    return min_color, max_color, color_range


# 主函数
def analyze_colors_in_folder(folder_path):
    image_paths = get_image_paths(folder_path)
    all_colors = get_colors_from_images(image_paths)
    top_colors = get_top_colors(all_colors)

    # 打印前十名颜色和数量
    print("Top 10 colors and their counts:")
    for color, count in top_colors:
        print(f"Color: {color}, Count: {count}")

    # 计算颜色范围
    min_color, max_color, color_range = calculate_color_range(top_colors)
    print("\nOverall color range of the top 10 colors:")
    print(f"Min color: {min_color}")
    print(f"Max color: {max_color}")
    print(f"Color range: {color_range}")


# 示例使用
folder_path = "images2"  # 修改为你的文件夹路径
analyze_colors_in_folder(folder_path)
