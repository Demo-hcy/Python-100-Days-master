# class  Test:
#     def __init__(self,faa):
#         self.__faa = faa
#
#     def __bar(self):
#         print(self.__faa)
#         print('__bar')
#
#
# def main():
#     test = Test('hello')
#
#     test._Test__bar()
#
#     print(test._Test__faa)
#
#
# if __name__ == "__main__":
#     main()

class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name + ': ' + str(self.__age)


def main():
    stu = Student('骆昊', 38)
    # 'Student' object has no attribute '__name'
    # print(stu.__name)
    # 用下面的方式照样可以访问类中的私有成员
    print(stu._Student__name)
    print(stu._Student__age)


if __name__ == '__main__':
    main()