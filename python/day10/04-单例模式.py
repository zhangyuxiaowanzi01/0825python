"""
单例模式：
一个类只创建一个对象
"""


class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance


s1 = Singleton()

s2 = Singleton()

s3 = Singleton()

print(s1)
print(s2)
print(s3)
