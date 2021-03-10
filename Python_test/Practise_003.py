"""
写一个删除列表中重复元素的函数，要求去重后元素相对位置保持不变
"""


# 方法1
# def dedup(items):
#     no_dup_items = []
#     seen = set()
#     for item in items:
#         if item not in seen:
#             no_dup_items.append(item)
#             seen.add(item)
#     return no_dup_items
#
# if __name__ == '__main__':
#     dep = dedup([1,11,1,12,13,1,14])
#     print(dep)


# 方法2
# def dedup(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#
#
# if __name__ == '__main__':
#     dep = dedup(['1', '12', '14', '1', '25', '51', '1'])
#     print(dep)


l1 = ['b','c','d','b','c','a','a']
l2 = sorted(set(l1),key=l1.index)
print(l2)
