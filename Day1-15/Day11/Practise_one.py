# 读取文件

def main():
    f = open('C:\\Users\\zrwjh\\Desktop\\测试.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()
