
'''
导入A文件夹图片，将其转换为数组，查看其中是否有像素0，如果没有零，就将其复制到B文件夹
'''

import os
from PIL import Image
import numpy as np
import shutil

# A文件夹为原始图像
# B文件夹为处理后保存图像
A='/home/dml307/exp/ysq/HRSCD/train/2012label_rgb'
B='/home/dml307/exp/ysq/HRSCD_NEW/train/label1'

# 获取文件夹中的所有文件名
files = os.listdir(A)
# 筛选出图片文件
image_files = [f for f in files]

# 遍历每个图片文件
for image_file in image_files:
    # 打开图片文件
    img = Image.open(os.path.join(A, image_file))
    # 将图片转换为数组
    img_array = np.array(img)
    # 打印图片文件的文件名
    # print(image_file)
    # 打印图片形状
    # print(img.size)
    # 查看图片中是否有零像素
    if not (img_array == 0).any():
        # 如果没有零，就将其复制到B文件夹
        # print("1111111111")
        shutil.copy2(os.path.join(A, image_file), B)