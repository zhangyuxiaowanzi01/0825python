import re

# TODO re.search(pattern, string[, flag])
# 在string中查找正则匹配的字符串,第一个匹配到的对象或者None.匹配到返回对象，匹配不到返回None
# 原字符
match_obj = re.search('hello', '你好hello world hello python')
# 匹配对象.group()  #提取匹配到的字符串
print(match_obj)
print(match_obj.group())
print('==' * 20)

# TODO re.findall(pattern, string[, flag])
# 列出字符串中模式的所有匹配项, 所有匹配到的字符串列表
match_list = re.findall('hello', '你好hello world hello python, hello')
print(match_list)
