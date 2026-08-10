# Access Modifiers

# public Access Modifier

class emp:
    def __init__(self):
        self.name = 'vikas'

a=emp()
print(a.name)

# private Access Modifier

class emp2:
    def __init__(self):
        self.__name = 'vicky'

b = emp2()
# print(b.name) #shows error bcz the name variable is  private  cannot be accessed directly
print(b._emp2__name) #can be accessed indirectly this method is called name mangling

# protected access Modifiers

class student:
    def __init__(self):
        self._name = 'raya'

class rank(student):
    pass

obj = rank()
print(obj._name) #its just a naming convection and does not provide any protection or restric access to the member
