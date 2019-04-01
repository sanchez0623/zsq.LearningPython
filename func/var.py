# 变量作用域

# exp1
c = 5

def add(x, y):
    c = x + y
    print(c)# 输出3

add(1, 2)
print(c)# 输出5


# exp2
def demo():
    c = 10
    for i in range(0, 5):
        a = 'a'
        c += 1

    print(c)
    print(a)  # 可以输出a
# py没有块级作用域的概念
# for循环内部定义的变量，可以在外部使用


# exp3
c = 1

def func1():
    c = 2
    def func2():
        c = 3
        print(c)
    func2()

func1()


# exp4
# global关键字
# global定义的变量，也可以被其他模块import并使用

def demo():
    global c
    c = 2

demo()# 必须先调用下，不然c不会被赋值，可以出面试题
print(c)