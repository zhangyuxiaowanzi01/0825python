"""
for 临时变量 in 可迭代对象:
    临时变量
说明：
字典如果没有指明操作的是key还是value，默认使用的是key
"""

info = {'name': 'fine', 'age': 18}
# TODO key
# 第一种
for key in info.keys():
    print(key)
print('--' * 20)
# 第二种
for key in info:
    print(key)
print('==' * 20)

# TODO value
for value in info.values():
    print(value)
print('==' * 20)

# TODO key, value
# 拆包
for key, value in info.items():
    print(key, value)
