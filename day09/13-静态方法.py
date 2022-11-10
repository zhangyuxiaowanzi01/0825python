class Person:
    @staticmethod
    def eat():
        print('吃饭')

    @staticmethod
    def run():
        print('跑')


# 类调用（一般用这种方式）
Person.eat()

# 对象调用
p1 = Person()
p1.eat()
