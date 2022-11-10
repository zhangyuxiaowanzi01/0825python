"""
打开模式：r:read, w:write（覆盖写）, a:追加写
        b:二进制操作 +:扩展功能
"""
# TODO r模式，读模式
"""
# 打开文件-读
# f = open('resource/demo1.txt', mode='r', encoding='utf8')
f = open('resource/demo1.txt', encoding='utf8')
# 操作文件
content = f.read()  # 返回读到的内容
print(content)
# 关闭文件
f.close()
"""

# TODO w模式，写模式
"""
# 特点:不存在创建，有内容会覆盖
# 打开文件-w
f = open('resource/demo2.txt', 'w', encoding='utf8')
# 操作文件
f.write('w是覆盖写操作')
# 关闭文件
f.close()
"""

# TODO a模式，追加写
# 特点:不存在创建，有内容会在后面进行追加
"""
f = open('resource/demo3.txt', 'a', encoding='utf8')
f.write('a模式是追加写模式2\n')
f.close()
"""

# TODO b模式，二级制模式，不能单独使用
# 注意：b模式，不能设置encoding
"""
f = open('resource/demo1.txt', 'rb')
print(f.read())
f.close()
"""

# TODO +模式，扩展模式，不能单独使用
# r+ ： 读写模式
f = open('resource/demo1.txt', 'r+', encoding='utf8')
# 读
print(f.read())
# 写
f.write('\nhello mysql')
f.close()
