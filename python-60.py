# Getters & Setters

class myclass:
    def __init__ (self,value):
        self.value2 = value

    def show(self):
        print(f"The value is {self.value2}")
   
    @property               #Getter
    def ten_value(self):
        return 10*self.value2

    @ten_value.setter
    def ten_value(self, new_value):
        self.value2 = new_value /10



obj = myclass(10)
obj.ten_value = 69
print(obj.ten_value)
obj.show()
