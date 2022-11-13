import re

# TODO re.I Ignore
# 不设置re.I
print(re.search('Hello', 'hello world'))
# 设置re.I
print(re.search('Hello', 'hello world', re.I))
print('==' * 20)

# TODO re.S Space
# 不设置re.S
print(re.search('hello.world', 'hello\nworld'))
# 设置re.S
print(re.search('hello.world', 'hello\nworld', re.S))
