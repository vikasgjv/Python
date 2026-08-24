# Hybrid and Hierarchical Inheritance 

#hybrid Inheritance 

class baseclass:
    pass

class derived1(baseclass):
    pass

class derived2(baseclass):
    pass

class derived3(derived1,derived2):
    pass

# Hierarchical Inheritance 

class baseclass:
    pass

class D1(baseclass):
    pass

class D2(baseclass):
    pass

class D3(D1):
    pass
class D4(D2):
    pass