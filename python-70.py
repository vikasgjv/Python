# Class Methods as Alternative Constructors

class employee :
    def __init__ (self, name , salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"name of the employee is {self.name} and his salary is {self.salary}")
    
    @classmethod
    def fromstr(cls,string): #used as an constructer for the whole class
        return cls (string.split('-')[0] , int(string.split('-')[1]))


string = "hulk-25000" 
emp1 = employee.fromstr(string)
emp1.show()
 