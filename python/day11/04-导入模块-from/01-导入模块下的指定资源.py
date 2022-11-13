"""
# 导入模块下的指定资源
from 模块名 import 资源名1 [as 别名], 资源名2, ...
"""
# 导入了module1下的name和fn资源
from module1 import name, fn
from module2 import name as m2_name, fn as m2_fn

print(name)
fn()

print(m2_name)
m2_fn()