"""
object是内置类，默认所有类都继承自object
"""


# 一般用这种方式
class A:
    pass


class B():
    pass


class C(object):
    pass


# python3之前的叫法
# 新式类
class D(object):
    pass


# 老式类
class E():
    pass
