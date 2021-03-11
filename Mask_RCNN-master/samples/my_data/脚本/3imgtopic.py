#将生成文件夹json中的png格式label文件存入cs2_mask文件夹中

import os
from shutil import copyfile
for root, dirs, names in os.walk(r'D:\my_data\labelme_json'):   # 改成你自己的json文件夹所在的目录
    for dr in dirs:
        file_dir = os.path.join(root, dr)
        print(dr)
        ''' file = os.path.join(file_dir,'img.png')
        print(file)'''
       
        new_name1 = dr.split('_')[0] + '.png'
        new_name = 'img.png'
        new_file_name = os.path.join(file_dir, new_name)    #源文件路径
        print(new_file_name)
        
        tar_root = r'D:\my_data\pic'      # 目标路径
        tar_file = os.path.join(tar_root, new_name1)    #目标文件名
        copyfile(new_file_name, tar_file)