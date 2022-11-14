# 1.导入pymysql
import pymysql

# 2.创建连接对象
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', password='root',
                       database='advanced', charset='utf8')

# 3.获取游标对象
# TODO 游标类型
# 元组游标，获取到的结果集类型就是元组 pymysql.cursors.Cursor,默认值
# cursor = conn.cursor(cursor=pymysql.cursors.Cursor)
# 字典游标，获取到的结果集类型就是字典
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 4.执行sql语句
# sql语句不需要分号
# 返回受影响行数
rows = cursor.execute('select * from student')
print(f'受影响行数：{rows}')

# 5.获取查询结果
# 游标对象只能获取一次结果集
# 获取单个记录
one = cursor.fetchone()
print(one)
# 获取指定条数的记录
many = cursor.fetchmany(2)
print(many)
# 一次性获取所有记录
all = cursor.fetchall()
print(all)

# 6.关闭游标对象
cursor.close()

# 7.关闭连接对象
conn.close()
