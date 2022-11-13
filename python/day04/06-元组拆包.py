# 定义一个元组
info = ('hello', 18, '成都省高天市')
# 元组拆包
name, age, address = info
print(name, age, address)

# 列表拆包
name, age, address = list(('hello', 18, '成都省高天市'))
print(name, age, address)

a, b, c = '123'
print(a, b, c)

# 注意：
# 变量个数和后面的元素个数要一一对应
