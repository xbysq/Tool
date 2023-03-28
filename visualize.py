import glob
import itertools
import os
import sys
import seaborn as sns
import numpy as np
import pandas as pd
from PIL.Image import Image
from cv2 import cv2
from matplotlib import pyplot as plt
from tqdm import tqdm
def fast_hist(a, b, n):
    k = (a >= 0) & (a < n)
    # print(k.size)
    return np.bincount(n * a[k].astype(int) + b[k], minlength=n ** 2).reshape(n, n)

def get_hist(image, label):
    # print(image.shape)
    hist = np.zeros((7, 7))
    hist += fast_hist(image.flatten(), label.flatten(), 7)
    return hist
def visualize_hist():
    INFER_DIR1 = 'C:\\Users\\yangs\\Desktop\\SSCDL\\out1'  # Inference path1
    INFER_DIR2 = 'C:\\Users\\yangs\\Desktop\\SSCDL\\out2'  # Inference path2
    LABEL_DIR1 = 'C:\\Users\\yangs\\Desktop\\SECOND2\\test\\label1'  # GroundTruth path
    LABEL_DIR2 = 'C:\\Users\\yangs\\Desktop\\SECOND2\\test\\label1'  # GroundTruth path
    infer_path_list1 = []
    infer_path_list2 = []
    label_path_list1 = []
    label_path_list2 = []
    for file in os.listdir(INFER_DIR1):
        file_path = os.path.join(INFER_DIR1, file)
        infer_path_list1.append(file_path)
    for file in os.listdir(INFER_DIR2):
        file_path = os.path.join(INFER_DIR2, file)
        infer_path_list2.append(file_path)
    infer_path_list1.sort()
    infer_path_list2.sort()
    infer_list = infer_path_list1 + infer_path_list2

    for file in os.listdir(LABEL_DIR1):
        file_path = os.path.join(LABEL_DIR1, file)
        label_path_list1.append(file_path)
    for file in os.listdir(LABEL_DIR2):
        file_path = os.path.join(LABEL_DIR2, file)
        label_path_list2.append(file_path)
    label_path_list1.sort()
    label_path_list2.sort()
    label_list = label_path_list1 + label_path_list2

    hist = np.zeros((7, 7))
    for infer, gt in tqdm(zip(infer_list, label_list)):

        try:
            infer = cv2.imread(infer, cv2.IMREAD_GRAYSCALE)
        except:
            print("File1 open error")
            sys.exit(0)
        try:
            label = cv2.imread(gt, cv2.IMREAD_GRAYSCALE)
        except:
            print("File2 open error")
            sys.exit(0)


        hist += get_hist(infer, label)
        # print(hist.shape)
    return hist


if __name__ == '__main__':
    trans_mat = visualize_hist()
    # print(trans_mat.shape)
    trans_prob_mat = trans_mat / np.sum(trans_mat, 0)
    # print(np.sum(trans_mat, 0))
    # trans_prob_mat = trans_mat / np.std(trans_mat)
    # trans_prob_mat = trans_mat
    # trans_prob_mat = trans_mat / [trans_mat[0][0] + trans_mat[1][0] + trans_mat[2][0] + trans_mat[3][0] + trans_mat[4][0] + trans_mat[5][0] + trans_mat[6][0],
    #                               trans_mat[0][1] + trans_mat[1][1] + trans_mat[2][1] + trans_mat[3][1] + trans_mat[4][1] + trans_mat[5][1] + trans_mat[6][1],
    #                               trans_mat[0][2] + trans_mat[1][2] + trans_mat[2][2] + trans_mat[3][2] + trans_mat[4][2] + trans_mat[5][2] + trans_mat[6][2],
    #                               trans_mat[0][3] + trans_mat[1][3] + trans_mat[2][3] + trans_mat[3][3] + trans_mat[4][3] + trans_mat[5][3] + trans_mat[6][3],
    #                               trans_mat[0][4] + trans_mat[1][4] + trans_mat[2][4] + trans_mat[3][4] + trans_mat[4][4] + trans_mat[5][4] + trans_mat[6][4],
    #                               trans_mat[0][5] + trans_mat[1][5] + trans_mat[2][5] + trans_mat[3][5] + trans_mat[4][5] + trans_mat[5][5] + trans_mat[6][5],
    #                               trans_mat[0][6] + trans_mat[1][6] + trans_mat[2][6] + trans_mat[3][6] + trans_mat[4][6] + trans_mat[5][6] + trans_mat[6][6]
    #                               ]
    # print(trans_mat[0][0]+trans_mat[1][0] + trans_mat[2][0] + trans_mat[3][0] + trans_mat[4][0] + trans_mat[5][0] + trans_mat[6][0])
    # print(np.sum(trans_mat, 1))
    # trans_prob_mat = (trans_mat.T / np.sum(trans_mat, 1)).T
    if True:
        label = ["{}".format(i-1) for i in range(1, trans_mat.shape[0] + 1)]
        df = pd.DataFrame(trans_prob_mat, index=label, columns=label)

        # Plot
        plt.figure(figsize=(7.5, 6.3))
        ax = sns.heatmap(df, xticklabels=df.corr().columns,
                         yticklabels=df.corr().columns, cmap=plt.cm.Blues,
                         linewidths=6, annot=True)

        # Decorations
        plt.xticks(fontsize=16, family='Times New Roman')
        plt.yticks(fontsize=16, family='Times New Roman')
        plt.ylabel('predict')
        plt.xlabel('true')
        plt.tight_layout()
        plt.savefig('res/SSCDL.png', transparent=True, dpi=800)
        # plt.show()
