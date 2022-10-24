# 流程控制： 程序执行的顺序
# 顺序执行
# 分支语句（条件控制）
# 循环语句

# TODO 单分支
# 表达式：可以一行写完的代码
"""
语法：
if 条件表达式:
    条件成立执行的代码块
说明：
    条件成立： 条件表达式的执行结果是True
    条件表达式的结果：就是True和False
"""
"""
num1 = 100
num2 = 10
if num1 > num2:
    print('num1大于num2')

if num1 < num2:
    print('num1小于num2')

if 1:
    print('1')

if 0:
    print('0')

if 1 == 1 and num1 > num2:
    print('ok')
"""

# TODO 双分支
"""
语法：
if 条件表达式:
    条件成立执行的代码块
else:
    条件不成立执行的代码块
"""
"""
num1 = int(input('num1:'))
num2 = int(input('num2:'))
if num1 > num2:
    print(num1)
else:
    print(num2)
"""

# TODO 多分支
"""
语法：
if 条件1:
    条件1成立执行的代码块
elif 条件2:
    条件2成立执行的代码块
elif 条件n:
    条件n成立执行的代码块
else:
    上面条件都不成立执行的代码块
总结：
前面条件成立，后面的条件直接跳过不执行
"""
# 接收用户输入的分数
score = int(input('分数：'))  # 80

if score >= 90:
    print('完美')
elif score >= 80:
    print('优秀')
elif score >= 70:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('下个班见')



# debug
# 1. 打断点
# 2. debug方式运行代码
# 3. 手动执行代码



