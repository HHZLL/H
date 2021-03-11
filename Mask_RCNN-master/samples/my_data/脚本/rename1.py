#将文件夹中第一个图片名字命名为文件夹前缀
import os
for root, dirs, names in os.walk(r'D:\Camera Roll\Crop classification\ML\order'):   # 改成你自己的json文件夹所在的目录
   
    for dr in dirs:
        file_dir = os.path.join(root, dr)
       # print(file_dir)
       # print(dr)
        b = os.listdir(file_dir)
        #print(b)
        new_name = dr.split('_')[0] + '.png'
        img_name= b[0].split('.')[0]+ '.json.png'
        file = os.path.join(file_dir, img_name)
        # # print(file)
        # new_name = dr.split('_')[0] + '.png'
        new_file_name = os.path.join(file_dir, new_name)
        print(new_file_name)
        os.rename(file, new_file_name)
