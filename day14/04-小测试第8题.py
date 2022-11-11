class Cat:
    name = 'Tom'
    __age = 3

    def run(self):
        return self.name + ' 正在跑'

    def __listen(self):
        return self.name + ' 正在听'

# 私有成员
# _类名__私有成员
class Dog:
    name = 'XiaoHei'
    __age = 4

    def run(self):
        return self.name + ' 正在跑'

    def __watch(self):
        return self.name + ' 正在看'


class Zoo(Dog, Cat):

    def run(self):
        return super(Zoo, self).run()

    def animal(self):
        return super(Zoo, self)._Cat__listen()

    def fn1(self, num):
        self.age = num


if __name__ == '__main__':
    zoo = Zoo()
    print(zoo.animal())

