# Local vs Global Variables 

x = 5 #acts as a global variable - can be accesed in both outside the func or inside the func
print(x)

def func():
    y = 7 #local variable defined within func
    print("helllo")
    print(x) # 5 is printed within function bcz x i global variable
    print(y)  # 7 is printed bcz y (local variable) defined within func

func()

# print(y) #shows error bcz y is a local variable of func and it cannot be accesed outside the function.

# global keyword

a = 20
print(f"global value of a is {a}")

def change():
    global a
    a = 10
change()
print(f"after changing the value of global var {a}")