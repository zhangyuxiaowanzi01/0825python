"""
猫类：Cat
    属性：name，age
    方法：跑， 吃
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f'{self.name}跑')

    def eat(self):
        print(f'{self.name}吃')


cat = Cat('TOM', 2)
cat.run()
cat.eat()
