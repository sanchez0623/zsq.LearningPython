# 表达式 是 运算符 和 操作数 所构成的序列
# 1.有序
# 2.函数也属于一种运算符

# 表达式优先级
# **同级运算符之间也有优先级
# 如not > and > or

a = 1
b = 2
c = 3
d = 4
print(b or c and d)


a = 1
b = 2
c = 2
print(not a or b + 2 == c)
# 正确的运算顺序
print((not a) or ((b + 2) == c))


print(not (a or b) + 2 == c)

