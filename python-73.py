# Magic/Dunder Methods

class employee :
    def __init__ (self,name):
        self.name = name 

    def __str__ (self):
        return f"Name of the employee is {self.name}"
    
    def __call__(self):
        print("hello guys")
    

emp = employee('peter')
print(emp)
emp() #calls __call__ methods