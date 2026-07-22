# 'is' vs '==' 

a = 3
b = 3

print(a is b) #compares exact  location of object in memory (here a,b are constant so python alocates same location for both)
print(a==b) #compares value

c = [1,2,4]
d = [1,2,4]
print(c is d) #(false) its a list so it can be changeable so python alocates in different location
print(c==d) #gives true bcz the values are same 

a1 = (4,5,6)
a2 = (4,5,6)
print(a1 is a2) #both are true bcz here it tis tuple immutable (constant) so allocates sam location
print(a1 == a2)