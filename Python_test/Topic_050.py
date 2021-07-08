def output(outputs):
    for i in outputs:
        print(i)

def test(a,b=0,*kw,**kwargs):
    print(a,b,kw,kwargs)

a =3
b=[1,2]
def test1(a,b):
    a =9
    b.append(3)
    print(a,b)
    print(a, b)

def seq():
    seq=(4,5,6,7,8,9)
    # seq1 = tuple(filter(lambda x:x%3 and x%2 ,seq))
    seq1 = list(filter(lambda x: x % 3 and x % 2, seq))
    print(seq1)





def  Sort():
    a = [1,3,5,7,9,2,4,6,8,10]
    b={'b':2,'a':1,'c':3}
    a.sort()
    print('数值排序为：',sorted(a))
    print('数值排序为：',a)
    print('数值排序为：',sorted(b))

def Space():
    a = ('1232  444 3123 333')
    b = [12,13,15,117,115,2,13,15]
    # a.count(' ')
    b.sort()
    print(a.count(' ')) # 计算空格的数量
    print(b)

if __name__ == '__main__':
    # output('a,b,c,d')
    # test(3)
    # test(3,4,5)
    # test(3,c=3)
    # test(c=3,3)
    # test1(9,[1,2])
    # seq()
    # Sort()
    Space()


