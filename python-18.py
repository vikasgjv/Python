# While Loops

i =0
while (i<=5): #runs until the condition is true
    print(i)
    i=i+1

n =int(input("Enter a number :  "))
while(n<=50):
    n = int(input("Enter a number : "))
    print(n)
print("Done with the loop!!")

#decrementing loop
count = 7 
while(count>0):
    print(count)
    count -=1

#while with else loop
count = 7 
while(count>0):
    print(count)
    count -=1
else:
    print("while loop ended and entered to the else statement")