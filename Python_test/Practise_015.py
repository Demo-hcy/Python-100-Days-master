"""
现有2元、3元、5元共三种面额的货币，如果需要找零99元，一共有多少种找零的方式？
"""

from functools import lru_cache


@lru_cache()
def change_money(total):
    if total == 0:
        print("11111")
        return 1
    if total < 0:
        print("222222")
        return 0
    return change_money(total - 2) + change_money(total - 3) + change_money(total - 5)


if __name__ == '__main__':
    print(change_money(10))
