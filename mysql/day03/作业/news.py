"""
使用python完成, 封装在类中：
a. 一次性添加5条记录
b. 根据用户输入的标题删除记录

分析：
类名：News
方法：
    add_five_data
    del_data_by_title
"""
import pymysql
from datetime import datetime


class News:
    def __init__(self):
        self.conn = pymysql.connect(user='root', password='root',
                                    database='advanced', charset='utf8')
        self.cursor = self.conn.cursor()

    def add_five_data(self):
        """一次性添加5条记录"""

        title = input('title:')
        author = input('author:')
        content = input('content:')
        click = int(input('click:'))

        try:
            for i in range(1, 6):
                sql = f"INSERT INTO news(title, author, content, pub_date, clicks) " \
                      f"VALUES('{title + str(i)}', '{author + str(i)}', '{content + str(i)}', '{datetime.now()}', {click + 1})"
                print(sql)
                # self.cursor.execute(sql)1
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            print('添加成功')
            self.conn.commit()

    def del_data_by_title(self):
        """根据用户输入的标题删除记录"""
        # 接收用户输入的标题
        title = input('title:')

        # 判断标题是否存在
        sql = f'select * from news where title = "{title}"'
        print(sql)
        rows = self.cursor.execute(sql)
        if rows:
            # 存在则执行删除操作
            try:
                rows = self.cursor.execute(f'delete from news where title = "{title}"')
            except Exception as e:
                print(e)
                self.conn.rollback()
                print('删除失败')
            else:
                self.conn.commit()
                print('删除成功')
        else:
            # 不存在则提示不存在
            print('标题不存在')

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    news = News()
    # 添加5条数据
    # news.add_five_data()

    # 根据标题删除数据
    news.del_data_by_title()
