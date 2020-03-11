class pet:
    a=1
    lt =[]
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def get_name(self):
        return self.name
    def get_species(self):
        return self.species
    def __str__(self):
        return "The name is %s and species %s"%(self.name,self.species)

tommy=pet("happy","dog")
sp2=pet("new","cat")

print tommy
print sp2

print tommy.get_name()
print tommy.get_species()
