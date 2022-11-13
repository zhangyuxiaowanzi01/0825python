class Demo:
    @staticmethod
    def range():
        return range(4)


tuple1 = ('python', 'git', 'mysql', 'linux')


def fn(index):
    return tuple1[index]


list1 = [fn(i) for i in Demo.range()]
print(list1)
