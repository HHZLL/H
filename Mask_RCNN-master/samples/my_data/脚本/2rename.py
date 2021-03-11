#为了适应模型内部默认的路径格式，需要对label.png进行简单的重命名
#比如你的json文件夹叫1_json，那这个png的图就应该改成1.png
import os
for root, dirs, names in os.walk(r'D:\Camera Roll\Crop classification\ML\order'):   # 改成你自己的json文件夹所在的目录
    for dr in dirs:
        file_dir = os.path.join(root, dr)
        # print(dr)
        file = os.path.join(file_dir, 'label.png')
        # print(file)
        new_name = dr.split('_')[0] + '.png'
        new_file_name = os.path.join(file_dir, new_name)
        os.rename(file, new_file_name)