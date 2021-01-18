def Many_judgment():
    x = float(input("请输入x："))
    if x >1:
        y = 3*x-5
        print("计算结果为："+ f'{y:.1f}' ,"输入的x为"+f'{x:f}')
    elif -1<=x and x<=1:
        y=x+2
        print("计算结果为："+ f'{y:.1f}' )
    else:
        y = 5*x+3
        print("计算结果为："+ f'{y:.1f}' )


if __name__ == '__main__':
    Many_judgment()