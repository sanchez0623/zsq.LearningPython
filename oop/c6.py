# 类的公开，私有


class Student():

    sum = 0
    name = 'zsq'
    age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0

    def marking(self, score):
        if score < 0:
            return '不能是负数'
        self.__score = score
        print(self.name + '分数是：' + str(self.__score))

    # 定义类方法
    @classmethod
    def plus_sum(cls):  # 参数通常命名为cls
        cls.sum += 1
        print(cls.sum)

    # 静态方法
    @staticmethod
    def add(x, y):
        print('static method')
        print(Student.sum)  # 静态方法访问类变量
        # print(self.name) 静态方法不能访问实例变量
        return x + y


student1 = Student('z1', 11)
result = student1.marking(-1)
print(result)
student1.marking(59)
# python是动态语言，此处会新创建一个变量__score，而不是原来的的实例私有变量__score
student1.__score = -1
print(student1.__score)

student2=Student('z2',12)
# print(student2.__score) 此处会报错，没有这个变量


# 在定义私有变量时,py会把这个变量重命名,让人看起来是一个'私有变量'
# 但其实还是能访问到的，'私有变量'会被重命名成--> _类名__字段名
# 可通过查看__dict__去看重命名后的变量名
print(student1.__dict__)