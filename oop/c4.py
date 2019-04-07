# 实例类内部 访问 类变量
# 1.使用类名.变量名
# 2.使用self.__class.变量名


class Student():
    name = 'demo'
    age = 18
    sum1 = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(sum1)  # 此处不会打印出类变量，报异常
        print(Student.sum1)
        print(self.__class__.sum1)

