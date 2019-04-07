# 类
# 面向对象
# 类和对象


class Student():
    name = 'demo'
    age = 18

    # 构造函数
    # 1.不返回，或者只能返回None类型——return None
    # 2.self表示当前实例
    def __init__(self, name, age):
        # 错误方式：给'类变量'赋值
        # name = name
        # age = age
        # 正确：给'实例变量'赋值
        self.name = name
        self.age = age

    # 定义方法需要加默认参数self
    def print_file(self):
        # 调用类变量时，要加self.xxx
        print(self.name)
        print(str(self.age))


# student = Student()
# student.print_file()

# student = Student()
# a = student.__init__()
# print(a)
# print(type(a))

student1 = Student('zsq', 18)
print(student1.name)
student2 = Student('sanchez', 19)
print(student2.name)
print(Student.name)


print(student1.__dict__)
print(Student.__dict__)