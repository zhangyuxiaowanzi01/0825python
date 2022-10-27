# TODO 定义集合 set
# 简单方式
set1 = {'python', 'mysql', 'linux'}
print(type(set1))

# 注意：{}表示字典，不是集合
# 函数方式
set2 = set('hello')
set3 = set(['python', 'mysql', 'linux'])
set4 = set(('python', 'mysql', 'linux'))
print(set2)
print(set3)
print(set4)

# 集合特点：
# 1. 集合是无序的，没有索引
# 2. 集合元素是唯一的。去重。
