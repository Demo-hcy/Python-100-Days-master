alist = [1,2,3,4,5,6]
print('使用append操作函数结果为：',alist.append(7),alist) # 列表末尾追加元素7
print('使用count操作函数结果为：',alist.count(3)) # 统计列表中3出现的次数
print('使用extend操作函数结果为：',alist.extend([2,'insert']),alist) # 列表末尾追加另一个列表
print('使用index操作函数结果为：',alist.index(3)) # 统计列表中3出现的索引位置
print('使用insert操作函数结果为：',alist.insert(3,3),alist) # 在列表的第三个位置插入3
print('使用pop操作函数结果为：',alist.pop(),alist) # 返回并删除列表最后一个元素
print('使用remove操作函数结果为：',alist.remove(3),alist) # 删除列表中元素3 ，且删除的是第一个元素
print('使用reverse操作函数结果为：',alist.reverse(),alist) #将列表中的元素颠倒
print('使用sort操作函数结果为：',alist.sort(),alist) #对列表进行排序

