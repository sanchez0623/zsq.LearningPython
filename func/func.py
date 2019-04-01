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


# 函数参数
# 1.必须参数
# 2.关键词参数
# 3.默认参数--默认参数要放在参数列表最后，和C#一致
# 4.可变参数（*）
# *号相当于传了一个tuple参数
def demo(*param):
    print(param)
    print(type(param))

demo(1, 2, 3, 4)

# 和以下类似：
def demo2(param):
    print(type(param))

demo2((1, 2, 3, 4, 5))

# 注意
a = (1, 2, 3, 4)
# 输出二维tuple
demo(a)
# 输入一维tuple
demo(*a)  # 参数使用*号，相当于进行了一次序列解包


# exp2
def squsum(*param):
    sum = 0
    for i in param:
        sum += i * i
    print(sum)


squsum(1, 2)
squsum(*(1, 2))
# can't multiply sequence by non-int of type 'tuple'
# squsum((1,2))
squsum(*[1, 2])
# can't multiply sequence by non-int of type 'list'
# squsum([1,2])

# 5.关键词可变参数（**）
# 相当于传了一个dict

# exp1
def city_temp(**param):
    for c in param:
        print(c)
    # 错误的dict示范
    for k, v in param:
        print(k, ':', v)
    # 正确的dict示范
    for k, v in param.items():
        print(k, ':', v)
    print(param)
    print(type(param))

city_temp(sz='28c', gz='30c', sh='15c')

a = {"a": "12", "b": "23"}
city_temp(**a)