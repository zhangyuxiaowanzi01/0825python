"""
类属性，可以通过类访问，也可以通过对象访问
"""


class Person:
    # 类属性
    __country = 'China'

    def get_country(self):
        print(self.country)

    @classmethod
    def set_country(cls, name):
        if name == 'China':
            cls.__country = name
        elif name == '中国':
            cls.__country = name
        else:
            print('Fail')


p1 = Person()
p1.get_country()
