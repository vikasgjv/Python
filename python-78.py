#Single inheritence

class animal:
    def __init__(self,name ,species):
        self.name = name
        self.species = species

    def sound(self):
        print('sound made by the animal')

class dog(animal): #it inherits attributes and behaviors including  __init__ and __sound__ method and it overrides  the sound method 
    def __init__(self,name,breed):
        self.name = name
        self.breed  =  breed

    def sound(self):
        print('bark!!!')

a = animal('dog','doggerman')
d = dog('rocky','dog')

a.sound()
d.sound()