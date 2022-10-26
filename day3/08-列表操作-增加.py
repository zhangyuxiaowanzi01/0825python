# TODO list.insert(索引， 数据)
list1 = ['python', 'mysql']
# 在索引1的位置添加git
list1.insert(1, 'git')
print(list1)
# 在索引-2的位置添加linux
list1.insert(-2, 'linux')
print(list1)

# TODO list.append(数据)
# 将整个数据添加到列表末尾
list1.append('shell')
print(list1)

list1.append('mysql')
print(list1)

list1.append([1, 2, 3])
print(list1)
print('==' * 20)

# TODO list.extend(list|str)
# 将数据（list|str）中的元素依次添加到列表末尾
list2 = ['apple']
# 列表
list2.extend(['banana', 'orange'])
print(list2)

# str
list2.extend('abc')
print(list2)
