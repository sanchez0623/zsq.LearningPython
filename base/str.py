# str 
# 单引号，双引号，三引号
# \	转义字符

# 三引号：字符串可换行
print('''
hello world
hello world
''');

print('''\nhello world\nhello world''');

print('hello world');
print('hello\
    world');


# 转义字符
# \t
# \n 换行   \r 回车
# \'

print('hello \\n world');

print('c:\northwind\northtest');
print('c:\\northwind\\northtest');    
# r ——raw  会把字符串变成原始字符串，不进行转义
print(r'c:\northwind\northtest');