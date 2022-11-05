"""
语法：
try:
    可能发生异常的代码
except 异常的类型:
    捕获到异常执行的代码
"""

try:
    num = int(input('输入数字'))
    result = 1 / num
except ZeroDivisionError:
    print('0不能作为除数使用')

print('hello python')
