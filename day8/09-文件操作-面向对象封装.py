"""
文件操作步骤
1. 打开文件
2. 操作文件
3. 关闭文件

类名：File
    方法：
        init：创建文件句柄：   self.f = open(xx)
        read
        write
        del: self.f.close()
"""


class File:
    def __init__(self, filename, mode, encoding=None):
        # 打开文件
        file_path = 'resource/' + filename
        self.f = open(file_path, mode, encoding=encoding)

    def read(self):
        return self.f.read()

    def write(self, content):
        self.f.write(content)

    def __del__(self):
        self.f.close()


# 调用
file = File('demo.txt', 'w', encoding='utf8')
# 写入方法
file.write('123\n456')
