"""
语法:
# 第一种
try:
    可能发生异常的代码
except (异常的类型1, 异常类型2, ...):
    捕获异常执行的代码

# 第二种
try:
    可能发生异常的代码
except 异常类型1:
    发生异常1,执行的代码
except 异常类型2:
    发生异常2,执行的代码
except ...:
    pass
"""
# TODO 第一种
# try:
#     num = int(input('数字:'))
#     result = 1 / num
# except (ZeroDivisionError, ValueError):
#     print('0不能是除数')

# TODO 第二种
try:
    num = int(input('数字:'))
    result = 1 / num
except ZeroDivisionError:
    print('0不能是除数')
except ValueError:
    print('输入的不能是非数字')
