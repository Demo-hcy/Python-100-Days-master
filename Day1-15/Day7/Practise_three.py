def get_suffix(filename):
    """
    :param filename: 文件名称
    :return: 返回的后缀名
    """
    pos = filename.rfind('.')
    print('.出现的下标是%d' % pos)
    # 如果没有匹配项返回-1，不等于-1就有后缀名
    if pos != -1:
        print(filename[pos:])
    else:
        print('输入错误')

if __name__ == '__main__':
    file_name = input('请输入文件名:')
    get_suffix(file_name)