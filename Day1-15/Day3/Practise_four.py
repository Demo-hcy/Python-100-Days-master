def Grades():
    fraction = int(input("成绩："))
    if fraction >=90:
        G = 'A'
        print(G)
    elif fraction >=80 or fraction < 90:
        G = 'B'
        print(G)
    elif fraction >=70 or fraction < 80:
        G = 'C'
        print(G)
    elif fraction >= 60 or fraction < 70:
        G = 'D'
        print(G)
    else:
        G = 'E'
        print(G)

if __name__ == '__main__':

    Grades()
    print("分数对应等级：",Grades())

