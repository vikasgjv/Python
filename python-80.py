# Multilevel Inhertience 

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

class Puppy(Dog):
    def __init__(self, name, breed, age):
        Dog.__init__(self, name, breed)
        self.age = age

    def show_details(self):
        Dog.show_details(self)
        print(f"Age: {self.age}")

p1 = Puppy("Tommy", "Golden Retriever", 2)
p1.show_details()