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