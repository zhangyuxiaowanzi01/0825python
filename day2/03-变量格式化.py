""""""
name = input('姓名：')
age = int(input('年龄：'))
height = float(input('身高：'))


# 姓名：xxx 年龄：xxx
# print('姓名：', name, '年龄:', age)

# TODO f格式化： 常用
# print(f'姓名：{name}, 年龄：{age}')

# TODO %格式化  %s:字符串  %d：整数 %f：浮点数
""""""
print('姓名：%s' % name)
print('年龄: %d' % age)
print('姓名：%s，年龄：%d, 身高：%f' % (name, age, height))
print('姓名：%s，年龄：%s, 身高：%s' % (name, age, height))


# %f格式化方式，小数点位数的调整
"""
num1 = 10.11
print('num1:%.2f' % num1)
"""

# %d格式化方式，调整数的位数，如果位数不够，填充0
"""
num2 = 100
print('num2:%04d' % num2)
"""

# 手机号 验证码:生成6位的验证码
import random  # 随即模块，用来产生随机数
# print(random.randint(1, 999999)) # 返回1-999999之间的随机数
code = '%06d' % random.randint(1, 999999)
print(code)





