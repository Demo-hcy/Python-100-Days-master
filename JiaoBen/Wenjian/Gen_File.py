import shutil
import sys
import hashlib
import os.path
import _md5

path = 'E:\\Python-100-Days-master\\JiaoBen\\Wenjian'
def Generate_File(size):
    file_size=(512,1024,)
    for i  in range (1):
        j = str(i + 1)
        file_name = j + '.txt'
        # 以路径path新建一个文件
        file = open(file_name, 'w')
        # 根据文件大小，偏移文件读取位置
        file.seek(1024*size)

        # 然后在当前位置写入任何内容，
        file.write('1341234123423')
        file.close()



def get_file_md5(file_name):
    """
    计算文件的md5
    :param file_name:
    :return:
    """
    md5 = hashlib.md5()   #创建md5对象
    # f = open(path + "/" + file_name)
    with open(file_name,'rb') as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def CP():
    source = '1.txt'
    target = '../test2'

    assert not os.path.isabs(source)
    target = os.path.join(target, os.path.dirname(source))

    os.makedirs(target)
    try:
        shutil.copy(source, target)
    # except IOError as e:
    #     print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())

def Cmo():
    hasher1 = hashlib.md5()
    afile1 = open('1.txt', 'rb')
    buf1 = afile1.read()
    a = hasher1.update(buf1)
    print(str(hasher1.hexdigest()))

    hasher2 = hashlib.md5()
    afile2 = open('../test2/1.txt', 'rb')
    buf2 = afile2.read()
    b = hasher2.update(buf2)
    print(str(hasher2.hexdigest()))

    print(str(a) == str(b))


if __name__ == '__main__':

    print("生成文件成功-----")
    Generate_File(1)
    CP()
    print("比较文件MD5")
    Cmo()




