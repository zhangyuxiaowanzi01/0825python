class Person:
    def __init__(self):
        self.name = 'hello'
        self.age = 18

    def eat(self):
        print(f'{self.name}吃东西')


class Teacher(Person):
    def __init__(self):
        self.name = 'good'
        self.age = 28

    def eat(self):
        print(f'{self.name}吃东西')


teacher = Teacher()
teacher.eat()
