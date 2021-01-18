
def Radius():
    r = float(input("请输入圆的半径："))
    return r

def Perimeter():
    R = Radius()
    Per = 2*3.1415926*R
    print("周长为：",f'{Per:.1f}',)

def Area():
    R = Radius()
    Per = 3.1415926*R*R
    print("面积为：",f'{Per:.1f}',)


if __name__ == '__main__':
    Perimeter()
    Area()
