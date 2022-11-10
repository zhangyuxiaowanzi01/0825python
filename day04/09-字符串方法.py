# TODO 去除俩边空格 strip()
str1 = ' hello '
print(str1)
# str.strip()  # 去除俩边空格
print(str1.strip())
# str.lstrip() # left去除左边空格
print(str1.lstrip())
# str.rstrip() # right去除右边空格
print(str1.rstrip())
print('==' * 20)

# TODO 字符串分割 split()
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
print('==' * 20)

# TODO 大小写转化  upper() lower()
str1 = 'hello python'
# 字符串转化为大写
str2 = str1.upper()
print(str2)

# 字符串转化为小写
print(str2.lower())

# 单词首字母大写
print(str1.title())
print('==' * 20)

# TODO 判断字符串开头或者结尾 startswith()  endswith()
# 判断开始
str1 = 'hello python'
print(str1.startswith('he'))
print(str1.startswith('le'))
# 判断结尾
print(str1.endswith('python'))
print(str1.endswith('pythof'))
# 举例：判断文件是不是.txt
print(str1.endswith('.txt'))

# TODO 变量格式化输出 format()
# f格式化， %格式化
name, age, address = 'hello', 11, '成都'
str1 = '姓名：{}, 年龄：{}, 地址：{}'.format(name, age, address)
str1 = '地址：{2},姓名：{0}, 年龄：{1}'.format(name, age, address)
str1 = '地址：{c},姓名：{a}, 年龄：{b}'.format(a='apple', b=18, c='高天')
print(str1)
print('==' * 20)

# TODO 字符串拼接 join()
# str.join(列表) 列表转字符串
list1 = ['python', 'mysql', 'linux']
print('|'.join(list1))
print(','.join(list1))
print(''.join(list1))
print(' '.join(list1))
print('+'.join(list1))

# TODO 字符串替换 replace()
# str.replace(原内容, 新内容)  # 返回替换之后的新字符串
str1 = 'hello world'
print(str1.replace('world', 'python'))
print('==' * 20)

# TODO 判断“数据类型”的方法 isdigit() isalpha() isalnum()
str1 = '11'
str2 = 'aa'
str3 = 'aa11'
# 判断字符串由数字组成
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())
print('--' * 20)
# 判断字符串由字母组成
print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())
print('--' * 20)
# 判断字符串由字母数字组成,包括一个就行
print(str1.isalnum())
print(str2.isalnum())
print(str3.isalnum())
print('--' * 20)
