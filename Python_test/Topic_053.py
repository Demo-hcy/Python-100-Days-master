class ABC:
    def info(self):
        print('测试')
    def Number(self,x,y):
        return x+y

class DEF:
    def __init__(self,x,y=1):
        self.x =x
        self.y =y
    def Add(self):
        return  self.x +self.y


if __name__ == '__main__':
    # abc = ABC()
    # print('第一个方法')
    # abc.info()
    # print('第二个方法')
    # print(abc.Number(1,2))
    de= DEF(3)
    print(de.Add())
    fd = DEF(3,4)
    print(fd.Add())