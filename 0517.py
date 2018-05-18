class Student(object):
    name = "张三"
    age = 19
    scores = (78,89,91)
    @classmethod
    def get_name(cls):
        print("学生的姓名为:%s"%cls.name)
    def get_age(cls):
        print("学生的年龄为:%d"%cls.age)
    def get_course(cls):
        print("学生的最高成绩为:%d"%(max(cls.scores)))

student = Student()
student.get_name()
student.get_age()
student.get_course()
