# dir, __dict__ and help method

#dir
x = [1,2,3]
print (dir(x))
print(x.__add__)

#__dict__ (attribute)

class person :
    def __init__(self,name ,age):
        self.name = name
        self.age = age
        self.version = 2.0

p1 = person ('james',32)
print(p1.__dict__)

#help method

print(help(str))
print(help(person))

