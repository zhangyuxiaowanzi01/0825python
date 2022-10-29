"""
配合for循环使用的语句：range
作用：生成一个范围的可迭代对象（list）
range(start, end, step)
start: 起始数，默认是0
end：截至数，不包括这个值。
step: 步长，默认1
"""
# while可以设置循环次数
# for用来遍历可迭代对象（str,list,tuple,dict）

# 输出1-10
for i in range(1, 11):
    print(i)
print('==' * 2)

# 输出1-10之间的奇数
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
print('==' * 20)

# 输出1-10之间的偶数
for i in range(2, 11, 2):
    print(i)

# 99乘法表(作业)

# range(1, 6)  # [1, 2, 3, 4, 5]
