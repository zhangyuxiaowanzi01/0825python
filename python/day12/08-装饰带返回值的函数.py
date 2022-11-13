# 定义装饰器
def wrapper(fn):
    def inner():
        print('计算开始...')
        result = fn()
        print('计算结束...')
        return result

    return inner


# 定义一个被装饰函数
@wrapper
def total():
    return 1 + 1


print(total())
