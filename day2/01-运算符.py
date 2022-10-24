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

# TODO 身份运算符
x = 'hello'
y = 'hello1'
print(x is y)  # False
print(x is not y)  # True

# 查看内存地址
print(id(x))
print(id(y))
print(id('hello'))
print('==' * 20)

# TODO 逻辑运算符
# and 并且，and俩边都为都为True，那么这个表达式的结果就是True，否则就是False
print(True and True)
print(True and False)
print(False and True)

# or 或者， or俩边只有由一个是True，那么这个表达式结果就是True，否则就是False
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# not 取反
print(not False)
print(not True)
print('==' * 20)

# 短路
# False: 0 '' None [] {} ()
# and
print(1 and 2)  # 2
print('hello' and '100')  # '100'
print(0 and 100)  # 0
print(None and 0)  # ''
print('==' * 20)

# or
print(1 or 2)  # 1
print('hello' or '100')  # 'hello'
print(0 or 100)  # 100
print(None or 0)  # 0

# not
print(not 1)
print(not 0)
print(not '')
print(not None)
print(not '0')

# TODO 运算符优先级
print(1 + 1 and 2 - 2)
print((1 + 1) and (2 - 2))  # 为了可读性更好，增加括号
print((1 + 2) * 3)
