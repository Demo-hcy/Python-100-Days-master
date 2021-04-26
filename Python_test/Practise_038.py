class A:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

obj = A(1)
obj.__value = 2
print(obj.value)
print(obj.__value)