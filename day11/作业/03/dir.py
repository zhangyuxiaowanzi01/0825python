"""
创建目录
删除目录（空目录或非空目录）
查找目录中是否存在某个文件
"""
import os
import shutil


class Directory:
    @staticmethod
    def mkdir(dirname):
        """创建目录"""
        os.mkdir(dirname)

    @staticmethod
    def rm_dir(dirname):
        """删除目录（空目录或非空目录）"""
        # os.rmdir()  # 只能删除空目录
        shutil.rmtree(dirname)  # 可以删除非空目录

    @staticmethod
    def is_file_in_dir(dirname, filename):
        resource_list = os.listdir(dirname)
        return filename in resource_list


# 创建目录
# Directory.mkdir('dir1')
# 删除目录（空目录或非空目录）
# Directory.rm_dir('dir1')

# 查找目录中是否存在某个文件
print(Directory.is_file_in_dir('dir1', 'demo.txt'))
print(Directory.is_file_in_dir('dir1', 'mydemo.txt'))
