# 正则一些疑问
import re

# 1.为啥都匹配到'\\'
a = 'efq\oewk'
a2 = 'efew\\qegfqeg'

r = re.findall('\D', a)
print(r)
r2 = re.findall('\D', a2)
print(r2)


# 2.为啥匹配到所有 由空字符串组成的结果
a = 'python123java90php'

print(re.findall('', a))


# 3.贪婪是建立在匹配到完整结果的基础上的！！！
s = 'pythhonn123python1234pythho'
r = re.findall('pyth{1,2}?on', s)
print(r)

d = re.findall('pyth{1,2}on', s)
print(d)
# 输出如下：
# ['pythhon', 'python']
# ['pythhon', 'python']
# 为什么会一致呢？
# h{1,2}?不是应该尽可能少的匹配h吗

# 因为贪婪不是首先考虑的，首先考虑的是匹配出的所有结果，然后在结果中选出贪婪或非贪婪。
# 以你的题目为例：
# 若不去掉ON，则前面的第1个匹配是唯一的pythhon，那么就没有贪婪性可言
# 若去掉ON，前面第1个匹配有两种pyth和pythh，然后就可以依据是否贪婪进行选择想要的结果