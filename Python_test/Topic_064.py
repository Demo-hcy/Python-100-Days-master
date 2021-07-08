import math

def PingFang(x):
    X = math.pow(x, 2)
    X = round(X, 2)
    if x < 0 :
        print("平方结果为",-X)
    else:
        print("平方结果为",X)

def JurDuiZhi(x):
    X = math.fabs(x)
    X = round(X,2)
    print("绝对值结果为",X)

def SuShu(x):
    if x >1:
        if x/1 ==x :
            print('这个数是素数')
        elif x/x  == x:
            print('这个数是素数')
        else:
            print('这个数不是素数')
    else:
        print('素数是大于1的正整数')

if __name__ == '__main__':
    x = float(input('请输入数字：'))
    PingFang(x)
    JurDuiZhi(x)
    SuShu(x)
