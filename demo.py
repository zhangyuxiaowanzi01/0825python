import os
import re

for dir in os.listdir():
    if dir.startswith('day') and len(dir) == 4:
        day = re.match('(day)(\d)', dir).groups()[0]
        num = re.match('(day)(\d)', dir).groups()[1]
        print(day + '0' + num)

        os.rename(dir, day + '0' + num)
