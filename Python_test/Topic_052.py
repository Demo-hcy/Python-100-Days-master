"""自定义函数实现对用户的登录验证，假设所有用户信息存在列表中，形式如下：
user = [
{‘name’:‘xuab’,‘password’:‘123’,‘usertype’:1},
{‘name’:‘hyc’,‘password’:‘1314’,‘usertype’:2},
{‘name’:‘yq’,‘password’:‘520’,‘usertype’:3},
{‘name’:‘lcz’,‘password’:‘1314520’,‘usertype’:4},
{‘name’:‘yqq’,‘password’:‘520’,‘usertype’:5}
]
验证成功返回用户类型，否则返回0"""
user = [
{'name':'123','password':'123','usertype':1},
{'name':'456','password':'456','usertype':2},
{'name':'789','password':'789','usertype':3},
{'name':'qwe','password':'qwe','usertype':4},
{'name':'asd','password':'qwe','usertype':5}
]

user_name_list = list(map(lambda name: name['name'],user))
print(user_name_list)
def Authenticate_user():
    name = input("请输入用户名：")
    if name in user_name_list:
        user_index = user_name_list.index(name)
        passwd = input("请输入密码：")
        if  passwd ==user[user_index]['password']:
            print("密码正确，登录成功")
            print("当前用户类型为：%d" % user[user_index]['usertype'])
        else:
            print('密码错误，错误代码：0')
    else:
        print('用户未注册，请注册或重新输入：')

def Authenticate_user2():
    for info in user:
        if info["name"] == '123':
            info.get("password")

if __name__ == '__main__':
    Authenticate_user()