"""
如何将'python'赋给列表的第三个值，而列表保存在名为bags的变量中？\
bags = [2, 4, 6, 8, 10]
"""
bags = [2, 4, 6, 8, 10]
# 添加
bags.insert(2, 'python')
print(bags)

# 修改
bags[2] = 'mysql'

print(bags)