"""
使用if，编写程序，实现以下功能：
从键盘获取用户名、密码
如果用户名和密码都正确（预先设定一个用户名和密码），
那么就显示“欢迎进入xxx的世界”，否则提示密码或者用户名错误
"""
# 预先设定一个用户名和密码
sys_name = 'admin'
sys_pass = '123456'

# 接收用户输入
username = input('用户名：')
password = input('密 码：')

# 根据用户输入的用户名密码和系统的用户名密码做比对
if username == sys_name and password == sys_pass:
    print(f'欢迎进入{username}的世界')
else:
    print('密码或者用户名错误')
