# 类的继承
# py支持多继承，但不建议使用（从C#就可以知道，单继承就可以解决问题了）
from c7 import Human


class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        # 调用父类构造函数
        # 错误
        # Human.__init__(name,age)
        # 不推荐方式（类调用实例方法）
        # Human.__init__(self, name, age)
        # 正确方式
        super(Student, self).__init__(name, age)
        # self.__score = 0

    def marking(self, score):
        if score < 0:
            return '不能是负数'
        self.__score = score
        print(self.name + '分数是：' + str(self.__score))

    def do_homework(self):
        super(Student,self).do_homework()
        print('son method')

student1 = Student('z校', 'z1', 18)
student1.get_name()
print(Student.sum)
print(student1.sum)
print(student1.name)
print(student1.age)

student1.do_homework()
