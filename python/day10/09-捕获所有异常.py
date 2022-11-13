"""
语法：
try:
    可能发生异常的代码
except Exception as result:
    print(result)
"""

try:
    num = int(input('数字：'))
    result = 1 / num
except Exception as e:
    print(e)
