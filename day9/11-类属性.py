"""
类属性属于整个类，可以通过类访问，也可以对象访问
"""


class Person:
    # 类属性
    country = '中国'


# 在类外部访问类属性
# 通过类名访问类属性
# 语法：类名.类属性名
print(Person.country)
p1 = Person()
print(p1.country)

# 修改
Person.country = 'China'
print(Person.country)
