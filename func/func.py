# 函数
# help(xxx) 可以查看函数的说明

# def funcname(parameter_list):
#     pass

# 可以通过sys模块设置递归的最大值
import sys
sys.setrecursionlimit(100000)


def add(x, y):
    result = x + y
    return result


# def print(code):
#     print(code)


def myPrint(code):
    print(code)


add(1, 2)
myPrint('python')
# print('1')
# 报异常：超过递归次数
# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded

a = add(1, 2)
b = myPrint('C#')
print(a, b)


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2
    return damage1, damage2

damages = damage(4, 5)
print(type(damages))
# 返回值不要依赖于下标，不好理解语义
print(damages[0], damages[1])

# 序列解包
skill1_damage, skill2_damage = damage(4, 5)
print(skill1_damage, skill2_damage)



a = 1
b = 2
c = 3
# 可简写为
a, b, c = 1, 2, 3

# 序列解包
d = 1, 2, 3
print(type(d))  # tuple类型
a, b, c = d
