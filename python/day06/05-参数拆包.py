def fn1(a, b, c):
    print(a, b, c)


list1 = [1, 2, 3]
tuple1 = ('a', 'b', 'c')
fn1(list1[0], list1[1], list1[2])

# TODO 列表，元组拆包
fn1(*list1)
fn1(*tuple1)
print('==' * 20)

# TODO 字典拆包
dict1 = {'a': 1, 'b': 2, 'c': 3}
fn1(**dict1)
