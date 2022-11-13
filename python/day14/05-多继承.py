# 单继承
# 子类重写父类的属性和方法
# 子类调用父类的属性和方法

class A:
    def info(self):
        super(A, self).info()  # C.info()
        print('a')


class C:
    def info(self):
        print('c')


class B(A, C):
    def info(self):
        super().info()  # super(B, self).info()  # A.info()
        print('b')


# MRO查找原则
print(B.__mro__)

b = B()
b.info()
