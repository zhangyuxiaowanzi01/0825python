"""
魔术方法：__del__
触发：当对象被销毁时触发del方法执行
作用：对象在销毁时，做一些收尾工作
"""


# 定义类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __del__(self):
        print('del执行')


# 创建对象
p1 = Person('fine1', 19)
# del p1
