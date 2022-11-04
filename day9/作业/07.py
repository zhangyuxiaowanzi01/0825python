"""
定义一个高级字符串工具类
具有如下方法:
将给定字符串反转（传入abcd返回dcba）
"""


class Tools:
    def reverse(self, string):
        return string[::-1]


tools = Tools()
print(tools.reverse('hello'))
