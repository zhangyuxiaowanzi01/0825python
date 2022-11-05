"""
定义一个文件操作类File，方法有：读取所有内容，读取数据按行返回，写入内容，追加数据。
有以下类方法：
File.read(文件名)
File.write(文件名,’内容’)
File.readlines(文件名)
File.append(文件名,’内容’)
"""
import time


class File:
    @staticmethod
    def read(filename):
        """读取所有内容"""
        # 打开文件
        f = open(filename, 'r', encoding='utf8')
        # 读取文件
        content = f.read()
        # 关闭文件
        f.close()
        return content

    @staticmethod
    def write(filename, content):
        """写入内容"""
        # 打开文件-w
        f = open(filename, 'w', encoding='utf8')
        # 写入操作
        f.write(content)
        # 关闭文件
        f.close()
        print('写入成功')

    @staticmethod
    def readlines(filename):
        """读取数据按行返回"""
        f = open(filename, 'r', encoding='utf8')
        line_list = []
        while True:
            line_content = f.readline()
            if not line_content:
                break
            line_list.append(line_content)
        return line_list

    @staticmethod
    def append(filename, content):
        """追加数据"""
        # 打开文件-a
        f = open(filename, 'a', encoding='utf8')
        f.write(content)
        f.close()
        print('追加写入成功')


File.write('demo.txt', '123\n456\n789')
print('==' * 20)
time.sleep(1)
print(File.read('demo.txt'))
print('==' * 20)
time.sleep(1)
print(File.readlines('demo.txt'))
print('==' * 20)
time.sleep(1)
File.append('demo.txt', '\nabc')
print('==' * 20)
time.sleep(1)
print(File.read('demo.txt'))
