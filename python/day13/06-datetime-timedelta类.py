from datetime import datetime, timedelta

# timedelta
# 作用：用于进行时间计算


datetime_obj = datetime.now()

# timedelta对象
timedelta_obj = timedelta(weeks=1)

# 7天之前的时间
day7_ago = datetime_obj - timedelta_obj
print(day7_ago)

# 7天之后的时间
day7_after = datetime_obj + timedelta_obj
print(day7_after)
