# Exception Handling

a = input("Enter a number : ")
print(f"Mulitplication table of {a} is : ")
    
try :                               
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("give correct input")
                    #if dont use try and except handling thn the code will stop at loop if it gets sny error .
                    #by using it if a error comes at the loop it exceutes remaning lines aftr the loop
print("some random code to run after the loop ")

#ValueError and IndexError

 
try:
    a = int(input("enter a number : "))
    num = [1,3,4]
    print(num[a])
except ValueError:
    print("Invalid input")
except IndexError:
    print("Index Error")