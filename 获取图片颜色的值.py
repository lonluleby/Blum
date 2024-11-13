from PIL import Image


def get_colors_from_image(image_path):
    """
    获取PNG图像中的所有颜色。
    :param image_path: PNG图像路径
    :return: 返回一个包含所有颜色的集合，每个颜色为RGB元组
    """
    # 打开图像
    img = Image.open(image_path)

    # 如果图像有透明通道（RGBA），可以去掉Alpha通道并转换为RGB模式
    if img.mode == 'RGBA':
        img = img.convert('RGB')

    # 获取图像的尺寸
    width, height = img.size

    # 存储所有颜色
    colors = set()  # 使用set来自动去重

    # 遍历每个像素
    for x in range(width):
        for y in range(height):
            color = img.getpixel((x, y))  # 获取当前像素的颜色（RGB）
            colors.add(color)  # 将颜色加入集合中

    return colors


def get_common_colors(image_paths):
    """
    获取多张图像的共有颜色。
    :param image_paths: 图像路径的列表
    :return: 返回所有图像中的共同颜色集合
    """
    # 初始化公共颜色集合为第一个图像的颜色
    common_colors = get_colors_from_image(image_paths[0])

    # 对每张图像的颜色集合执行交集操作
    for image_path in image_paths[1:]:
        colors = get_colors_from_image(image_path)
        common_colors &= colors  # 交集运算

    return common_colors


# 示例：读取多张图像并获取共同颜色
image_paths = ['xin10.png', 'xin13.png']  # 替换为你的图片路径
# image_paths = ['xin1.png', 'xin2.png', 'xin4.png', 'xin5.png','xin7.png']  # 替换为你的图片路径

#(215, 250, 151)  3，6
#(207, 227, 74) 2，4，7，8
#(168, 249, 90) 1，2，4，5，7
#(228, 247, 146) 10，9，12
# (212, 250, 133)
# (212, 251, 132)
# 获取共同颜色
common_colors = get_common_colors(image_paths)

# 打印共有颜色
print(f"共同颜色 ({len(common_colors)}):")
for color in common_colors:
    print(color)
