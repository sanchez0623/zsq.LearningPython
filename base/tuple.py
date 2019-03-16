#tuple

print((1, 2, 3, 4, 5))
print(type((1, 2, 3, 4, 5)))

print((1, 2, "hello", "world", True, (1, 2), (True, False)))
print(type((1, 2, "hello", "world", True, (1, 2), (True, False))))

#基础操作

#返回单个元素
print(("1", "2", "3", "4")[0])

#返回list
print(("1", "2", "3", "4")[0:2])
print(("1", "2", "3", "4")[-1:])

print(("1", "2", "3", "4") + (5, 6))
print(("1", "2", "3", "4") * 3)

#特殊类型
print(type(1))
print(type((1)))
#为何不是元组
print(type('hello'))
print(type(('hello')))
#为何不是元组

print(type(('hello', )))
#一个元素的时候要加逗号才能表示元组

# 面试可以出题
# print(type(1));
# print(type((1)));
# print(type((1,2,3)));
# print(type([1]));

# 当他为一个元素时，IDE无法区分是int还是tuple，
# 如（1+1）*2，此时无法得知（1+1）的类型，
# 所以规定如果tuple为一个元素，则需要写成(1,)

# 序列类型
# str,list,tuple
