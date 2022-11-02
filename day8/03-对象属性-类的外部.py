# 定义类
class Person:
    pass


# 创建对象
p1 = Person()

# TODO 设置对象属性
# 语法：obj.attr = value
p1.name = 'hello'
print(p1.name)

# TODO 修改对象属性
# 属性存在就是修改，不存在就是设置
# 语法：obj.attr = new_value
p1.name = 'apple'
print(p1.name)

# TODO 获取对象属性
print(p1.name)

# TODO 删除对象属性
del p1.name
print(p1.name)
