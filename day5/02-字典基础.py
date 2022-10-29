"""
结构：
简单写法（常用）： {key1:value1, key2:value2, ...}
函数写法: dict(key1=value1, key2=value2, ...)
key:不可变数据类型，一般都用字符串
value: 任何数据类型都可以
Why:
[xx, xx, xx, xx, xx]
[xx, xx, xx, xx, xx]
[[18, 18, xx, xx, xx], [xx, xx, xx, xx], [xx, xx, xx, xx]]
[
 {'name':'good', 'age':18, 'addr':'成都', 'number':18},
 {'name':'good', 'age':18, 'addr':'成都', 'number':18},
 {'name':'good', 'age':18, 'addr':'成都', 'number':18}
]
特点：
key是唯一的
key：value形式的数据结构
"""
dict1 = dict(a=1, b=2)
print(dict1)
