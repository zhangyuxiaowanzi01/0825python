"""
需求：
1.定义两个变量，分别记录年龄和是否携带身份证
2.如果满18岁，并且带有身份证，运行进入网吧上网。
"""
age = int(input('年龄：'))
is_card = int(input('是否由身份证【1有|0没有】：'))  # 1 0

if age >= 18 and is_card:
    print('可以上网')
else:
    print('大咩')



