# -*- coding: utf-8 -*-
import shutil
import os


def objFileName():
    local_file_name_list = "./img.txt"
    obj_name_list = []
    for i in open(local_file_name_list, 'r'):
        obj_name_list.append(i.replace('\n', ''))
        # print(obj_name_list)
    return obj_name_list


def copy_img():
    local_img_name = r'C:\\Users\\yangs\\Desktop\\Landsat-SCD\\label1'
    # 指定要复制的图片路径
    path = r'C:\\Users\\yangs\\Desktop\\Landsat\\test\\label1'
    # 指定存放图片的目录
    for i in objFileName():
        new_obj_name = local_img_name +'/' +i
        dir, file = os.path.split(new_obj_name)
        shutil.copy(new_obj_name, path + '/' + file)


if __name__ == '__main__':
    copy_img()