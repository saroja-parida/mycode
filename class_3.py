#Multiple Inheritance 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def changeName(self, name, age):
        self.age = age
        self.name = name
    def __str__(self):
        return self.name + "----" + str(self.age)

class addr:
    def __init__(self, dist, state):
        self.dist = dist
        self.state = state
    def changeDist(self, dist):
        self.dist = dist
    def __str__(self):
        return self.dist + " <= district and state => "+ self.state

#========Inheritance class=============
class student(Person, addr):
    def __init__(self, name, age, grade, test, dist, state):
        Person.__init__(self, name, age)
        addr.__init__(self, dist, state)
        self.grade = grade
        self.test = test
    def changegpa(self, test):
        self.test = test
    def __str__(self):
        return Person.__str__(self) + "--" + str(self.age) + "--"+ self.grade + "--" + self.test + "--" +addr.__str__(self)


P1 = student("saroj",37,"A","math","cuttak","odisha")
print(P1)

P1.changegpa("hindi")
print(P1)

P1.changeName("Rahul",20)
print(P1)

P1.changeDist("Dhenknanl")
print(P1)

P2 = student("saroj1",36,"B","eng","ber","andhra")
print(P2)

P2.changeName("sura",70)
print(P2)
