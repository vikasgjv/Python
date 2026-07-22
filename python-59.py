# Decorators

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("tThanks for using this function")
    return mfx

@greet   
def hello():
    print("hello world")

hello()

#to pass arguments use *args and **kwargs -. gives in list ,tuple

def greets(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("tThanks for using this function")
    return mfx

@greets
def sum(x,y):
    print(x+y)

sum(10,2)
