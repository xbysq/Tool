# 边缘提取
import os
import numpy as np
from cv2 import cv2


def Edge_Extract(root):
    img_root = os.path.join(root, 'label')			# 修改为保存图像的文件名
    edge_root = os.path.join(root,'edge')			# 结果输出文件

    if not os.path.exists(edge_root):
        os.mkdir(edge_root)

    file_names = os.listdir(img_root)
    img_name = []

    for name in file_names:
        if not name.endswith('.png'):

            assert "This file %s is not PNG"%(name)
        img_name.append(os.path.join(img_root, name[:-4]+'.png'))

    index = 0
    for image in img_name:
        # print(image)
        img = cv2.imread(image)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #
        image,contours,hierarchy = cv2.findContours(gray , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        img_tmp = np.zeros_like(img)
        img_tmp = cv2.drawContours(img_tmp, contours, -1, (255,255,255), 1)
        img_tmp = cv2.cvtColor(img_tmp,cv2.COLOR_RGB2GRAY)
        # cv2.imwrite(edge_root + '/' + file_names[index], cv2.Canny(img, 30, 100))
        cv2.imwrite(edge_root + '/' + file_names[index],img_tmp)
        index += 1
    return 0
if __name__ == '__main__':
    root = 'C:\\Users\\yangs\\Desktop\\dataset\\LEVIR_256\\train'	# 修改为你对应的文件路径
    Edge_Extract(root)