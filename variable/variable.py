a = [1, 2, 3]
b = [4]

print(a * 3 + b + a)

# 变量命名 可读性
# 命名规则
# 1.不用系统变量名
# 2.区分大小写

a = 1
b = a
a = 3
print(b)
#b=1

a = [1, 2, 3]
b = a
a[0] = '1'
print(b)
#b=['1',2,3]

# 值类型(不可改变)——赋值后会重新生成一个字段
# int str tuple

# 引用类型（可改）
# list set dict

# 可通过id()函数证明
a = 'hello'
print(id(a))

a = a + ' world'
print(id(a))


# 修改变量后，id值没有改变
a = [1,2,3]
print(id(a))
a[0] = '1'
print(id(a))

b=[1,2,3];
b.append(4)

c=(1,2,3)
# c.append(4) #异常


# 可'修改'的嵌套元组
a=(1,2,3,[1,2,4]);
a[2]=4;# 异常，不可改
print(a)
a[3][2]='4'# 实际上改变的是列表
print(a)
