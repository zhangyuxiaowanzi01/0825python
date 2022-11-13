# 名片存储
cards = [
    {'name': '张三', 'age': 18, 'tel': 111111}
]


def add_card():
    print('====添加名片====')
    # 接收用户数据
    name = input('姓名：')
    age = input('年龄：')
    tel = input('手机：')
    # 组装名片信息
    card_info = {'name': name, 'age': age, 'tel': tel}
    # 添加到列表中[名片盒]
    cards.append(card_info)
    print(cards)
    print('添加成功')


def show_cards():
    print('====查看名片====')
    print(f'姓名\t年龄\t手机号')
    for card_info in cards:
        for info in card_info.values():
            print(info, end='\t')
        print()


def edit_card():
    print('====修改名片====')
    # 接收要修改的姓名
    name = input('要修改名片的姓名：')
    for card_info in cards:
        if card_info['name'] == name:
            # 新的信息
            name = input('姓名：')
            age = input('年龄：')
            tel = input('手机：')
            card_info['name'] = name
            card_info['age'] = age
            card_info['tel'] = tel
            print('修改完成')
            break
    else:
        print('姓名不存在')


def del_card():
    # 接收要删除的姓名
    name = input('要删除的姓名：')
    # 遍历名片列表
    for card_info in cards:
        # 找到要删除姓名的字典
        if card_info['name'] == name:
            # 从名片列中删除
            cards.remove(card_info)
            print('删除成功')
            break
    else:
        # 找不到对应的姓名，提示不存在
        print('姓名不存在')


def main():
    while True:
        code = input('选择功能[1添加|2显示|3修改|4删除]:')
        if code == '1':
            add_card()
        elif code == '2':
            show_cards()
        elif code == '3':
            edit_card()
        elif code == '4':
            del_card()
        else:
            print('退出系统')
            break


main()
