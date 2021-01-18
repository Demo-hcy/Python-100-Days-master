def Year():
    y = int(input("请输入年份："))
    leap_year = y %4 ==0 and y %100!= 0 or y % 400 == 0
    print(leap_year)

if __name__ == '__main__':
    Year()