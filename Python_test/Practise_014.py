"""
使用Python代码实现遍历一个文件夹的操作。
Python标准库os模块的walk函数提供了遍历一个文件夹的功能，它返回一个生成器。
"""
import os

def Resdfile():
    Path = os.walk("D:\公司\二代项目\动环盒子")
    for path, dir_list, file_list in Path:
        for dir_name in dir_list:
            print(os.path.join(path, dir_name))
        for file_name in file_list:
            print(os.path.join(path, file_name))

if __name__ == '__main__':
    print(Resdfile())