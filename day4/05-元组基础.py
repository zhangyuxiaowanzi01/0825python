# TODO 元组结构 tuple
# 简单方式（常用）
t1 = ()
t2 = ('a', 1, 1.1, True, [1, 2], ('hello', 'good'))
print(type(t1))
print(type(t2))
t3 = ("hello")
# 注意：只有一个元素的情况下，后面必须要有逗号，否则就是一个普通数据
print(type(t3))
print('==' * 20)

# 函数方式
t4 = tuple('hello')
print(t4)
t5 = tuple(['python', 'mysql', 'linux'])
print(t5)
l1 = list(t5)
print(l1)
print('--' * 20)

# 下标使用
print(t2[1])

# 切片使用
print(t2[:3])

# TODO 元组特点
"""
1. 元组中可以放任何数据类型
2. 元组也是有序的，可以通过下标获取元素
3. 通过切片获取新的子元组，和列表相同
4. 元组不可以修改(和列表的区别)
"""

# t2[0] = 'aaaa'   # 元组不能修改
# print(t2)
print('--' * 20)
t2[-2][0] = 100
print(t2)
