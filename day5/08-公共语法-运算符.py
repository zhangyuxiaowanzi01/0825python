# TODO + str list tuple
# str
str1 = 'hello'
str2 = 'world'
print(str1 + str2)

# list
print([1, 2] + ['a', 'b'])

# tuple
print((1, 2) + ('a', 'b'))
print('==' * 20)

# TODO * str list tuple
# 注意：只能和正整数相乘
print('abc' * 2)
print([1, 2] * 2)
print((1, 2) * 2)

# TODO in语句
# 元素是否存在，在True， 不在False
# 数据：str list tuple dict
# 语法：item in 容器数据
str1 = 'hello'
print('he' in str1)

list1 = ['python', 'msyql']
print('python' in list1)

tuple1 = ('python', 'msyql')
dict1 = {'name': 'hello', 'age': 18}
print('hello' in dict1) #  True False
print('hello' in dict1.values()) #  True False
print('name' in dict1) #  True False

# TODO not in 语句 不在True， 在False
print('hello' not in dict1.values()) #  True False
