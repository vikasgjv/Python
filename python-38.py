# Raising custom errors

a = int(input("enter a number bewteen 5 and 10 : "))
if (a<5 or a>10):
    raise ValueError("value enterd is not valid")
else:
    print(a)






