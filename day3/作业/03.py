"""
判断判断并且提示成绩的等级（A、B、C）。
90-100:A
80-90:B
80以下：C
"""
# 接收分数
score = int(input('分数：'))  # 1 - 100   120

# 根据分数，输出等级
# 传统写法
"""
if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score < 90:
    print('B')
else:
    print('C')
"""

# 简洁写法
if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
else:
    print('C')
