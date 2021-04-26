# message= 'hello the world'
# print(message.replace("o","l"))
#
# import re
#
# message = 'hello, world!'
# pattern = re.compile('[l]')
# print(pattern.sub('#', message))

# filenames = ['a12.txt', 'a8.txt', 'b10.txt', 'b2.txt', 'b19.txt', 'a3.txt']
# dict = {'a8.txt':'a08.txt','b2.txt':'b02.txt','a3.txt':'a03.txt'}
# genhuan_filenames = [dict[x] if x in dict else x for x in filenames]
# new_filenames = sorted(genhuan_filenames)
# dict = {'a08.txt':'a8.txt','b02.txt':'b2.txt','a03.txt':'a3.txt'}
# Tihuan_filenames = [dict[x] if x in dict else x for x in new_filenames]
# print(Tihuan_filenames)

# filenames = ['a12.txt', 'a8.txt', 'b10.txt', 'b2.txt', 'b19.txt', 'a3.txt']
# new_filenames = sorted(filenames)
# print(new_filenames)
# number = input('请输入一串数字：')
# number_list = list(map(int,list(number)))
# number_list.sort()
# print('排序后的数字列表为：%s' % number_list)


# val = quzhi[0:2] + '0'
# print(val)
# print(quzhi)
# huifu = quzhi.split(",")  #  str -->list
# print(huifu)



def panduan(filenames):
    # quzhi = ",".join(filenames)
    # a = quzhi.zfill(5)
    # print(a)
    # quzhi = ",".join(filenames)  # list -->str
    for i in filenames:
        # print(i)
        if len(i) < 3 :
            new_filenames = i[0] + '0' + i[1]
            #         # huifu = new_filenames.split(",")
            return new_filenames
    #     new_list = i + new_filenames
    #     print(new_list)
    #     # else:
    #     pai = list(i)
    #     print(pai)
    #     while len(huifu):
    #         Result = sorted(huifu)
    #         print(Result)


def paixu():
    a = panduan(filenames)

    print(a)


if __name__ == '__main__':
    filenames =['a12', 'a8', 'b10', 'b2', 'b19', 'a3']
    panduan(filenames)
    paixu()
