"""
python编写一个聊天记录保存功能，不断获取用户输入信息，保存到record.log文件
"""

# 打开record.log - a
f = open('record.log', 'a', encoding='utf8')

while True:
    # 接收用户输入
    msg = input('输入信息：')
    if msg == 'quit':
        break
    f.write(msg + '\n')

f.close()
