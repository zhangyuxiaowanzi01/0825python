class Person:
    def __init__(self):
        # 受保护权限
        self._name = 'hello'
        # 私有权限
        self.__age = 18


class Staff(Person):
    def get_name(self):
        print(self._name)


staff = Staff()
staff.get_name()

# print(staff._name)

person = Person()
print(person._name)

# 私有权限也可以直接访问
# 私有权限：_类名__私有权限名字
print(person._Person__age)


