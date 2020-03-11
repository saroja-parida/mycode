class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count +=1
    def changeName(self, name, age):
        self.age = age
        self.name = name
    def getcount(self):
        return Person.count
    def __str__(self):
        return self.name + "----" + str(self.age)

P1 = Person("saroj",37)
print(P1)
print(P1.getcount())

P1.changeName("himanshu",34)
print(P1)

P2 = Person("saroj1",47)
print(P1)
print(P2.getcount())

P3 = Person("saroj2",38)
print(P3)
print(P3.getcount())
