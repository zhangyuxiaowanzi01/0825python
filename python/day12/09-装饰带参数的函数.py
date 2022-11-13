# 定义装饰器
def wrapper(fn):
    def inner(*args, **kwargs):
        print('计算开始...')
        result = fn(*args, **kwargs)
        print('计算结束...')
        return result

    return inner


# 定义一个被装饰函数
@wrapper
def total(a, b):
    return a + b


@wrapper
def total1():
    return 1 + 1


print(total1())
print('==' * 20)

print(total(1, 2))
print(total(2, 2))
print(total(2, 3))
