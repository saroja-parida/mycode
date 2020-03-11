#Inheritance 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def changeName(self, name, age):
        self.age = age
        self.name = name
    def __str__(self):
        return self.name + "----" + str(self.age)

#========Inheritance class=============
class student(Person):
    def __init__(self, name, age, grade, test):
        Person.__init__(self, name, age)
        self.grade = grade
        self.test = test
    def changegpa(self, test):
        self.test = test
    def __str__(self):
        return Person.__str__(self) + "--" + str(self.age) + "--"+ self.grade + "--" + self.test



P1 = student("saroj",37,"A","math")
print(P1)

P1.changegpa("hindi")
print(P1)

P1.changeName("Rahul",20)
print(P1)
