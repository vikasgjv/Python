# Instance variables vs Class variables

class employee:
    company_name = 'google' # Class variable associted with the class 
    def __init__(self,name):
        self.name = name
        self.raise_salary = 10 # instance variable only assicoted with the instance (init method) or local variable
    def show(self):
        print(f"name of the employee is {self.name} and the salary is raised by {self.raise_salary} percent in {self.company_name}")

emp1 = employee('jon')
emp1.raise_salary = 25
emp1.show()

emp2 = employee('tony')
emp2.show()