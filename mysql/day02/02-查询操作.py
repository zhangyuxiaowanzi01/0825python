# TODO 1.导入pymysql
import pymysql

# TODO 2.创建连接对象
# host:主机地址（域名|ip地址），默认值：localhost
# port:MySQL服务的端口号，默认值：3306
# user:账号
# password:密码
# database:要操作的数据库
# charset:python和服务端通信的字符集
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', password='root',
                       database='advanced', charset='utf8')

# TODO 3.获取游标对象
# 作用：执行sql语句，获取查询结果集
cursor = conn.cursor()

# TODO 4.执行sql语句
# sql语句不需要分号
# 返回受影响行数
rows = cursor.execute('select * from student')
print(f'受影响行数：{rows}')

# TODO 5.获取查询结果
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

# TODO 6.关闭游标对象
cursor.close()

# TODO 7.关闭连接对象
conn.close()
