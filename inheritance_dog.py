"""
inheritance 
continue 
"""
import pet

class dog(pet):
    chases_cat=True
class cat():
    def __init__(self,name):
        self.name=name
    chases_dog=True
    

obj1=dog("newdog","dog")
print obj1
print obj1.getName()
print obj1.count
print obj1.chases_cat
