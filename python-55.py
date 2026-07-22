import random
print("Welcome to snake-water-gun game")
name = input("Enter you name : ")
print(f"{name} there will be  a three round match ")


w =0
s = 1
g =2

com = random.randint(0,2)
user = int(input(f" Enter 0 for Water :  \n Enter 1 for Snake : \n Enter 2 for Gun : "))



def game(x,y):
    if x == y :
        print('Draw')
    elif x >y and y !=0:
        print('computer won')
    elif x>y and y==0:
        print(f'you won') 
    elif x<y and x==0:
        print("computer won") 
    else :
        print("you won")
    print("computer choosed water") if com ==0 else print("computer choosed snake") if com ==1 else print("computer choosed Gun")

 
   
game(com,user)
 
    