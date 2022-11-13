"""
while 条件表达式1:
    循环体...
    while 条件表达是2：
    	循环体
"""

"""
需求1：正方形
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""
# 不嵌套
"""
i = 0
while i < 5:
    print('* ' * 5)
    i += 1
"""
# 循环嵌套
"""
j = 0
while j < 5:
    i = 0
    while i < 5:
        print('*', end=' ')
        i += 1
    print()
    j += 1
"""

"""
需求2：三角形
* 
* * 
* * * 
* * * * 
* * * * * 
"""

j = 0
while j < 5:
    i = 0
    while i <= j:
        print('*', end=' ')
        i += 1
    print()
    j += 1

print('==' * 20)

j = 1
while j <=5:
    i = 1
    while i <= j:
        print('*', end=' ')
        i += 1
    print()
    j += 1

