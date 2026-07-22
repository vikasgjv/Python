#Constructors

# parameterized Constructors
class person:
    def __init__(self,n,o):
        print("hello ") #it prints every time when ever a new obj is created on this class
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person("raju","programmer")
b = person('hari','designer')

a.info()
b.info()


# Default Constructors
class per():
    def __init__(self):
        print("This one is Default Constructors")

c = per()
