# 查询
# list[索引] 通过索引获取元素
list1 = ['python', 'mysql', 'git']
print(list1[1])
print(list1[-2])

# list.index(数据) 查询数据第一次出现的索引，查询不到抛出错误
list1 = ['python', 'mysql', 'git', 'mysql']
print(list1.index('mysql'))
# list1.index('linux')  # 询不到抛出错误

# len() 通用方法，用来查询容器数据的长度
print(len(list1))
print(len('hello'))

# list.count(元素) 根据元素获取元素在列表中出现的次数
print('mysql个数：', list1.count('mysql'))
print('python个数：', list1.count('python'))



# 修改
# 语法：list[下标] = value
list1[0] = 'java'
print(list1)
