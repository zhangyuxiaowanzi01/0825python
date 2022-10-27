"""
求解1-100中能被3整除的所有数字的和
"""
total = 0
i = 1
while i <= 100:
    if i % 3 == 0:
        print(i)
        total += i
    i += 1
print(total)
