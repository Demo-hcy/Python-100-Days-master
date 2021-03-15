"""
写一个函数统计传入的列表中每个数字出现的次数并返回对应的字典。
"""

# 第一种方式:遍历
def count_letters1(items):
    result = {}
    for item in items:
        if isinstance(item, (int, float)):
            result[item] = result.get(item, 0) + 1
    return result

if __name__ == '__main__':
    print("第一种结果",count_letters1([1,2,4,4,4,2,21,5,6,6,7,88,8,8,9]))



# 第二种方式:构造字典

from collections import Counter

def count_letters2(items):
    counter = Counter(items)
    return {key: value for key, value in counter.items() if isinstance(key, (int, float))}

if __name__ == '__main__':
    print("第二种方式",count_letters2([1,2,4,4,4,2,21,5,6,6,7,88,8,8,9]))
