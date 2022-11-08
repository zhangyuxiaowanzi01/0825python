import random

# 内置  第一级
# 标准  第二级 [当前目录，标准包，第三方]
# random.random()	实数相关	用于生成一个0到1的随机浮点数: [0, 1)
"""
print(random.random())
"""
# random.uniform(a,b)		生成[a,b]或[b,a]之间的均匀分布随机浮点数。
"""
print(random.uniform(1, 10))
"""

# random.randint(a,b)	整数相关	生成[a,b]的随机整数，要求a < b。
"""
for i in range(3):
    print(random.randint(1, 10))
"""

# random.randrange(a,b)		生成[a,b)的随机整数，第三个参数可以指定步长。
"""
print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))
"""

# random.choice(seq)	序列相关	从序列中随机选择一个元素，若序列为空，则抛出异常。
# seq:list str tuple
"""
print(random.choice(['python', 'mysql', 'linux']))
print(random.choice(('python', 'mysql', 'linux')))
print(random.choice('hello'))
"""

# random.shuffle(seq)		打乱原序列，原序列必须可写。
"""
list1 = ['python', 'mysql', 'linux']
random.shuffle(list1)
print(list1)
"""

# random.sample(seq,k)		从序列中随机选择k个元素返回，原序列不变。
"""
list1 = ['python', 'mysql', 'linux', 'git', 'shell', '禅道']
print(random.sample(list1, 2))
str1 = 'hello'
print(random.sample(str1, 2))
"""

# random.seed(n=none)	初始化	初始化随机熵池。
random.seed(2)

print(random.randint(1, 10))

random.seed(5)
list1 = ['python', 'mysql', 'linux', 'git', 'shell', '禅道']
print(random.sample(list1, 2))
