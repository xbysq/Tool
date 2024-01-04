import os

# 指定文件夹路径
folder_path = "/home/dml307/exp/ysq/HRSCD_NEW/train/label1"

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    # 检查文件是否以.tif结尾
    if file_name.endswith(".tif"):
        # 构造新的文件名（去掉.tif后缀，加上.png后缀）
        new_file_name = file_name[:-4] + ".png"
        # 构造原始文件和新文件的完整路径
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)
        # 重命名文件
        os.rename(old_file_path, new_file_path)
