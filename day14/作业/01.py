# 实现匹配邮箱的正则
import re

# xxxx@163.com xxxx@189.cn xxx@gmail.com xxx@qq.com xxxx@.com.cn
# 账号：3 - 20
# @：@
# 域名：数字或者.com .cn .org .dev .edu .us 5 .com.cn
email = input('email:')
re_str = '^\w{2,20}@[a-z0-9A-Z]{1,25}\.[a-z]{2,5}(\.[a-z]{2,5})?$'
if re.search(re_str, email, re.I):
    print('邮箱格式正确')
else:
    print('邮箱格式错误')
