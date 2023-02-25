import cv2
import os

# Cutting the input image to h*w blocks
# heightCutNum = 272;
# widthCutNum = 272;

# The folder path of input and output
# C:\\Users\\yangs\\Downloads\\labels_land_cover_20121\\2012\\D14
inPath = "C:\\Users\\yangs\\Downloads\\labels_land_cover_20121\\2012\\D35"
# C:\Users\yangs\Desktop\数据集\s2looking\S2Looking\train\OUTC:\\Users\\yangs\\Downloads\\labels_change1\\change\\D14
outPath = "2012_label/D35"
# 2012_label/D14
k = 0
for f in os.listdir(inPath):
    # print(f)
    path = inPath + '/' + f.strip()
    # print(path)
    img = cv2.imread(path,-1)
    # print(img)
    # The size of each input image
    height = img.shape[0]
    # print("height",height)
    width = img.shape[1]

    # The size of block that you want to cut
    # heightBlock = int(height / heightCutNum)
    # widthBlock = int(width / widthCutNum)
    heightBlock = 256
    widthBlock = 256

    for i in range(0, height, heightBlock):
        # print("i", i)
        for j in range(0, width, widthBlock):
            # print("j", j)
            k = k+1
            # print("k", k)
            cutImage = img[i :i + 256, j: j+ 256]
            savePath = outPath + '/' + str(k) + ".png"
            cv2.imwrite(savePath, cutImage)
