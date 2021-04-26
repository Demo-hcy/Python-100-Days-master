"""
random.random()函数可以生成[0.0, 1.0)之间的随机浮点数。
random.uniform(a, b)函数可以生成[a, b]或[b, a]之间的随机浮点数。
random.randint(a, b)函数可以生成[a, b]或[b, a]之间的随机整数。
random.shuffle(x)函数可以实现对序列x的原地随机乱序。
random.choice(seq)函数可以从非空序列中取出一个随机元素。
random.choices(population, weights=None, *, cum_weights=None, k=1)函数可以从总体中随机抽取（有放回抽样）出容量为k的样本并返回样本的列表，可以通过参数指定个体的权重，如果没有指定权重，个体被选中的概率均等。
random.sample(population, k)函数可以从总体中随机抽取（无放回抽样）出容量为k的样本并返回样本的列表。
"""
import random
a =1
b = 10
x = [1,2,4,5,6,8]
q = random.random()
w = random.uniform(a,b)
e = random.randint(a,b)
random.shuffle(x)
t = random.choice(x)


print(q,w,e,x,t)

