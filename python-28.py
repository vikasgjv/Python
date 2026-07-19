#f-string (formating-string)

name = input("Enter your name : ")
country = input('enter Your country : ')
bio = f'hi my name is {name} and my country is {country}.'
print(bio)

price = 14.04563
final_price = f"total price is {price:.2f}" # 2f prints in 2 decimal point value if you want 3 :.3f
print(final_price)

print(f"{2*5}") #we can use f-string in this way as well
print(type(f"{2*5}")) #string