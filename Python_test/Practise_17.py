from os import times

items = [1, 2, 3, 4]
print([i for i in items if i > 2])  # 3,4
print([i for i in items if i % 2])  # 1,3
print([(x, y) for x, y in zip('abcd', (1, 2, 3, 4, 5))])   #('a', 1), ('b', 2), ('c', 3), ('d', 4)
print({x: f'item{x ** 2}' for x in (2, 4, 6)})   # 2: 'item4', 4: 'item16', 6: 'item36'
print(len({x for x in 'hello world' if x not in 'abcdefg'}))  #  6


