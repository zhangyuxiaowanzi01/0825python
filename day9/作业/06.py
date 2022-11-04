"""
新建一个文件，定义一个计算类,有两个属性,数字1,数字2,具有 加 减 乘 除 方法
"""


class Computer:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


computer = Computer(10, 2)
print(computer.add())
print(computer.sub())
