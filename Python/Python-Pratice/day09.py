'''
DAY 9
'''

class Person(object):

    def __init__(self, name = '', age = 0):
        self._name = name
        self._age = age

    @classmethod
    def create_nobody(cls):
        return cls("Nobody", 0)

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if (age>0):
            self._age = age

    def __str__(self):
        return "Name: %s, Age: %d" %(self._name, self._age)

    @staticmethod
    def check_age(age):
        if (age < 0):
            return "WTF!"
        elif (0 < age and age < 18):
            return "child"
        else:
            return "adult"

    # @staticmethod
    # def check_age(person):
    #     if (person.age < 0):
    #         return "WTF!"
    #     elif (0 > person.age and person.age < 18):
    #         return "Child"
    #     else:
    #         return "Adult"

    def eat(self, food = "food"):
        print("%s is eating %s." %(self._name, food))

def main():

    person1 = Person("John", 15)
    person2 = Person("Amy", 30)
    print(person1)
    print(person2)
    person1.age = -100
    print(person1)
    person1.age = 16
    print(person1)
    nobody = Person()
    print(nobody)
    print("person1 is", Person.check_age(person1.age))
    print("person2 is", Person.check_age(person2.age))
    person3 = Person.create_nobody()
    print(person3)
    person3.eat("apple")


if __name__ == "__main__":
    main()

