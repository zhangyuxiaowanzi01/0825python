"""
# 导入模块并起别名
import 模块名1 [as 模块1别名], 模块名2 [as 模块2别名,] ...

# 起别名的作用:
# 简化模块名
# 防止名字冲突
"""
import module1 as m1, module2 as m2

module2 = 'hello'
print(module2)

print(m1.name)
m1.fn()

print(m2.name)
m2.fn()
