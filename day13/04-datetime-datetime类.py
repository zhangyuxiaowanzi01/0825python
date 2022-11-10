from datetime import datetime
import time

# TODO 类方法
# datetime.today()	当前时间，localtime。
"""
datetime_obj = datetime.today()
print(datetime_obj)
print(type(datetime_obj))
"""

# datetime.now()	当前的时间。
"""
datetime_obj = datetime.now()
print(datetime_obj)
"""

# datetime.utcnow()	当前格林时间。
"""
print(datetime.utcnow())
"""

# datetime.fromtimestamp()	将时间戳的转换为时间。
"""
timestamp = time.time()
print(datetime.fromtimestamp(timestamp))
"""

# TODO datetime.strptime(str,fmt)
# datetime.strptime(str,fmt)	按照fmt的格式解析字符串生成datetime。 字符串时间-》对象时间
"""
datetime_str = '2022-10-1 10:10:10'
datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
print(datetime_obj)
print(type(datetime_obj))
"""

# TODO 对象方法
# datetime.date()	返回一个date对象。
"""
datetime_obj = datetime.now()
date_obj = datetime_obj.date()
print(date_obj)
print(type(date_obj))
"""

# datetime.time()	返回time对象。
"""
datetime_obj = datetime.now()
time_obj = datetime_obj.time()
print(time_obj)
print(type(time_obj))
"""

# TODO datetime.strftime(fmt)
# datetime.strftime(fmt)	按照fmt的格式生成字符串。  对象时间-》字符串时间
datetime_obj = datetime.now()
datetime_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
print(datetime_str)
print(type(datetime_str))
