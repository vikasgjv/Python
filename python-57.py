# classes and objects

class person:
    name = 'vikas'
    age = '20'
    occupation = 'editor'
    
    def info(self):
        print(f"{self.name}  is a  {self.occupation}" ) #self parameter self it implies as 'a' and 'b' object : it prints info a object


a = person() #a - object
b = person() #b - object

a.name = 'vikram'
a.occupation = 'HR'

b.name = 'vicky'
b.occupation = 'software developer'

a.info() # a -> goes to self palce

b.info()  # b -> goes to self palce