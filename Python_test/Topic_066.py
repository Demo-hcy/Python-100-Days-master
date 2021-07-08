class MyIterator:
    def __init__(self,x=2,xmax=100):
        self.__mul,self.__x=x,x
        self.__xmax = xmax

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x  and self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__xmax:
                return self.__mul
            else:
                raise StopIteration
        else:
            raise StopIteration

class Myiter:
    def __init__(self):
        self. myiterator = MyIterator()

    def info(self):
        for i in self.myiterator:
            print('迭代数据为：', i)

if __name__ == '__main__':
    myiter = Myiter()
    myiter.info()