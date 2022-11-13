"""
1. 在函数嵌套(函数里面再定义函数)的前提下
2. 内部函数使用了外部函数的变量(还包括外部函数的参数)
3. 外部函数返回了内部函数

函数可以当作参数被传入，也可以当作返回值被返回
"""


# 闭包
def wrapper1():
    num = 100

    def inner():
        print(num)

    return inner


def wrapper2(num):
    def inner():
        print(num)

    return inner
