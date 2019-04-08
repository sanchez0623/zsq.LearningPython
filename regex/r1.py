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


# '\D'——匹配一个数字字符，等价于[^0-9]
a3 = 'c0c++3java5C#8python2js'

r3 = re.findall('\D', a3)
print(r3)