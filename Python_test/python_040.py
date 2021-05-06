import random


def random_str():
    # random_num = str(random.randint(0, 9))
    # random_low_alpha = chr(random.randint(97, 122))
    # random_char = random.choice([random_num, random_low_alpha])
    # return random_char
    code_list = []
    # for i in range(10):  # 0~9
    #     code_list.append(chr(i))
    for i in range(48, 57):  # ASCII表示的数字0-9 chr()方法将10进制的数字传化为对应的字符
        code_list.append(chr(i))  # 将迭代器追加到列表
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z
        code_list.append(chr(i))
    code = random.sample(code_list, 6)  # 用于截取列表的指定长度的随机数，返回的是列表
    code_num = ''.join(code)  # 将列表里的元素以指定的字符连接生成一个新的字符串
    return code_num


if __name__ == '__main__':
    print("随机6位验证码：", random_str())
