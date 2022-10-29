"""
写一个后期网络聊天项目的模块，用户不断从键盘输入，每次输入回车后，
将打印用户输入的字符个数和内容，当用户输入quit后，退出该功能
"""

while 1:
    msg = input('输入信息：')
    if msg == 'quit':
        break
    print(msg)
