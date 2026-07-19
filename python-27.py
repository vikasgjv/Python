#KBC

print("Welcome to KBC !!")
print("for each correct answer the amount will be 1k")
enter = input("to play please press enter button")
 
def kbc(questions,answers):
   sum =0
   for i in  range(len(questions)):
      print(questions[i])
      ans = input("Enter the answer (type it )")
      if ans in answers :
         print("correct answer")
         sum+=1000
      else:
         print("incorrect answer")
   print("you Won amount of :",sum)
         
 

questions = ["1. Which is the largest planet in our Solar System? \n A) Earth \nB) Mars\n C) Jupiter\n D) Venus  ","2. What is the capital of India?\nA) Mumbai\nB) Chennai\nC) New Delhi\nD) Kolkata","3. Which gas do plants absorb from the atmosphere?\n A) Oxygen\nB) Carbon Dioxide\nC) Nitrogen\nD) Hydrogen"]
answers = ["Jupiter","New Delhi","Carbon Dioxide"]

kbc(questions,answers)