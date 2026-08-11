#Static Methods

class math:
    
    @staticmethod
    def add(a,b): #nop need to self parameter
        return a + b
    
a = math()
#two ways to access 
print(a.add(10,2))
print(math.add(10,5))