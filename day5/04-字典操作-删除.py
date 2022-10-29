# TODO del dict[key]
info = {'name': 'fine', 'age': 18}
del info['age']
print(info)
print('==' * 20)

# TODO dict.pop(key)
# 删除指定key对应的数据并返回，key不存在抛出错误
info = {'name': 'fine', 'age': 18}
# 存在
print(info.pop('age'))
print(info)
# info.pop('age')
print('==' * 20)

# TODO dict.clear()
# 清空字典
info = {'name': 'fine', 'age': 18}
info.clear()
print(info)
