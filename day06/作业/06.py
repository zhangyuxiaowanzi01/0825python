"""
封装函数，设计根据QQ和密码登录的过程(QQ和密码预设为指定的值).
执行结果为登录是否成功(boolean类型的值)
"""


def login():
    # 设置账号密码
    account = '123'
    password = '123'

    # 接收用户输入
    user_account = input('账号：')
    user_password = input('密码：')

    # if account == user_account and password == user_password:
    #     return True
    # else:
    #     return False
    return account == user_account and password == user_password


print(login())
