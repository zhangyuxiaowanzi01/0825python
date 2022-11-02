"""
任何类型的大文件的复制
img, video, big
"""

# 接收要复制文件的文件名（完整）
import os

source_file = input('要复制文件的名称：')
# 通过源文件名构造目标文件名
source_filename, extension = os.path.splitext(source_file)
target_file = f'{source_filename}-副本{extension}'

# 打开源文件-rb
source_f = open(source_file, 'rb')
# 打开目标文件-wb
target_f = open(target_file, 'wb')

# 打开源文件进行读取1024byte
# 打开目标文件将读取的内容写入
while True:
    content = source_f.read(1024)
    if not content:
        break
    target_f.write(content)

# 关闭资源
source_f.close()
target_f.close()
