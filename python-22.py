# Introduction to Lists

marks = [10,50,33,49]
print(type(marks))
print(marks)
print(marks[0])
print(marks[3])
marks.append(45) #added to last
print(marks)

# negtive index

print(len(marks))

print(marks[-1]) # works as len(marks) - 1 -> 5 - 1 = 4 (prints 4th index)

if 33 in marks:
    print("present")
else:
    print('not pressent')

 
if "vi" in "vikas":
    print("yes")

#to print all elemnts in py
print(marks) #with brackets
print(*marks) #without brackets
print(marks[:]) #slicing to print all 

print(marks[0:5:2]) #jumping index-2


#list comprehension
list = ["vikas","jon snow","walter white","rocky"]
list2 =[i for i in list] #it takes all the values from list to list2
print(list2)

list3 = [name for name in list if "i" in name] #loop with condition
print(list3)

#to print odd in range 10
odd = [i for i in range(11) if i%2 != 0]
print(odd)