"""
在类的内部操作对象属性，本质就是在对象方法中操作对象属性，在self上来操作对象属性
"""


# 定义类
class Person:
    def set_name(self):
        # 设置属性
        self.name = 'hello'

    def get_name(self):
        print(self.name)

    def edit_name(self):
        self.name = 'good'

    def del_name(self):
        del self.name


p1 = Person()
# 调用对象方法
p1.set_name()  # 设置
p1.get_name()  # 获取
p1.edit_name()  # 修改
p1.get_name()  # 获取
p1.del_name()  # 删除
print(p1.name)
