#  if else
temp = True
if temp:
    print("1")
    print("2")
else:
    print("4")
print("3")

# '常量'用全大写表示
# python没有任何方式命名一个常量
# 只能用约定俗称的全大写表示，其实还是可以被更改的
ACCOUNT = "zsq"
PASSWORD = "123"

print("input account")
user_account = input()

print("input password")
user_password = input()

if ACCOUNT == user_account and PASSWORD == user_password:
    print("success")
else:
    print("failure")


a = input()
# a 输入时为字符串
print(type(a))
a = int(a)

if a == 1:
    print("1")
else:
    if a == 2:
        print("2")
    else:
        print("other")

# elif
# 上面的代码可简化为：
if a == 1:
    print("1")
elif a == 2:
    print("2")
else:
    print("other")

#  for
# 遍历 序列，集合，字典
# break 为终止当前循环
# continue 为跳过这一轮

# for target_list in expression_list:
#     pass
b = [1, 2, 3, 4]
for x in b:
    print(x)

for x in b:
    # 不换行，默认为'\n'
    print(x, end=",")

# for target_list in expression_list:
#     pass
# else:
#     pass
# 当for循环完，才执行else
# 如果被break终止掉了，则不会执行else语句


#  while
# 递归的时候适合用while
# 其他循环建议用for

# 两种方式
# while expression:
#     pass

# while expression:
#     pass
# else:
#     pass

counter = 1
while counter <= 10:
    print(counter)
    counter += 1
else:
    print("EOF")

# range:start-闭区间，stop-开区间
for x in range(0, 10, 2):
    print(x)


# 面试题，使用最少3种方式，打印出1,3,5,7
c = [1, 2, 3, 4, 5, 6, 7, 8]
for x in range(0, len(c), 2):
    print(c[x], end=",")

for x in c:
    if x % 2 != 0:
        print(x, end=",")

print(c[0 : len(a) : 2], end=",")

