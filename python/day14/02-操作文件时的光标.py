# 打开文件-w
f = open('resource/demo.txt', 'w+', encoding='utf8')
# 写入内容
f.write('你好 job1')
f.write('good job2')
f.write('good job3')

# TOOD 移动光标
f.seek(0)

# 读取文件
content = f.read()
# 关闭文件
f.close()

print(content)
