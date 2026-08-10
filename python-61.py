# Inheritance

class employee:
    def __init__ (self,name , id):
        self.name = name
        self.id = id
    
    def showdata(self):
        print(f"the detailes are : {self.name} and  ID is {self.id} ")

class programmer(employee):
    def show(self):
        print("The default programing language is python")



e1 = programmer('vikas',101)
e1.showdata()
e1.show()