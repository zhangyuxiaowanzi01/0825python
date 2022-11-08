# 定义装饰器
def wrapper(fn):
    def inner():
        # 前置扩展
        print('前置扩展')
        fn()
        # 后置扩展
        print('后置扩展')

    return inner


# TODO 装饰器的语法糖形式
# 语法：在被装饰函数上添加@装饰器的名称
# wrapper装饰器对demo1函数进行装饰
@wrapper
def demo1():  # demo1 = wrapper(demo1)
    print('demo1')


demo1()
