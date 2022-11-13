# 需求1：求1+1和的函数
# 定义
def sum1():
    result = 1 + 1
    print(result)


# 调用
sum1()


# 需求2：求1+2和的函数
# 定义
def sum2():
    result = 1 + 2
    print(result)


# 调用
sum2()


# 需求3：求2+3和的函数
# 定义
def sum3():
    result = 2 + 3
    print(result)


# 调用
sum3()


# TODO 参数
# 需求4： 求2个数的和
# 定义
def sum3(a, b):  # a,b 定义时写的参数叫做形式参数：形参
    result = a + b
    print(result)


# 调用
sum3(1, 1)  # 1,1 调用时传入的参数叫做实际参数：实参
sum3(1, 1)
sum3(1, 2)
sum3(2, 3)
sum3(100, 100)

# TODO 作用：
"""
通用性更强,满足多种情况
"""

# TODO 概念：
"""
定义时写入的参数叫做形式参数：形参
调用时传入的参数叫做实际参数：实参
"""
