# import re
#
#
# def main():
#     usrname = input("请输入用户名：")
#     passward = input("请输入密码：")
#     name = re.match(r'^[0-9a-zA-Z_]{6,20}$', usrname)
#     if not name:
#         print('请输入有效的用户名.')
#     pawd = re.match(r'^[1-9]\d{4,11}$', passward)
#     if not pawd:
#         print('请输入有效的密码.')
#     if name and pawd:
#         print('你输入的信息是有效的!')
#
#
# if __name__ == '__main__':
#         main()

init_usrname = input("请输入初始用户名:")
init_password = input("请输入初始用户密码：")
# 打印输出设置好的用户名和初始登录密码
print(init_usrname)
print(init_password)

# 进入登录界面，flag0指的是输入密码错误的次数
# flag1指的是登录成功标志位
flag0 = 0
flag1 = 1
print(">>>>User Login<<<<<")
print(">>>>  用户登录 <<<<<")
while True:
    # 提示用户输入用户名
    usr = input("输入用户名:")
    if usr == init_usrname:
        # 输入用户名正确则进入到输入登录密码阶段
        # 判断输错登录密码次数
        while flag0 < 3:
            password = input("输入密码:")
            if password == init_password:
                # 若密码输入正确则登录成功因而跳出循环
                print("Success Login（登录成功）!")
                flag1 = 1
                break
            else:
                # 计算输错次数，每输错一次flag加1
                flag0 += 1
                if flag0 < 3:
                    print("密码错误，请重新输入!")
# 输错三次跳出输入扥路密码环节重新进行用户名的输入，相应的flag也要归零
            if flag0 == 3:
                print("你已经失败三次了...")
                break
    else:
        flag0 += 1
        if flag0 < 3:
            print("用户名错误，请重新登录!")
    if flag0 == 3:
        print("你已经失败三次了，请重新登录")
        break
