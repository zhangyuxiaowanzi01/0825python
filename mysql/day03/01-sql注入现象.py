# 需求：利用标题查询新闻
import pymysql

conn = pymysql.connect(
    user='root', password='root',
    database='advanced', charset='utf8'
)

cursor = conn.cursor()

# 接收用户输入的标题
title = input('title:')
# 组织sql语句
sql = f'select * from news where title = "{title}"'
rows = cursor.execute(sql)

# 获取结果集
print(cursor.fetchall())

# 关闭
cursor.close()
conn.close()
