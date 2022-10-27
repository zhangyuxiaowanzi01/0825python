list1 = [
    ['python', 'mysql', 'linux'],
    ['apple', 'pear', 'lemon']
]

# 需求
# 把这个列表中的所有元素都遍历出来
# TODO while
i = 0
while i < len(list1):
    j = 0
    item_list = list1[i]  # 小列表
    while j < len(item_list):
        print(item_list[j])
        j += 1
    i += 1
print('==' * 20)

# TODO for
for item_list in list1:
    for item in item_list:
        print(item)
