"""
语法：
try:
    可能发生异常的代码
except Exception as result:
    发生异常执行的代码
else:
    没有异常的时候执行的代码
"""
try:
    num = int(input('数字：'))
    result = 1 / num
except Exception as e:
    print(e)
else:
    print('没有异常执行else代码块')
