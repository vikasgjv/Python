import random
import string
word = input("enter the word : ")

def code(w):
    if(len(w)<=3):
        letter = w.remove[0]
        w.add[letter]
        random_letters = "".join(random.choices(string.ascii_letters, k=3))
        for i in range(3):
            w.add[[i],random_letters]
        print(w)
    else:
        print(w.reverse())

code(word)

        
