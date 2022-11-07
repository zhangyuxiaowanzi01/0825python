# 变量
name = 'module1'


# 函数
def fn():
    print('module1 fn函数')


# 类
class Demo:
    def __str__(self):
        return 'module1 中的Demo实例'


# 指定当前模块在import * 时，可以被导入的资源
# 注意：列表中写的时资源的字符串名称
__all__ = ['name', 'fn']
