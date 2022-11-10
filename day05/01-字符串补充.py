# TODO str.index('子字符串')
# 查找子字符串在字符串中出现的位置（下标）,找不到抛出错误
str1 = 'hello'
print(str1.index('el'))  # 找到返回索引位置
# print(str1.index('le')) # 找不到抛出错误
print('==' * 20)

# TODO str.find('子字符串')
# 查找子字符串在字符串中出现的位置（下标）,找不到返回-1
print(str1.find('el'))  # 找到返回索引位置
print(str1.find('le'))  # 找不到抛出错误