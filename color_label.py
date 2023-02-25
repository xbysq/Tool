import numpy as np
import os
from PIL import Image
from tqdm import tqdm


def color_map():
    cmap = np.zeros((10, 3), dtype=np.uint8)
    # 土地覆盖图生成
    # cmap[0] = np.array([0, 0, 0])  #黑色
    # cmap[1] = np.array([128,128,128])# 灰色
    # cmap[2] = np.array([102,80,68]) # 褐色
    # cmap[3] = np.array([0,128,0])# 绿色
    # cmap[4] = np.array([144,238,144])# 浅绿
    # cmap[5] = np.array([0,0,255])  # 蓝色
    cmap[0] = np.array([255, 255, 255])  #黑色
    cmap[1] = np.array([130,87,87])# 灰色
    cmap[2] = np.array([255,0,0]) # 褐色
    cmap[3] = np.array([128,128,128])# 绿色
    cmap[4] = np.array([255,0,0])# 浅绿
    cmap[5] = np.array([0,0,255])  # 蓝色
    cmap[6] = np.array([128,128,128]) #
    cmap[7] = np.array([130,87,87])  #
    cmap[8] = np.array([128,128,128])  #
    cmap[9] = np.array([130,87,87])  #
    # 二值变化图生成
    # cmap[0] = np.array([0, 0, 0])  # 黑色
    # cmap[1] = np.array([255,255,255])# 白色
    # cmap[2] = np.array([255, 255, 255])  # 白色
    # cmap[3] = np.array([255, 255, 255])  # 白色
    # cmap[4] = np.array([255, 255, 255])  # 白色
    # cmap[5] = np.array([255, 255, 255])  # 白色
    # cmap[6] = np.array([255, 255, 255])  # 白色
    return cmap


if __name__ == '__main__':
    path = 'C:\\Users\\yangs\\Desktop\\Landsat-SCD_dataset\\label'
    out_path = 'C:\\Users\\yangs\\Desktop\\Landsat-SCD_dataset\\label2_rgb'
    filenames = os.listdir(path)

    cmap = color_map()

    for filename in tqdm(filenames):
        mask = Image.open(os.path.join(path, filename)).convert("P")

        # labels_bn = (mask > 0).unsqueeze(1).float()
        mask.putpalette(cmap)
        mask.save(os.path.join(out_path, filename))
