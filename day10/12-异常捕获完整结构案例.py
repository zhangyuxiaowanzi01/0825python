"""
需求：读取文件内容
1. 文件不存在，报错。捕获，然后创建这个文件。
2. 文件存在，直接读取
"""
try:
    f = open('resource/demo.txt', 'r', encoding='utf8')
except FileNotFoundError as e:
    f = open('resource/demo.txt', 'w', encoding='utf8')
else:
    print(f.read())
finally:
    print(1111)
    f.close()


# FileExistsError
# FileNotFoundError