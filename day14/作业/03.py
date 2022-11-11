# 将resource/demo目录下的下的目录名字改为day1 -> day01
# 获取demo下的所有资源
import os

resources = os.listdir('demo')

for resource in resources:
    if len(resource) == 4:
        # 提取要修改的资源
        # 分割资源名，重新组合
        name = resource[:3]
        num = resource[-1]
        # 修改资源名
        os.rename(f'demo/{resource}', f'demo/{name}0{num}')
