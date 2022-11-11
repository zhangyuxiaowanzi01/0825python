import re

# 实现匹配身份证号正则
code = input('code:')

print(re.search('^\d{17}[0-9x]$', code, re.I))
