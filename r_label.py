import numpy as np
import os
from PIL import Image
from tqdm import tqdm




if __name__ == '__main__':
    path = 'C:\\Users\\yangs\\Desktop\\HRSCD_512\\train\\label1_rgb'
    out_path = 'C:\\Users\\yangs\\Desktop\\HRSCD_\\train\\label1_rgb'
    filenames = os.listdir(path)
    for filename in tqdm(filenames):
        gt1 = np.array(Image.open(os.path.join(path, filename)))
        # mask_bin = np.zeros_like(gt1)
        if gt1.all():
            mask_bin = Image.fromarray(gt1.astype(np.uint8))
            mask_bin.save(os.path.join(out_path, filename))
