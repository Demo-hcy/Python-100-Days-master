# def maxnum(x):
#     list1 = x
#     maxfirst = max(list1)
#     list1.pop()
#     maxsecond = max(list1)
#     return maxfirst, maxsecond
#
#
# list = [1, 2, 3, 4, 5, 6]
# num = maxnum(list)
# print(num)


# def maxnum(x):
#     m1 = max(x)#  m1是最大元素
#     x2 = x.copy()#  复制一个列表，同时不破坏原来的列表
#     x2.remove(m1) # 把列表里最大的元素删除
#     m2 = max(x2) #  再次取列表里最大的元素，这时取到的就是列表里第二大的元素
#     return m2,m1  #  m1是第二大的值,m2是最大值
#
# list = [1, 2, 3, 4, 5, 6]
# num = maxnum(list)
# print(num)