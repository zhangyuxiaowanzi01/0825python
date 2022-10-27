"""
使用while，完成以下图形的输出
*
* * *
* * * * *
* * * * * * *
* * * * * * * * *
"""

i = 0
while i < 5 * 2:
    j = 0
    while j <= i:
        print('*', end=' ')
        j += 1
    print()
    i += 2

