"""
索引：
利用单个索引值获取列表中的元素
切片作用：
利用索引范围返回多个元素的新列表
切片特点：
切片返回的仍然是原数据类型
切片返回新的列表，不影响原列表
语法：
list1 = ['python', 'mysql', 'git', 'linux']
list1[start:end:step]
start:起始索引,默认0,可以为负数
end:结束索引，不过结束位置（左闭右开），可以为负数
step:步长，默认为1，可以为负数
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

# 复制这个列表
list2 = list1[:]
print(list2)

