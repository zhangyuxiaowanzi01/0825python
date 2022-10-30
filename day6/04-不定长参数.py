"""
不定长参数：
    可以传入任意多个参数
不定长参数类型：
    位置不定长: 可以接收任意多个位置参数，会以元组类型将所有位置参数打包在args变量中
    关键字不定长：可以接收任意多个关键字参数，会以字典类型将所有关键字参数打包在kwargs变量中
"""


# TODO 位置不定长参数
def fn1(*args):
    print(args)  # tuple


fn1(1, 'a', 'b', 'hello', 'xxx')


# TODO 关键字不定长参数
def fn2(**kwargs):
    print(kwargs)


fn2(a=1, b=2, c='hello')


# 混合使用
def fn3(*args, **kwargs):
    print(args)
    print(kwargs)


fn3(1, 2, 3, a=1, b=2, c=3)
