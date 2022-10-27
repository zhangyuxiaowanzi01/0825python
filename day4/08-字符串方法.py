# TODO 去除俩边空格
str1 = ' hello '
print(str1)
# str.strip()  # 去除俩边空格
print(str1.strip())
# str.lstrip() # left去除左边空格
print(str1.lstrip())
# str.rstrip() # right去除右边空格
print(str1.rstrip())
print('==' * 20)

# TODO 字符串分割
# 字符串转列表
str2 = 'hello world'
# str.split() 按照空格分割字符串为列表
print(str2.split())
# str.split(分割符) 按照空格分割字符串为列表
str3 = 'python,mysql,linux,git'
print(str3.split(','))
# str.split(分割符, 分割次数) 从左按照指定分隔符分割,分割指定的次数,返回一个列表
print(str3.split(',', 2))
# str.rsplit(分割符, 分割次数) 从右按照指定分隔符分割,分割指定的次数,返回一个列表
print(str3.rsplit(',', 2))
