'''
DAY 8
'''

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age

    def study(self, c_name):
        print("%s is studying %s." %(self.name, c_name))

    def friend(self, other):
        print("%s and %s are friend now." %(self.name, other.name))

    def __str__(self):
        return "Name: %s, Age: %s" %(self.name, self.__age)

stu1 = Student("John", 30)
print("Student name is", stu1.name)
# print("Student age is", stu1.__age) # AttributeError: 'Student' object has no attribute '__age'
print("Student age is", stu1.getAge())
stu1.study("ABC")
print(stu1)

stu2 = Student("Amy", 30)
stu1.friend(stu2)