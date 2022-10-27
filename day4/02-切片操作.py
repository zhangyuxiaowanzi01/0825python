"""
索引：
利用单个索引值获取列表中的元素
切片作用：
利用索引范围返回多个元素的新列表
切片可以针对：列表，元组，字符串
切片特点：
切片返回的仍然是原数据类型
切片返回新的列表，不影响原列表
语法：
list1 = ['python', 'mysql', 'git', 'linux']
list1[start:end:step]
start:起始索引,默认0,可以为负数
end:结束索引，不过结束位置（左闭右开），可以为负数正数从左向右查，负数从右向左查
step:步长，默认为1，可以为负数。 负责方向：
"""
# TODO 正数
list1 = ['python', 'mysql', 'git', 'linux']
# ['python', 'mysql']
print(list1[0:2:1])
print(list1[0:2])
print(list1[:2])
print('--' * 20)

# ['python', 'git']
print(list1[:3:2])

# ['git', 'linux']
print(list1[2:])

# 复制这个列表
list2 = list1[:]
print(list2)

print('==' * 20)

# TODO 负数
list1 = ['python', 'mysql', 'git', 'linux']
# ['python', 'mysql']
print(list1[:2])
print(list1[-4:-2])

# ['git', 'linux']
print(list1[-2:])

# ['linux', 'git']
print(list1[-1:-3:-1])

# list.reverse()  # 改变原列表进行反转
# 列表反转，返回新的列表
print(list1[::-1])








