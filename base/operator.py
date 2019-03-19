# 算数运算符
# + - * /
# % （取余）
# //（除法取整）
# **（乘方）


# 赋值运算符
# =
# += -= *= /=
# %=
# //=
# **=
# 没有++和--


# 关系运算符
# == !=
# > <
# >= <=
# str list tuple等 都可以比较大小，比较的是ascii编码


# 逻辑运算符
# and
# or
# not


# 成员运算符
# in
# not in

# 身份运算符
# is
# is not

a = 1
print(type(a) == int)
print(isinstance(a, int))
print(isinstance(a, (str, float)))
# type类型判断  不能判断变量的子类是否属于某种类型
# isinstance类型判断  可以

# 对象三个特征：id，value，type

# 位运算符
# &(按位与) |(按位或) ^(按位异或) ~(按位取反)
# <<(左移动) >>(右移动)
# 主要用于二进制运算
