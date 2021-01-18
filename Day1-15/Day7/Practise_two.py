import random


def Random_number(code_len):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
    """

    all_chars= '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for V_code in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
        print("测试：",index)
        print("结果：",code)
    return code

if __name__ == '__main__':
    Random_number(5)
