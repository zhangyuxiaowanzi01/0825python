# list tuple str
# TODO 索引
str1 = 'hello'
print(str1[-1])
print(str1[-2])
# str1[-1] = 'a'   # 字符串不能修改
print('==' * 20)

# TODO 切片
print(str1[::-1])
print(str1[:])
print('==' * 20)

# TODO 遍历
# while
i = 0
while i < len(str1):
    print(str1[i])
    i += 1
print('--' * 20)

# for
for char in str1:
    print(char)

print('==' * 20)
# TODO 数据类型（可变不可变）：
# 可变数据类型
"""
list
"""
# 不可变数据类型
"""
int,float
str
tuple
bool
None
"""
