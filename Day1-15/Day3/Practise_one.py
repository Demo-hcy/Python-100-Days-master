def Log():
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    if username == "123" and password =="123456":
        print("用户校验通过")
    else:
        print("用户校验没有通过")

if __name__ == '__main__':
    Log()