# Multiple Inheritance 

class employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f'The name is {self.name}')

class dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f'The name is {self.dance}')

class employeedancer(employee,dancer): #allows class to inherit attributes and methods from multiple parent class 
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

obj = employeedancer('jackson','moonwalk')
obj.show()
print(employeedancer.mro()) # it shows the how the code track or flow of work