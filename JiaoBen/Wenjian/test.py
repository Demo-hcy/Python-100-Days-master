import os
import shutil
import time


def CP():
    start_time = time.time()
    # 需要被复制的文件夹
    old_path = r'E:\Python-100-Days-master\JiaoBen\Wenjian\Gen_File.py'
    new_path = r'E:\Python-100-Days-master\JiaoBen\Wenjian\tool'
    all_list = os.listdir(old_path)
    for i in all_list:
        print(i)
    name, suffix = i.rsplit('.json')
    name = name.replace('.', '')
    old_name = old_path + '\ ' + i
    new_name = new_path + '\ ' + name + ".json"
    shutil.copyfile(old_name, new_name)
    print(len(all_list))
    print(all_list)
    end_time = time.time()
    print(end_time - start_time, '秒')


if __name__ == '__main__':
    CP()