# TODO 普通修改
# {key:value}
# 通过key可以获取key对应的value
info = {'name': 'fine', 'age': 18}
# 语法（获取）：dict[key] 得到这个key对应的value
"""
print(info['name'])
print(info['age'])
"""
# 语法（修改）： dict[key]=new value
# key存在：就是修改
info['name'] = 'hello'
info['age'] = 28
print(info)

# key不存在，新增
info['addr'] = '成都'
print(info)
print('==' * 20)

# TODO dict.setdefault(key, value)
# key存在不设置新值，不存在才设置，并返回
info = {'name': 'fine', 'age': 18}
print(info.setdefault('name', 'good'))
print(info.setdefault('addr', '成都'))
print(info)
print('==' * 20)

# TODO dict1.update(dict2)
# 将字典2合并到字典1， 如果key相同，后面的会覆盖前面的
info1 = {'name': 'fine', 'age': 18}
info2 = {'name': 'good', 'age': 19, 'addr': '成都'}
info1.update(info2)
print(info1)
