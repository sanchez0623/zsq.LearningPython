# 1.整形 int
# 其他语言有short，int，long

# 2.浮点数 float
# 其他语言有float，double
# py的float相当于其他语言的double

print(type(1));
print(type(-1));
print(type(1.1))

print(type(1+1.1));
print(type(1+1.0));

print(type(1*1));
print(type(1*1.0));

# 输出float
print(type(2/2));
# 输出int————'//'表示整除
print(type(2//2));


# number:数字

# bool ：首字符大写，——数字类型的一种
#       True 非0，非空字符串，数组，元组
#       False 0 ，空字符串，空数组，空元组

print(type(True));
print(type(False));

print(int(True));
print(int(False));

print(bool('1'));
print(bool(''));

print(bool([1]));
print(bool([]));

print(bool({1}));
print(bool({}));

print(bool(None));


# complex:复数
print(36j);