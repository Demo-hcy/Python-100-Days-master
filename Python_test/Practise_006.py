"""
说说Python中的浅拷贝和深拷贝

浅拷贝通常只复制对象本身，而深拷贝不仅会复制对象，还会递归的复制对象所关联的对象。
深拷贝可能会遇到两个问题：一是一个对象如果直接或间接的引用了自身，会导致无休止的递归拷贝；
二是深拷贝可能对原本设计为多个对象共享的数据也进行拷贝。
Python通过copy模块中的copy和deepcopy函数来实现浅拷贝和深拷贝操作，
其中deepcopy可以通过memo字典来保存已经拷贝过的对象，
从而避免刚才所说的自引用递归问题；
此外，可以通过copyreg模块的pickle函数来定制指定类型对象的拷贝行为。
"""

import copy


class PrototypeMeta(type):
    """实现原型模式的元类"""

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为对象绑定clone方法来实现对象拷贝
        cls.clone = lambda self, is_deep=True: \
            copy.deepcopy(self) if is_deep else copy.copy(self)


class Person(metaclass=PrototypeMeta):
    pass


p1 = Person()
p2 = p1.clone()                 # 深拷贝
p3 = p1.clone(is_deep=False)    # 浅拷贝