"""
私有成员：具有私有权限的属性和方法
私有权限：只能在类的内部访问

# 语法：
私有属性: __attr
私有方法: __fn()
"""


class Person:
    def __init__(self):
        # 私有属性
        self.__name = 'hello'

    def get_name(self):
        print(self.__name)

    def __fn(self):
        print('fn')


p1 = Person()
p1.get_name()


# TODO 在类的外部访问私有属性 - 不能
# print(p1.__name)
# p1.__fn()


# 在派生类中
class Student(Person):
    def get_name(self):
        print(self.__name)  # 调用不到
        self.__fn()  # 调用不到


# TODO 在派生类中访问私有属性 - 不能
s1 = Student()
s1.get_name()
