#operator overloading

class vector:
    
    def __init__(self,i,j,k):
        self.i =i
        self.j =j
        self.k =k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):                # Here, + is overloaded to add two vector objects.
        return vector(self.i + x.i , self.j +x.j , self.k+ x.k)
    
v1 = vector(2,3,5)
v2 = vector (4,4,1)
print(v1+v2)