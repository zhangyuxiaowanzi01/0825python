"""
语法：
#  B类继承A类
class A:
    pass

class B(A):
    pass
"""


# 员工类
class Staff:
    def __init__(self):
        self.name = 'hello'
        self.age = 18


# 老师类
class Teacher(Staff):
    pass


teacher = Teacher()
print(teacher.name)
print(teacher.age)
