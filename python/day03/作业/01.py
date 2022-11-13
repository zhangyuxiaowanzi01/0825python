"""
提示⽤户输⼊：姓名、公司、职位、电话、公司地址
按照以下格式输出
"""
# 输入
name = input('name:')
phone = input('phone:')
job = input('job:')
company = input('company:')

# 输出
# 第一种
"""
print('**'*20)
print(f'姓名：{name} \t 电话：{phone}')
print(f'职位：{job} \t 公司：{company}')
print('**'*20)
"""

# 第二种
info = f"""
{'**'*20}
姓名：{name} \t 电话：{phone}
职位：{job} \t 公司：{company}
{'**'*20}
"""
print(info)
