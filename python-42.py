marks = [23,47,39,49,50,12]

# for index,mark in enumerate(marks):
#     print(index,mark) 
#     if(mark == 49):
#         print('v7')

# print("start index =3")

for index,mark in enumerate (marks,start = 3):  #start the index from 5 insted 0 (from the 1st element it counts from 5)
    print(mark)
    if (index==5):
        print(f"{mark} ->  marks")