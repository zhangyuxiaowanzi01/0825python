# 需求：利用标题查询新闻
import pymysql

conn = pymysql.connect(
    user='root', password='root',
    database='advanced', charset='utf8'
)

cursor = conn.cursor()

# 接收用户输入的标题
title = input('title:')
clicks = input('clicks')
# 组织sql语句
# TODO sql注入解决
# " or 1 = 1 or "
sql = 'select * from news where title = %s or clicks = %s'
rows = cursor.execute(sql, [title, clicks])

# 获取结果集
print(cursor.fetchall())

# 关闭
cursor.close()
conn.close()
