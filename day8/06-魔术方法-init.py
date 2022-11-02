"""
魔术方法：__init__
触发：当创建对象以后，init自动执行
作用：初始化对象属性
说明：以后对象属性的初始化，都在init方法中设置
"""


# 定义类
class Person:
    def __init__(self, name, age):
        print('init')
        self.name = name
        self.age = age


# 创建对象
p1 = Person('hello', 18)  # 人的实例
print(p1.name)
print(p1.age)

p2 = Person(name='good', age=18)
print(p2.name)
print(p2.age)
