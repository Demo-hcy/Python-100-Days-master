# from Module.module1 import foo
# foo()
# from Module.module2 import foo
# foo()
#
#
# import Module.module1 as m1
# import Module.module2 as m2
#
# print(m1.foo(),"m1")
# print(m2.foo(),"m2")

import Module.module3

def foo():
    b = 'hello'

    def bar():
        c = True
        print("a为：",a)
        print(b)
        print(c)

    bar()


if __name__ == '__main__':
    a = 100
    foo()