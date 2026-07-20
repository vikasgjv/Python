# dictionary methods

emp = {
    'v' : 101,
    'i' : 103,
    'k' : 106,
    'a' : 110
}

emp2 = {
    's' : 107,
    'g' : 102,
    'j' : 200
}

emp.update(emp2) #adds emp2 key:values to the emp
print(emp)
emp2.clear() #clears all the key:vlaues in the emp
print(emp2)

emp.pop('g') #remove g key :value
print(emp)

emp.popitem() #removes last key:value pair
print(emp)

del emp2 #deletes

del emp['a'] #delets only a keyvlaue
print(emp)
