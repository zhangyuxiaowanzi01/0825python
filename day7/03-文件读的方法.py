"""
f.read([n])
    1. 不写参数，一次性读取所有内容
    2. 写参数
        2.1 如果是普通模式，n就是字符个数
        2.2 如果是二进制模式,n就是字节个数
f.readline()
    读取一行
f.readlines()
"""
# TODO f.read([n])
# 打开文件-普通模式
"""
f = open('resource/demo1.txt', 'r', encoding='utf8')
print(f.read(3))
f.close()
"""
# 打开文件-二进制模式
"""
f = open('resource/demo1.txt', 'br')
content = f.read(7)
# 二进制类型转化为str
print(content)
# print(content.decode())
f.close()
"""

# TODO f.readline() 按行读取内容
"""
f = open('resource/demo1.txt', 'r', encoding='utf8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
f.close()
"""

# TODO f.readlines() 一次性读取所有行，返回列表。列表中每个元素就是一行
f = open('resource/demo1.txt', 'r', encoding='utf8')
content_list = f.readlines()
print(content_list)
f.close()
