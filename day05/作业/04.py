"""
假设有一个列表 names = [[“张飞”,”刘备”,”关羽”],[“曹操”,”典韦”,”司马懿”]],
如何将names这个列表通过代码 转变得到如下列表 li=[“张飞”,”刘备”,”关羽”,“曹操”,”典韦”,”司马懿”]
"""
names = [['张飞', '刘备', '关羽'], ['曹操', '典韦', '司马懿']]
new_names = []
for name_list in names:
    for name in name_list:
        new_names.append(name)

print(new_names)
