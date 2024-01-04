from PIL import Image
import numpy as np
import os

SS_path = "/home/dml307/exp/ysq/HRSCD_NEW/train/label1"
CD_path = "/home/dml307/exp/ysq/HRSCD_NEW/train/label"

SS_file_namelist = os.listdir(SS_path)

for i in SS_file_namelist:

    SS_img = Image.open(os.path.join(SS_path, i))
    SS_arr = np.array(SS_img)

    CD_img = Image.open(os.path.join(CD_path, i))
    CD_arr = np.array(CD_img)

    SCD_arr = SS_arr * CD_arr

    SCD_img = Image.fromarray(SCD_arr)
    SCD_img.save(os.path.join(SS_path, i))

