"""
需求：
1.程序启动，提示用户登录或者注册
2.选择注册->要求输入用户名和密码->返回注册提示信息
3.选择登录->要求输入用户和密码->判断是否登录成功
4.防止重复注册（自己完成）
"""
"""
分析：
注册：
username,password -> 保存-> 文件
内容在文件中的格式：
username,password
username,password
登录：
username,password
和系统中（文件保存的数据）username和password做对比
比对通过，Ok
不通过，Fail
"""
while True:
    # 接收用户输入选择功能
    code = input('选择功能[1注册|2登录]：')
    if code == '1':
        # 注册
        # 接收用户注册信息
        username = input('username:')
        password = input('password:')

        # 写入到文件中
        # 打开文件-a
        f = open('resource/user.txt', 'a', encoding='utf8')
        # 操作文件
        f.write(f'{username},{password}\n')
        # 关闭文件
        f.close()
        print(f'[{username}]用户注册成功')
    elif code == '2':
        # 登录
        # 接收用户登录信息
        username = input('username:')
        password = input('password:')

        # 打开文件-r
        f = open('resource/user.txt', 'r', encoding='utf8')
        user_list = f.readlines()  # ['username,password\n', 'username,password\n']
        f.close()
        for userinfo in user_list:
            # 去除用户信息字符串中的\n
            userinfo = userinfo.rstrip('\n')
            sys_username, sys_password = userinfo.split(',')  # ['11', '11']
            if username == sys_username and password == sys_password:
                print('登录成功')
                break
        else:
            print('登录失败')
    else:
        print('没有此功能')
        break
