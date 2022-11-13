"""
模块里面具有 三个类
厨师: 炒菜方法
服务员: 接待客人方法  送走客人方法
收银员: 收钱方法
客人来-->服务员接待-->客人点菜-->厨师炒菜-->客人吃完了-->收营员收钱-->服务员送客
"""


# 厨师
class Cook:
    def cooking(self):
        print('炒菜')


# 服务员
class Waiter:
    def server(self):
        print('接待客人')

    def send(self):
        print('送走')


# 收营员
class Cashier:
    def money(self):
        print('收钱')


print('客人来')
# Waiter().server()
Waiter.server(Waiter())
