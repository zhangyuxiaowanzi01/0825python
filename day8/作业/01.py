"""
根据录入文件名,复制出来一个新的文件,新的文件名为:原文件名-副本.源文件后缀
"""
import os

# 打开源文件
f = open('demo.txt', 'r', encoding='utf8')
# 读取源文件的内容
content = f.read()
# 关闭源文件
f.close()

# 通过源文件名称，构造目标文件名称
filename, extension = os.path.splitext('demo.txt')
target_file = filename + '-副本' + extension
# 打开目标文件
f = open(target_file, 'w', encoding='utf8')
# 将源文件的内容写入目标文件
f.write(content)
# 关闭目标文件
f.close()
