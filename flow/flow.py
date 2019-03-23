#  if else
temp=True
if temp:
    print('1')
    print('2')
else:
    print('4')
print('3')

# '常量'用全大写表示
# python没有任何方式命名一个常量
# 只能用约定俗称的全大写表示，其实还是可以被更改的
ACCOUNT='zsq'
PASSWORD='123'

print('input account')
user_account=input()

print('input password')
user_password=input()

if ACCOUNT==user_account and PASSWORD==user_password:
    print('success')
else:
    print('failure')

#  for

#  while