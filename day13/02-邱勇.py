import copy

dict1 = {'name': 'hello', 'age': 20}


def my_copy1(fn):
    def inner(*args):
        result = copy.copy(*args)
        return result

    return inner


@my_copy1
def my_copy(*args):
    copy.copy(*args)
    return copy.copy(*args)


print(id(my_copy(dict1)))
print(id(dict1))
