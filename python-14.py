# If Else Conditional Statements 

a = int(input("Enter your age : "))
print("Your age is : ",a)

if (a>=18):
    print("You can Drive")
else:
    print("You cannot Drive")

#if-elif-else (if any one true it exits)

n = int(input("Enter a number : "))
if (n<0):
    print("negative")
elif(n==0):
    print("Zero value")
else:
    print("Positive")

print("thank youu")

#nested if statemnets

num =17

if(num<0):
    print("negative")
elif(num>0):
    if(num>0 and num<=10):
        print("num btw 1 and 10")
    elif(num>=10 and num<=20):
        print("num btw 11 and 20")
    else:
        print("num is greater then 20")
else:
    print("num is zero")
