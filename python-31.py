#Sets

#unorderd-it can print the elements in any way not in the order how you enterred.

s1 = {1,2,0,2} #it don't considers the duplicate 2
print(s1) 

s2 = {}  #if we create empty set like this..it considerd as an dict so we use -> set()
print(type(s2)) #it gives dictonary

#empty set can be created in this way
num = set() #empty set
print(type(num))

#accesing elements 

info = {'v7',18,19,True,18,'python','v7'}

for value in info:
    print(value) #unordered way
    
print(len(info)) #only unique values len