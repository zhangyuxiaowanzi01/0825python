class Person:
    country = '中国'

    # 类方法
    @classmethod
    def get_country(cls):
        print(cls.country)

    @classmethod
    def set_country(cls):
        cls.country = 'China'


# print(Person)
Person.get_country()
Person.set_country()
Person.get_country()
