"""
读取一个py文件，显示除了以井号(#)开头的行以外的所有行
"""

# 打开文件-r
f = open('02.py', 'r', encoding='utf8')
# readlines读取
data_list = f.readlines()
for data in data_list:
    if not data.startswith('#'):
        print(data)

# 关闭文件
f.close()
