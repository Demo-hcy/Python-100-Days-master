# def TestTry(index,flag = False):
#     stulst =['abc','def','ghk']
#     AFile = open('C:\\Users\\12569\\Desktop\\配置服务接口api.txt','wt+')
#     try:
#         AFile.write(stulst[index])
#     except IndexError:
#         pass
#     finally:
#         AFile.close()
#         print('打开文件结束')
#
# def Test(index,i):
#     stulst = ['abc', 'def', 'ghk']
#     try:
#         print(len(stulst[index])/i)
#     except IndexError:
#         print('ERROR')
#
# if __name__ == '__main__':
#     # print('NO IndexError')
#     # TestTry(1)
#     # print('IndexError')
#     # TestTry(4)
#     Test(1,4)
#     Test(5,4)
#     Test(1,0)

#
# def dd(y):
#     for x in range(y):
#         yield x,y = dd(5)
#         for x in y:
#             print(x)