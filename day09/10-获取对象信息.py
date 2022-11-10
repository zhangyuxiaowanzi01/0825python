# ● type  查看数据类型
print(type('string'))


class Person:
    pass


class Goods:
    pass


goods = Goods()

p1 = Person()
p1.name = 'hello'
print(type(p1))
print('==' * 20)

# ● dir  查看对象上所有方法和属性
print(dir(p1))
print('==' * 20)

# ● isinstance(obj, class)  查看对象是否属于某个类. True|False
print(isinstance(p1, Person))
print(isinstance(goods, Person))
print(isinstance('hello', str))
