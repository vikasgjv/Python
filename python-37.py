# Finally Clause / keyword

def func():
    try:
        l = [1,2,4,5]
        a = int(input("enter a number :  "))
        print(l[a])
        return 1
    except:
        print("some error occured")
        return 0

    finally:                          #it  excutes just before the return 
        print("it always executes")

print(func())