import cv2
# from matplotlib import pyplot as plt
# img = cv2.imread("11.tif",-1)
#第二个参数是通道数和位深的参数，
# IMREAD_UNCHANGED = -1#不进行转化，比如保存为了16位的图片，读取出来仍然为16位。
#IMREAD_GRAYSCALE = 0#进行转化为灰度图，比如保存为了16位的图片，读取出来为8位，类型为CV_8UC1。
#IMREAD_COLOR = 1#进行转化为RGB三通道图像，图像深度转为8位
# IMREAD_ANYDEPTH = 2#保持图像深度不变，进行转化为灰度图。
#IMREAD_ANYCOLOR = 4#若图像通道数小于等于3，则保持原通道数不变；若通道数大于3则只取取前三个通道。图像深度转为8位
# print (img)
# print (img.shape) # (10000, 10000)
# print (img.dtype)# uint16
# print (img.min())
# print (img.max())

# 计算未变化与变化像素数
import os
from pylab import *
import matplotlib.pyplot as plt
# 图像上显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

import numpy
# from matplotlib import pyplot as plt
from tqdm import tqdm

a = numpy.zeros(7, dtype=int)
if __name__ == '__main__':
    path = './SECOND2/val/label1'
    path2 = './SECOND2/val/label2'
    filenames = os.listdir(path)
    filenames2 = os.listdir(path2)
    # print(filenames)
    for filenames in tqdm(filenames):
        # print(filenames)
        img = cv2.imread(os.path.join(path,filenames), 0)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                # print(img[i,j])
                if img[i, j] == 0:
                    a[0] += 1
                elif img[i,j]==1:
                    a[1] += 1
                elif img[i,j]==2:
                    a[2] += 1
                elif img[i,j]==3:
                    a[3] += 1
                elif img[i,j]==4:
                    a[4] += 1
                elif img[i,j]==5:
                    a[5] += 1
                elif img[i,j]==6:
                    a[6] += 1
                else:
                    print("error")
    np.savetxt("res/a1.txt", a)
    for filenames2 in tqdm(filenames2):
        # print(filenames)
        img = cv2.imread(os.path.join(path2,filenames2), 0)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                # print(img[i,j])
                if img[i, j] == 0:
                    a[0] += 1
                elif img[i, j] == 1:
                    a[1] += 1
                elif img[i, j] == 2:
                    a[2] += 1
                elif img[i, j] == 3:
                    a[3] += 1
                elif img[i, j] == 4:
                    a[4] += 1
                elif img[i, j] == 5:
                    a[5] += 1
                elif img[i, j] == 6:
                    a[6] += 1
                else:
                    print("error")
    np.savetxt("res/a2.txt", a)
x = ['水体', '地面', '低矮植被', '树木', '建筑物', '运动场']
plt.bar(x, a[1:], color='blue')
# 绘制条形图
# x = ('0', '1')
# y = [74361309/(74361309+25638691), 25638691/(74361309+25638691)]
# plt.bar(x, y)
# plt.title('hist')
plt.savefig('res/label.png')
# plt.show()
