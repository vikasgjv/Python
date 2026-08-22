# Class Methods

class employee:
    company = 'Apple'

    def show(self):
        print(f"name of the employe is {self.name}  and his company is {self.company}")

    @classmethod # it operates on the whole class rather then specific instance.
    def changecompany (cls,newcompany):
        cls.company = newcompany

emp1 = employee()
emp1.name = 'stark'
emp1.changecompany("telsa")
emp1.show()
print(employee.company)