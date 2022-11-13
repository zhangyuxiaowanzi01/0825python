"""
print('BAAAAAAAAAAAAAAAAAAAAAAAA')
print('BAAAAAAAAAAAAAAAAAAAAAAAA')
print('BAAAAAAAAAAAAAAAAAAAAAAAA')
print('BAAAAAAAAAAAAAAAAAAAAAAAA')
print('BAAAAAAAAAAAAAAAAAAAAAAAA')
print('AAAAAAAAAAAAAAAAAAAAAAAAA')
print('AAAAAAAAAAAAAAAAAAAAAAAAA')
"""

# 变量
# 语法：
# 变量名 = 变量值
a = 'BAAAAAAAAAAAAAAAAAAAAAAA'
# 说明：
# 把AA这个字符串 赋值 给变量a
print(a)
print(a)
print(a)
print(a)
print(a)
print(a)

# 标识符
# 变量名就是个标识符
# 在python中所有代码子的东西都叫做标识符。 函数名， 类名， 模块名， 包名
# 标识符的命名
# 1.由字母数字下划线组成，不能以数字开头
# 2.区分大小写
# 3.不能使用python的关键字

# python的关键字
import keyword

print(keyword.kwlist)

false = 'good'
# False = 'hello'

# 小驼峰
helloWorld = 'aaa'
# 大驼峰
HelloWorld = 'bbb'
# 下划线拼接
hello_world = 'ccc'

print('==' * 20)

# 变量的操作
# 增删改查
name = '邱勇'
# 改
name = '廖坤林'
# 查：使用
print(name)
# 删
del name
print(name)
