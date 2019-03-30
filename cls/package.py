# 包（一个包就是文件夹）
# 必须包含一个__init__.py文件才是一个包，不然只是一个文件夹
# __init__.py的名字就是包名

# 命名空间
# a.aa
# b.aa
# a.__init__ 错误————>正确为a

# import
import p1
print(p1.p1a)
# import xx.yy.zz as x
# 简化

# from import
from p1 import p1a
print(p1a)

# 会引入所有元素，不推荐使用
# from p1 import *

# 引入多个变量，导致代码行长度太长
# 可以使用（）将需要导入的变量放一起
# from p1 import (p1a.a,pa1.b,
# p1a.c)

# 执行一个py文件时，会自动执行__init__.py
# 感觉类似于C#的构造函数

# 避免循环导入，和C#的循环引用是一个道理


# 模块
# 当导入一个模块的时候，就会执行模块里面的代码

# 模块内置变量
# dir()--返回当前模块所有变量
infos = dir()
print(infos)
# 输出['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

import sys
infos = dir(sys)
print(infos)
# 输出sys模块的所有变量


# 相对导入、绝对导入
# 入口文件不支持相对导入
# import xx.yy  绝对导入
# from .xx.yy import *  相对导入
# . 同级  .. 上级  以此类推

# 类

# 函数，变量