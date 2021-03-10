"""
假设你使用的是官方的CPython，说出下面代码的运行结果

True False
True False
True
"""
a, b, c, d = 1, 1, 1000, 1000
print(a is b, c is d)

def foo():
    e = 1000
    f = 1000
    print(e is f, e is d)
    g = 1
    print(g is a)

foo()