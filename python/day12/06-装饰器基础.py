def fn2():
    # 开始时间
    print('fn2')
    # 结束时间
    # 结果 = 结束时间 - 开始时间


# 定义装饰器
# fn: 被装饰的函数
def wrapper(fn):
    def inner():
        print('前置扩展')
        fn()
        print('后置扩展')

    return inner


def fn1():
    print('fn1')


# 使用装饰器
fn1 = wrapper(fn1)
fn1()

# fn2 = wrapper(fn2)
# fn2()
