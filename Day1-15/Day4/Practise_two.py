def Star():
    row = eval(input('请输入行数: '))
    if row is None or row<= 0 :
        print("请输入正确的行数")
    for i in range(row):
        for j in range(i + 1):
            print('*', end='')
        print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for j in range(row - i - 1):
            print(' ', end='')
        for j in range(2 * i + 1):
            print('*', end='')
        print()

if __name__ == '__main__':
    Star()