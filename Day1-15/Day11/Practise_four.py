import time


def main():
    # 一次性读取整个文件内容
    Article = 'C:\\Users\\zrwjh\\Desktop\\测试.txt'
    with open(Article, 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open(Article, mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open(Article) as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main()
