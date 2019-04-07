# __dict__变量的用法


class Student():
    name = 'demo'
    age = 18

    def __init__(self, name, age):
        # 错误方式：给'类变量'赋值
        name = name
        age = age
        # 正确：给'实例变量'赋值
        # self.name = name
        # self.age = age


student1 = Student('zsq', 18)
# 当__dict__找不到该变量name时，会向上寻找——>类似于C#去找父类的变量
# 所以此处会输出Student.name的值
print(student1.name)
print(Student.name)

# __dict__变量 以字典dict的形式 存着类里面所有的变量和方法
print(student1.__dict__)
print(Student.__dict__)