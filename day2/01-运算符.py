# TODO 算术运算符
# % 取模
a = 10
b = 2
print(a % b)
print('==' * 20)

# ** 取幂值
print(a ** b)
print(a ** 3)
print(2 ** 4)
print('==' * 20)

# // 整除, 得到整数
# / 除法，得到浮点数
print(a / b)
print(a // b)
print(11 // 2)
print('==' * 20)

# TODO 比较运算符
# == 比较俩个值相等
m = 'hello'
n = 'hello1'
print(m == n)

# != 比较俩个值不相等
print(m != n)
print('==' * 20)

# TODO 赋值运算符
# =
x = 1
y = 2

# +=
y += x  # y = y + x 3
y += 1  # y = y + 1 4
y += 2  # y = y + 2 6

# -=
y -= 1  # y = y - 1 5
print(y)

# //=
y //= 2  # y = y // 2 2
print(y)

# %=
y %= 2  # y = y % 2 0
print(y)
print('==' * 20)

# 身份运算符
x = 'hello'
y = 'hello1'
print(x is y)  # False
print(x is not y)  # True
