# TODO 前置知识
# 索引【下标】， 列表里元素的序号
# 可以用索引获取列表中的元素
# 语法：list[索引]
"""
list1 = ['python', 'mysql']
print(list1[0])
print(list1[-2])
"""

# TODO del 列表[索引]
list1 = ['python', 'mysql']
del list1[0]
print(list1)

# TODO list.remove(数据)
list1 = ['python', 'mysql', 'python']
list1.remove('python')
print(list1)
print('==' * 20)

# TODO list.pop([索引]) 默认弹出列表末尾的数据，如果设置了索引就弹出指定数据
# 不指定索引
list1 = ['python', 'mysql', 'git']
item = list1.pop()
print(item)
print(list1)

# 指定了索引
item = list1.pop(-1)
print(item)
print(list1)
print('==' * 20)

# TODO list.clear()
list1 = ['python', 'mysql', 'git']
list1.clear()
print(list1)
