"""
__new__魔术方法：
作用：创建类的实例并且返回
触发：创建类的对象的时候
"""


class Person(object):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


p1 = Person()
print(p1)

p2 = Person()
print(p2)
