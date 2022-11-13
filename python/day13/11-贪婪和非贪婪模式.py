import re

# TODO 贪婪模式 默认
"""
print(re.search('\w+go', '你好123goodgo'))
"""

# TODO 非贪婪模式  \w   {1,}
"""
# 贪婪
print(re.search('你\w+', '你好kfjsdklsfdjklfjadslkjfksdl'))
# 非贪婪
print(re.search('你\w+?', '你好kfjsdklsfdjklfjadslkjfksdl'))
# 贪婪
print(re.search('\w+', '你好kfjsdklsfdjklfjadslkjfksdl'))
# 非贪婪
print(re.search('\w+?', '你好kfjsdklsfdjklfjadslkjfksdl'))
"""

# 案例
str1 = '<html><head></head><body><h1>标题</h1></body></html>'
# 贪婪
print(re.search('<.+>', str1))
# 非贪婪
print(re.search('<.+?>', str1))
