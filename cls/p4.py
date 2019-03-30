from sub import *

print(p11.a)

# 这里会报异常，因为在执行__init__.py时，__all__变量只引入了p11.py这个文件
# print(p12.d)