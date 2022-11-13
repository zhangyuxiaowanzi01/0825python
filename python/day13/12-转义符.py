# 需求：匹配文件名（完整文件名）
# 文件名：demo.txt cat.jpg  xx.mp4 xx.mp3
import re

filename = input('文件名：')
if re.search(r'^\w{1,32}\.[a-zA-Z]{2,4}[34]?$', filename):
    print('文件名格式正确')
else:
    print('文件名格式错误')
