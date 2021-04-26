def extend_list(val, items=[]):
    items.append(val)
    return items

list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')
print(list1)
print(list2)
print(list3)

"""
Python函数在定义的时候，默认参数items的值就被计算出来了，即[]。
因为默认参数items引用了对象[]，每次调用该函数，
如果对items引用的列表进行了操作，下次调用时，默认参数还是引用之前的那个列表而不是重新赋值为[]，
所以列表中会有之前添加的元素。
如果通过传参的方式为items重新赋值，那么items将引用到新的列表对象，
而不再引用默认的那个列表对象。
通常不建议使用容器类型的默认参数，像PyLint这样的代码检查工具也会对这种代码提出质疑和警告。
"""