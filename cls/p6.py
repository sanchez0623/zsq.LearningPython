import sub.p13

print('name:' + __name__)
# NoneType也属于False
print('package:' + (__package__ or 'no package'))
print('doc:' + (__doc__ or 'no doc'))
print('file:' + __file__)


# 被导入的模块
# name:sub.p13
# package:sub
# doc:
#     this is sub.p13
# file:D:\SourceCode\python\zsq.LearningPython\class-py\sub\p13.py

# 执行的p6.py文件即为入口文件
# 入口文件的name为__main__，就像C#的入口main方法
# name:__main__
# 入口文件不属于任何包
# package:no package
# doc:no doc
# 入口文件的file不显示物理路径
# file:.\p6.py