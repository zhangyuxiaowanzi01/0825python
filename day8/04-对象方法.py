"""
对象是由属性和方法构成的
语法：
class ClassName:
    # 属性方法
    def 方法名(self):
        代码块
说明：
    定义的位置不同：需要定义在类中
    必须要有一个参数：self
    调用方式不同：obj.fn()
    除以上，其他一切和函数相同
self:
    调用对象方法的当前对象
    python解释器会自动把调用这个方法的对象传入到方法的self中
"""


# 定义类
class Person:
    # TODO 定义对象方法
    def eat(self):
        print(self)
        print(self.name + '吃串串')


# 创建对象
p1 = Person()
p1.name = 'hello'
print(p1)
# TODO 调用对象方法
# 语法：obj.fn()
p1.eat()
print('==' * 20)

p2 = Person()
p2.name = 'good'
print(p2)
p2.eat()
