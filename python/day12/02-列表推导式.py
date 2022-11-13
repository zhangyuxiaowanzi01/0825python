# 需求：列表中有1-100的元素 [1, 2, 3,...100]
"""
list1 = []
for i in range(1, 101):
    list1.append(i)

print(list1)
"""

# TODO 列表推导式
"""
说明：快速生成列表的表达式
特点：生成列表语法简洁，效率高。
语法：[生成元素的表达式 控制元素生成个数的表达式]
"""
# 需求1：列表中有1-100的元素 [1, 2, 3,...100]
list2 = [i for i in range(1, 101)]
print(list2)

# 需求2：生成1-10之间的奇数列表
# 第一种
list3_1 = [i for i in range(1, 11, 2)]
print(list3_1)

# 第二种
list3_2 = []
for i in range(1, 11):
    if i % 2 != 0:
        list3_2.append(i)
print(list3_2)

# 第三种
list3_3 = [i for i in range(1, 11) if i % 2 != 0]
print(list3_3)

# 需求3：['hello', 'hello', ...]
list4 = ['hello' for i in range(10)]
print(list4)

list5 = ['hello' + str(i) for i in range(10)]
print(list5)

list5 = [i ** 2 for i in range(10)]
print(list5)
print('==' * 20)

# 需求4：[(1, 1), (1, 2), (2, 1), (2, 2)]
# 传统
list6 = []
for i in range(1, 3):
    for j in range(1, 3):
        list6.append((i, j))
print(list6)
print('--' * 20)

# 列表推导式
list7 = [(i, j) for i in range(1, 3) for j in range(1, 3)]
print(list7)
