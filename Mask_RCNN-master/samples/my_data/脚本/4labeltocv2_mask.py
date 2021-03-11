#将生成文件夹json中的png格式label文件存入cs2_mask文件夹中

import os
from shutil import copyfile
for root, dirs, names in os.walk(r'D:\my_data\labelme_json'):   # 改成你自己的json文件夹所在的目录
    for dr in dirs:
        file_dir = os.path.join(root, dr)
        print(dr)
        # file = os.path.join(file_dir,'label.png')
        # print(file)
        new_name = dr.split('_')[0] + '.png'
        new_file_name = os.path.join(file_dir, new_name)
        print(new_file_name)
        
        tar_root = r'D:\my_data\cv2_mask'      # 目标路径
        tar_file = os.path.join(tar_root, new_name)
        copyfile(new_file_name, tar_file)