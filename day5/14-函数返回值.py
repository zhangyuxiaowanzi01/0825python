# TODO 函数返回值
"""
语法：
def 函数名([参数列表]):
    函数体
    return 表达式结果
说明：
    return返回函数结果
    return后面的代码不在执行
    函数在哪儿调用，函数结果就返回在哪儿
关于函数返回None的情况：
    1. return None
    2. return
    3. 函数体中没有return
"""


# 需求1： 返回俩个数求和的结果
# 定义
def sum1(a, b):
    result = a + b
    return result
    print(result)


# 调用
print(sum1(1, 2))

# data = sum1(1, 2)
# print(data)
