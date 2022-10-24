# 1. 写出变量名字，可以由哪些字符组成。

# 2. 写出变量命名时的规则。

# 3. 变量的作用是什么？什么时候需要使用变量？

# 4. 说出什么是驼峰法（大驼峰、小驼峰）， 举例说明
# 大驼峰
# 小驼峰
# 下划线拼接

# 5. 编写一个python程序
# A. 要求用户输入数据
# B. 打印输出数据的类型
"""
data = input('请输入数据：')
print(type(data))
"""


# 1. 编写1个python程序，完成以下要求
# A. 从键盘获取用户的姓名、性别、家庭地址
# B. 使用一个print输出： 姓名，男，地址：
"""
name = input('name:')
gender = input('gender:')
address = input('address:')

print('姓名：', name, '性别：', gender, '地址：', address)
"""

# 1. 分析以下代码为什么会报错？翻译报错信息。
# print(a)  # a: 标识符
# print(a)


# 1. 分析以下代码为什么会报错？翻译报错信息
# print(a  # 语法错误  syntaxError

# 1. 编写1个python程序，完成以下要求：
# A. 获取用户输入的两个数字
# B. 对获取的两个数字进行求和运行，并输出相应的结果

num1 = int(input('num1:'))
num2 = int(input('num2:'))

print(num1 + num2)

"""
# 数据类型转换
num1_int = int(num1)   # '11'  '11.1'  'abc' '11a'
num2_int = int(num2)

result = num1_int + num2_int
print(result)
"""

