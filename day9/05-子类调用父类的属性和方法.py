class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('人类吃东西')


# TODO super指向当前的父类
class Teacher(Person):
    def __init__(self, name, age, num):
        super().__init__(name, age)
        self.num = num

    def eat(self):
        super().eat()
        print(f'{self.name}吃东西')


teacher = Teacher('hello', 18, 100)
print(teacher.name)
print(teacher.age)
print(teacher.num)

teacher.eat()
