# 类方法、静态方法
# @classmethod @staticmethod


class Student():

    sum = 0
    name = 'zsq'
    age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义类方法
    @classmethod
    def plus_sum(cls):  # 参数通常命名为cls
        cls.sum += 1
        print(cls.sum)

    # 静态方法
    @staticmethod
    def add(x,y):
        print('static method')
        print(Student.sum)# 静态方法访问类变量
        # print(self.name) 静态方法不能访问实例变量
        return x+y


# student1 = Student('z1', 11)
# # student1.plus_sum() # 实例也可以调用类方法，但是不建议这么用，会导致意义不明确
# Student.plus_sum()
# student2 = Student('z2', 12)
# # student2.plus_sum()
# Student.plus_sum()
# student3 = Student('z3', 13)
# # student3.plus_sum()
# Student.plus_sum()

student1 = Student('z1', 11)
Student.plus_sum()
student1.add(1, 2)
Student.add(1, 2)
