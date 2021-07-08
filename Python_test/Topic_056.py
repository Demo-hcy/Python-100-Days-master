class ABC:

    @staticmethod
    def a():
        print('调用了a的静态方法')

    @classmethod
    def b(cls):
        print('调用了b的动态方法')

if __name__ == '__main__':
    ABC.a()
    ABC.b()
    abc = ABC()
    abc.a()
    abc.b()
