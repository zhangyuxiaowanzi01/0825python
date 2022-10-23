# TODO 多个值赋值给多个变量
a, b, c = 1, 2, 3

print(a, b, c)
print('==' * 20)

# TODO 变量交换：2个变量值交换
m = 100
n = 10
# 第一种：传统方式
x = m
m = n
n = x
print(m, n)
# 第二种：python方式
m, n = n, m
print(m, n)
print('==' * 20)

# TODO 多个变量赋相同的值
num1 = num2 = num3 = 100
print(num1, num2, num3)
