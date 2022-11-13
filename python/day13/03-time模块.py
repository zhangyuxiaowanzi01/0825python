import time

# TODO time.time()
# time.time() 重点	返回一个距Epoch的秒数，是浮点数。 时间戳：1970年1月1月1号0时0分0秒到现在的秒数。
"""
while True:
    print(time.time())
"""

# TODO time.sleep(n=seconds)
# 程序休眠时间

# time.gmtime([seconds])	将秒数转化为年月日时分秒，以UTC时间为标准。
"""
print(time.gmtime())
print(time.gmtime(120))
"""

# time.localtime([seconds])	将秒数转化为年月日时分秒，以当地时间为标准。
"""
print(time.localtime())
print(time.localtime(130))
print(type(time.localtime(130)))
"""

# time.ctime([seconds])	    返回年月日时分秒的字符串。
"""
print(time.ctime())
print(time.ctime(120))
print(type(time.ctime()))
"""

# time.asctime(tuple)	    从struct_time返回年月日时分秒字符串。
"""
struct_time = time.localtime()
print(time.asctime(struct_time))
"""

# time.mktime(tuple)	    将struct_time转换为秒数
"""
struct_time = time.localtime()
print(time.mktime(struct_time))
"""
# time.strftime(fmt,t)	    按照fmt格式将struct_time显示成字符串。
"""
struct_time = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M:%S', struct_time))
"""

# time.strptime(str,fmt)	将年月日时分秒的字符串按照fmt解析成struct_time结构。
str_time = '2022-11-10 10:31:05'
print(time.strptime(str_time, '%Y-%m-%d %H:%M:%S'))
