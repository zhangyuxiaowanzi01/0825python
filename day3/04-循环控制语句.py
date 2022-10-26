# break和continue只能在循环体中使用
# TODO break
# break表示终止循环(退出整个循环)
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1

print('==' * 20)

# TODO continue
# 跳过本次循环
i = 0
while i < 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
