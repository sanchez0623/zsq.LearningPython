# 正则表达式

import re

a = 'c|c++|java|C#|python|js'

r = re.findall('python', a)

if len(r) > 0:
    print(r)
else:
    print('nothing')


# '\d'——匹配一个数字字符，等价于[0-9]
a2 = 'c0c++3java5C#8python2js'

r2 = re.findall('\d', a2)
print(r2)


# '\D'——匹配一个非数字字符，等价于[^0-9]
a3 = 'c0c++3java5C#8python2js'

r3 = re.findall('\D', a3)
print(r3)


# [xyz]、[x-z]——匹配字符集
a4 = 'abc,acc,adc,aec,afc,ahc'

r4 = re.findall('a[cf]c', a4)
print(r4)


# [^xyz]、[^x-z]——不匹配字符集
a5 = 'abc,acc,adc,aec,afc,ahc'

r5 = re.findall('a[^cf]c', a5)
print(r5)


# \w 匹配[A-Za-z0-9_中文]
a6 = 'py111java222C#333你好'

r6 = re.findall('\w', a6)
print(r6)


# # \W 匹配非[A-Za-z0-9_中文]
a7 = 'py111 java\t222C#333你好'

r7 = re.findall('\W', a7)
print(r7)


# \s 匹配所有不可见字符，[ \f\n\r\t\v]
# \S 匹配所有可见字符,非[ \f\n\r\t\v]
a7 = 'py111 java\t222C#333\r你好'

r7 = re.findall('\s', a7)
print(r7)


# 匹配多个字符——{3,7}
# py默认为：贪婪匹配，即匹配到最多才返回
a8 = 'python111 java\t222.net333\r你好'

r81 = re.findall('[a-z]{3}', a8)
print(r81)
r82 = re.findall('[a-z]{3,7}', a8)
print(r82)


# *：匹配0次或无限次
# +：匹配1次或无限次
# ?：匹配0次或1次
a9 = 'pytho0python1pythonn2'

r91 = re.findall('python*', a9)
print(r91)
r92 = re.findall('python+', a9)
print(r92)
r93 = re.findall('python?', a9)
print(r93)


# 单个字符的'?' 和 非贪婪模式的'?' 比较
a10 = 'pytho0python1pythonn2'

r101 = re.findall('python?', a10)
print(r101)
r102 = re.findall('python{1,2}', a10)
print(r102)
r103 = re.findall('python{1,2}?', a10)
print(r103)


# 边界匹配符
# 匹配4-8位qq号
a111 = '100001'
r111 = re.findall('\d{4,8}', a111)
print(r111)

a112 = '101'
r112 = re.findall('\d{4,8}', a112)
print(r112)

a113 = '100000001'
r113 = re.findall('\d{4,8}', a113)
print(r113)
# 只会匹配到前8位

# 加入边界匹配符
a114 = '100000001'
r114 = re.findall('^\d{4,8}$', a114)
print(r114)
r115 = re.findall('\d{4,8}$', a114)
print(r115)
r116 = re.findall('^\d{4,8}', a114)
print(r116)

a115 = '100000001'
r117 = re.findall('000', a115)
print(r117)
r118 = re.findall('^000', a115)
print(r118)
r119 = re.findall('000$', a115)
print(r119)

a116 ='100000002, 20000008, 38849305'
r1110=re.findall('^\d{4,8}$',a116)
print(r1110)
a117 ='20000008'
r1111=re.findall('^\d{4,8}$',a116)
print(r1110)
a118 ='38849305'
r1112=re.findall('^\d{4,8}$',a116)
print(r1110)


# 组
import re
a12 = 'pythonpythonpythonpythonpythonpython'

r12 = re.findall('(python){3}', a12)
print(r12)
# 因为你要匹配连续的3个Python。如果匹配到连续的3个，则显示()中的内容。就是Python


# 匹配模式
import re
a13 = 'pythonC#JavaPhp'

r13 = re.findall('c#', a13, re.I)
print(r13)


# . 匹配除换行符\n以外的所有字符
import re
a14 = 'pythonC#\nJavaPhp'

r141 = re.findall('c#.{1}', a14, re.I)
print(r141)
r142 = re.findall('c#.{1}', a14, re.I | re.S)
print(r142)