"""
f.write(content) 一次性写入内容
f.writelines(list) 一次性写入多行
"""

# TODO f.write(content) 一次性写入内容
"""
f = open('resource/demo4.txt', 'w', encoding='utf8')
f.write('123\n')
f.write('456\n')
f.write('789\n')
f.close()
"""

# TODO f.writelines(list) 一次性写入多行
f = open('resource/demo5.txt', 'w', encoding='utf8')
f.writelines(['123\n', '456\n', '789\n'])
f.writelines(['123\n', '456\n', '789'])
f.close()
