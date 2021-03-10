"""
Lambda函数是什么，举例说明的它的应用场景
"""

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
items = list(map(lambda x: x ** 2,filter(lambda x: x%2,items)))
print(items)


items = [12, 5, 7, 10, 8, 19]
items = [x ** 2 for x in items if x % 2]
print(items)    # [25, 49, 361]