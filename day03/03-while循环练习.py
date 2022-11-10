# 1. 输出1-100
# 计数器
# 功能：计数，控制循环次数。 参与运算

# 计数器
"""
i = 1
while i <= 100:
    print(i)
    i += 1
"""

# 2. 输出1-100的和
"""
i = 1
total = 0
while i <= 100:
    total += i
    i += 1

print(total)
"""

# 3. 输出1-100之间奇数的和
# 奇数-第一种
i = 1
total = 0
while i <= 100:
    if i % 2 != 0:
        total += i
    i += 1

# 奇数-第一种
i = 1
total = 0
while i <= 100:
    total += i
    i += 2

print(total)

# 偶数-第一种
i = 1
total = 0
while i <= 100:
    if i % 2 == 0:
        total += i
    i += 1

# 偶数-第二种
i = 2
total = 0
while i <= 100:
    total += i
    i += 2

print(total)
