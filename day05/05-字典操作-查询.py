# TODO dict[key]
# 根据key查询对应的值，key不存在则抛出错误
info = {'name': 'fine', 'age': 18}
# 存在
print(info['name'])
# 不存在
# print(info['addr'])
print('==' * 20)

# TODO dict.get(key [, default=None])
# 根据key查询对应值，key不存在，返回default的值，default默认是None
info = {'name': 'fine', 'age': 18}
# 存在
print(info.get('name'))
# 不存在
print(info.get('addr'))
print(info.get('addr', '成都'))
print('==' * 20)

# TODO len(dict) 通用方法：str，list，tuple，dict, set
print(len(info))
print('==' * 20)

# TODO 获取key，获取value， 获取key和value
# dict.keys()
info = {'name': 'fine', 'age': 18}
print(info.keys())

# dict.values()
print(info.values())

# dict.items()
print(info.items())
